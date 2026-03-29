#!/usr/bin/env python3
"""
Edge CV Safety Monitor
======================
Runs a real-time computer vision inference pipeline on edge devices (Jetson, x86).
Detects safety violations (PPE, restricted zones, anomalies) from RTSP camera streams
and streams annotated video + telemetry to a monitoring dashboard.

Designed for Roboflow inference API compatibility.
Author: Josephine Odusanya
"""

import cv2
import time
import json
import socket
import threading
import argparse
import logging
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from collections import deque

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("/tmp/edge_monitor.log"),
    ],
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Telemetry collector
# ---------------------------------------------------------------------------
class TelemetryCollector:
    """
    Collects system + inference telemetry and exposes it as JSON.
    Mirrors what a Roboflow edge device would push to a remote dashboard.
    """

    def __init__(self, window: int = 60):
        self.window = window  # seconds to keep in rolling buffer
        self._lock = threading.Lock()
        self.events: deque = deque()
        self.fps_samples: deque = deque(maxlen=30)
        self.start_time = time.time()

    # -- system helpers -------------------------------------------------------

    @staticmethod
    def _cpu_temp() -> float:
        """Read CPU temp on Linux (works on Jetson + generic Linux)."""
        try:
            with open("/sys/class/thermal/thermal_zone0/temp") as f:
                return int(f.read()) / 1000.0
        except FileNotFoundError:
            return -1.0

    @staticmethod
    def _gpu_util() -> float:
        """Read GPU utilisation via tegrastats (Jetson) or nvidia-smi."""
        try:
            out = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                timeout=1,
            ).decode().strip()
            return float(out)
        except Exception:
            return -1.0

    @staticmethod
    def _net_interface_status(iface: str = "eth0") -> dict:
        """Check interface state — mirrors nmcli / ifconfig usage in the field."""
        try:
            out = subprocess.check_output(["ip", "link", "show", iface], timeout=1).decode()
            state = "UP" if "state UP" in out else "DOWN"
        except Exception:
            state = "UNKNOWN"
        return {"interface": iface, "state": state}

    # -- public API -----------------------------------------------------------

    def record_detection(self, label: str, confidence: float, bbox: list):
        with self._lock:
            self.events.append({
                "ts": datetime.utcnow().isoformat(),
                "label": label,
                "confidence": round(confidence, 3),
                "bbox": bbox,
            })
            # Prune events older than window
            cutoff = time.time() - self.window
            while self.events and datetime.fromisoformat(
                self.events[0]["ts"]
            ).timestamp() < cutoff:
                self.events.popleft()

    def record_fps(self, fps: float):
        self.fps_samples.append(fps)

    def snapshot(self) -> dict:
        with self._lock:
            avg_fps = (
                sum(self.fps_samples) / len(self.fps_samples)
                if self.fps_samples
                else 0.0
            )
            return {
                "uptime_s": round(time.time() - self.start_time, 1),
                "avg_fps": round(avg_fps, 2),
                "cpu_temp_c": self._cpu_temp(),
                "gpu_util_pct": self._gpu_util(),
                "net": self._net_interface_status(),
                "recent_detections": list(self.events)[-20:],
                "total_detections_last_60s": len(self.events),
            }


# ---------------------------------------------------------------------------
# Roboflow-compatible inference shim
# ---------------------------------------------------------------------------
class InferencePipeline:
    """
    Wraps Roboflow Inference SDK (or falls back to local OpenCV for demo).
    In production, swap the stub below for:
        from inference import get_model
        self.model = get_model(model_id, api_key=api_key)
    """

    # Class-level colours for bounding boxes (one per label)
    COLOURS = {
        "person": (52, 152, 219),
        "no_helmet": (231, 76, 60),
        "no_vest": (230, 126, 34),
        "forklift": (39, 174, 96),
        "restricted_zone": (142, 68, 173),
    }

    def __init__(self, model_id: str, api_key: str | None = None, device: str = "cpu"):
        self.model_id = model_id
        self.api_key = api_key
        self.device = device
        log.info(f"Initialising inference pipeline — model={model_id} device={device}")
        self._setup_model()

    def _setup_model(self):
        """
        Try to load Roboflow hosted model; fall back to OpenCV HOG person detector
        so the demo runs without a GPU or API key.
        """
        try:
            from inference import get_model  # Roboflow inference SDK
            self.model = get_model(self.model_id, api_key=self.api_key)
            self._mode = "roboflow"
            log.info("Roboflow inference SDK loaded.")
        except ImportError:
            log.warning("Roboflow SDK not installed — using OpenCV HOG fallback.")
            self.model = cv2.HOGDescriptor()
            self.model.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            self._mode = "hog"

    def predict(self, frame):
        """Return list of dicts: [{label, confidence, bbox:[x,y,w,h]}, ...]"""
        if self._mode == "roboflow":
            results = self.model.infer(frame)[0]
            return [
                {
                    "label": p.class_name,
                    "confidence": p.confidence,
                    "bbox": [int(p.x - p.width / 2), int(p.y - p.height / 2),
                             int(p.width), int(p.height)],
                }
                for p in results.predictions
            ]
        else:  # HOG fallback
            rects, weights = self.model.detectMultiScale(
                frame, winStride=(8, 8), padding=(4, 4), scale=1.05
            )
            return [
                {"label": "person", "confidence": float(w[0]), "bbox": list(map(int, r))}
                for r, w in zip(rects, weights)
            ]

    def annotate(self, frame, predictions: list) -> None:
        """Draw bounding boxes and labels in-place."""
        for pred in predictions:
            x, y, w, h = pred["bbox"]
            label = pred["label"]
            conf = pred["confidence"]
            colour = self.COLOURS.get(label, (255, 255, 255))
            cv2.rectangle(frame, (x, y), (x + w, y + h), colour, 2)
            cv2.putText(
                frame,
                f"{label} {conf:.0%}",
                (x, max(y - 8, 16)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                colour,
                1,
                cv2.LINE_AA,
            )


# ---------------------------------------------------------------------------
# RTSP stream reader (threaded for latency)
# ---------------------------------------------------------------------------
class RTSPReader:
    """
    Non-blocking camera reader. Works with RTSP, USB (/dev/video0), or file.
    Mirrors field RTSP setup: rtsp://user:pass@192.168.1.X:554/stream1
    """

    def __init__(self, source: str, reconnect_delay: float = 3.0):
        self.source = source
        self.reconnect_delay = reconnect_delay
        self._frame = None
        self._lock = threading.Lock()
        self._running = False
        self._thread: threading.Thread | None = None

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._reader_loop, daemon=True)
        self._thread.start()
        log.info(f"RTSP reader started — source={self.source}")

    def _reader_loop(self):
        while self._running:
            cap = cv2.VideoCapture(self.source)
            if not cap.isOpened():
                log.warning(f"Cannot open stream {self.source}, retrying in {self.reconnect_delay}s")
                time.sleep(self.reconnect_delay)
                continue
            while self._running:
                ok, frame = cap.read()
                if not ok:
                    log.warning("Stream dropped — reconnecting")
                    break
                with self._lock:
                    self._frame = frame
            cap.release()
            time.sleep(self.reconnect_delay)

    def read(self):
        with self._lock:
            return self._frame.copy() if self._frame is not None else None

    def stop(self):
        self._running = False


