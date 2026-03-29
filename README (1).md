# Edge CV Safety Monitor

> Real-time computer vision inference pipeline for industrial edge deployment.
> Designed for Roboflow inference API compatibility on NVIDIA Jetson and Linux x86 hardware.

**Author:** Josephine Odusanya  
**Stack:** Python · Bash · OpenCV · Roboflow Inference SDK · Docker  
**Target hardware:** NVIDIA Jetson Orin/Xavier, Ubuntu 20.04/22.04 x86  

---

## What it does

Runs a PPE (personal protective equipment) and zone-violation detection pipeline on an edge device connected to one or more IP/RTSP cameras. Annotated video is displayed locally, and telemetry (FPS, CPU temp, GPU utilisation, detection events) is broadcast over UDP for remote monitoring — across a VPN tunnel in real deployments.

**Detection classes (configurable via Roboflow model):**
- `person` — human presence detection
- `no_helmet` — PPE violation: missing hard hat
- `no_vest` — PPE violation: missing hi-vis vest
- `forklift` — vehicle proximity alert
- `restricted_zone` — zone intrusion alert

---

## Architecture

```
IP/RTSP Camera
    │
    ▼
RTSPReader (threaded, auto-reconnect)
    │
    ▼
InferencePipeline (Roboflow SDK or OpenCV HOG fallback)
    │
    ├──► Annotated video frame (display / RTSP re-stream)
    │
    └──► TelemetryCollector
              │
              ▼
         TelemetryServer (UDP broadcast)
              │
              ▼
         Remote dashboard / monitoring node
```

The RTSP reader runs in a dedicated thread so a dropped stream never blocks inference. Telemetry is broadcast rather than pushed to a fixed endpoint — any device on the subnet (or VPN) receives it without a persistent connection.

---

## Quick start

### Demo (no Jetson, no API key needed)

```bash
# USB webcam fallback — uses OpenCV HOG person detector
python edge_monitor.py --source 0 --display
```

### Roboflow inference

```bash
pip install inference roboflow
python edge_monitor.py \
  --source rtsp://192.168.1.22:554/stream1 \
  --model safety-ppe-monitor/1 \
  --api-key YOUR_KEY \
  --device cuda \
  --display
```

### Docker (Roboflow inference server)

```bash
docker run -p 9001:9001 \
  --env ROBOFLOW_API_KEY=YOUR_KEY \
  roboflow/roboflow-inference-server-gpu:latest
```

---

## Field deployment (Jetson / Linux edge device)

The `deploy.sh` script handles the full site-setup workflow used in real field deployments.

```bash
# Full install: deps, venv, Docker, systemd service, firewall
sudo ./deploy.sh install \
  --source rtsp://192.168.1.22:554/stream1 \
  --api-key rf_abc123

# Check camera before mounting hardware
sudo ./deploy.sh check-camera rtsp://192.168.1.22:554/stream1

# Configure static IP (common at industrial sites with no DHCP)
sudo ./deploy.sh set-ip eth0 192.168.1.100 192.168.1.1

# Print device status report (temp, GPU, net interfaces, service state)
./deploy.sh status

# Tail inference log
./deploy.sh logs
```

The systemd service auto-starts on boot, restarts on crash, and logs to `/var/log/edge-cv-monitor.log`.

---

## Telemetry format

JSON broadcast over UDP every second:

```json
{
  "uptime_s": 15882.4,
  "avg_fps": 28.6,
  "cpu_temp_c": 46.2,
  "gpu_util_pct": 38.0,
  "net": { "interface": "eth0", "state": "UP" },
  "total_detections_last_60s": 12,
  "recent_detections": [
    { "ts": "2026-03-29T14:22:01", "label": "no_helmet", "confidence": 0.941, "bbox": [120, 80, 140, 310] }
  ]
}
```

Listen on any machine:

```bash
python -c "import socket,json; s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.bind(('',5005));
[print(json.loads(s.recv(65536))) for _ in iter(int, 1)]"
```

---

## Network setup notes

| Scenario | Command |
|---|---|
| Check interface state | `ip link show eth0` |
| Bring up interface | `nmcli device connect eth0` |
| Set static IP | `./deploy.sh set-ip eth0 192.168.1.X 192.168.1.1` |
| Open RTSP firewall port | Handled by `deploy.sh install` |
| SSH tunnel for remote access | `ssh -R 9001:localhost:9001 user@remote-host` |

---

## Requirements

```
opencv-python-headless>=4.8.0
numpy>=1.24.0
inference>=0.9.0      # Roboflow SDK (optional — falls back to HOG)
```

Jetson: use system OpenCV from JetPack instead of pip (GPU-accelerated).

---

## Project context

Built to demonstrate the edge-deployment skills relevant to Roboflow Field Engineering:
- Roboflow inference pipeline integration
- NVIDIA Jetson hardware target
- RTSP / IP camera connectivity  
- Linux networking (nmcli, ifconfig, static IP, systemd)
- Bash scripting for field SOPs
- Remote telemetry and monitoring
- Docker-based inference server deployment