# ---------------------------------------------------------------------------
# Telemetry UDP broadcaster
# ---------------------------------------------------------------------------
class TelemetryServer:
    """
    Broadcasts JSON telemetry over UDP every second.
    A remote dashboard (or the included web UI) listens on TELEMETRY_PORT.
    In field deployments, this data would go over VPN tunnel / SSH reverse tunnel.
    """

    def __init__(self, telemetry: TelemetryCollector, port: int = 5005,
                 host: str = "0.0.0.0"):
        self.telemetry = telemetry
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.broadcast = ("255.255.255.255", port)
        self._running = False

    def start(self):
        self._running = True
        threading.Thread(target=self._loop, daemon=True).start()
        log.info("Telemetry broadcaster started on UDP broadcast port")

    def _loop(self):
        while self._running:
            payload = json.dumps(self.telemetry.snapshot()).encode()
            try:
                self.sock.sendto(payload, self.broadcast)
            except Exception as e:
                log.debug(f"Telemetry send error: {e}")
            time.sleep(1.0)

    def stop(self):
        self._running = False
        self.sock.close()


# ---------------------------------------------------------------------------
# Main pipeline loop
# ---------------------------------------------------------------------------
def run(args):
    telemetry = TelemetryCollector()
    pipeline = InferencePipeline(args.model, api_key=args.api_key, device=args.device)
    reader = RTSPReader(args.source)
    tel_server = TelemetryServer(telemetry, port=args.telemetry_port)

    reader.start()
    tel_server.start()

    log.info("Edge CV Safety Monitor running. Press Ctrl+C to stop.")
    prev_time = time.time()

    try:
        while True:
            frame = reader.read()
            if frame is None:
                time.sleep(0.05)
                continue

            predictions = pipeline.predict(frame)
            for p in predictions:
                telemetry.record_detection(p["label"], p["confidence"], p["bbox"])

            pipeline.annotate(frame, predictions)

            # FPS overlay
            now = time.time()
            fps = 1.0 / max(now - prev_time, 1e-9)
            prev_time = now
            telemetry.record_fps(fps)
            cv2.putText(frame, f"FPS {fps:.1f}", (12, 28),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

            # Device info overlay
            snap = telemetry.snapshot()
            overlay = (
                f"Temp {snap['cpu_temp_c']}°C  |  "
                f"GPU {snap['gpu_util_pct']}%  |  "
                f"Net {snap['net']['interface']} {snap['net']['state']}  |  "
                f"Det/60s {snap['total_detections_last_60s']}"
            )
            cv2.putText(frame, overlay, (12, frame.shape[0] - 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1, cv2.LINE_AA)

            if args.display:
                cv2.imshow("Edge CV Monitor", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    except KeyboardInterrupt:
        log.info("Interrupted — shutting down.")
    finally:
        reader.stop()
        tel_server.stop()
        cv2.destroyAllWindows()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Edge CV Safety Monitor")
    parser.add_argument("--source", default="0",
                        help="Camera source: RTSP URL, device index (0), or file path")
    parser.add_argument("--model", default="safety-ppe-monitor/1",
                        help="Roboflow model ID (workspace/project/version)")
    parser.add_argument("--api-key", default=None,
                        help="Roboflow API key (or set ROBOFLOW_API_KEY env var)")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda"],
                        help="Inference device")
    parser.add_argument("--telemetry-port", type=int, default=5005,
                        help="UDP port for telemetry broadcast")
    parser.add_argument("--display", action="store_true",
                        help="Show annotated video window")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
