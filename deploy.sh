#!/usr/bin/env bash
# =============================================================================
# Edge CV Monitor — Jetson/Linux Edge Device Setup Script
# Author: Josephine Odusanya
# Compatible: NVIDIA Jetson (JetPack 5+), Ubuntu 20.04/22.04 x86
# =============================================================================
set -euo pipefail

APP_DIR="$HOME/edge-cv-monitor"
SERVICE_NAME="edge-cv-monitor"
VENV="$APP_DIR/.venv"
LOG_FILE="/var/log/edge-cv-monitor.log"
TELEMETRY_PORT=5005

# ── colour output ─────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
info()  { echo -e "${GREEN}[INFO]${NC}  $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*"; }

# ── helpers ───────────────────────────────────────────────────────────────────
require_root() {
  [[ "$EUID" -eq 0 ]] || { error "Run as root (sudo)"; exit 1; }
}

detect_platform() {
  if grep -q "tegra" /proc/device-tree/model 2>/dev/null; then
    echo "jetson"
  elif uname -m | grep -q "aarch64"; then
    echo "arm64"
  else
    echo "x86"
  fi
}

check_network() {
  local iface="${1:-eth0}"
  info "Checking network interface: $iface"
  if ip link show "$iface" &>/dev/null; then
    state=$(ip link show "$iface" | grep -oP "state \K\S+")
    info "$iface state: $state"
    if [[ "$state" != "UP" ]]; then
      warn "$iface is not UP — attempting nmcli bring-up"
      nmcli device connect "$iface" 2>/dev/null || warn "nmcli unavailable; check interface manually"
    fi
  else
    warn "Interface $iface not found. Available interfaces:"
    ip link show | grep -E "^[0-9]" | awk '{print "  " $2}'
  fi
}

set_static_ip() {
  local iface="${1:-eth0}" ip="${2:-192.168.1.100}" gw="${3:-192.168.1.1}"
  info "Setting static IP $ip on $iface via nmcli"
  nmcli con mod "$iface" \
    ipv4.method manual \
    ipv4.addresses "$ip/24" \
    ipv4.gateway "$gw" \
    ipv4.dns "8.8.8.8 1.1.1.1"
  nmcli con up "$iface"
}

configure_rtsp_firewall() {
  info "Opening firewall ports: 8554 (RTSP), $TELEMETRY_PORT (telemetry UDP), 8080 (dashboard)"
  if command -v ufw &>/dev/null; then
    ufw allow 8554/tcp
    ufw allow "$TELEMETRY_PORT"/udp
    ufw allow 8080/tcp
    ufw --force enable
  else
    warn "ufw not found — configure firewall manually"
  fi
}

install_deps() {
  PLATFORM=$(detect_platform)
  info "Platform detected: $PLATFORM"

  info "Updating apt packages"
  apt-get update -qq

  info "Installing system dependencies"
  apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    libopencv-dev python3-opencv \
    v4l-utils \
    net-tools iproute2 \
    curl wget git \
    docker.io \
    2>/dev/null || warn "Some packages may not have installed — check manually"

  if [[ "$PLATFORM" == "jetson" ]]; then
    info "Jetson detected — skipping generic CUDA install (use JetPack CUDA)"
    warn "Ensure JetPack 5.x is installed: https://developer.nvidia.com/embedded/jetpack"
  fi
}

setup_python_env() {
  info "Creating Python virtual environment"
  python3 -m venv "$VENV"
  source "$VENV/bin/activate"
  pip install --upgrade pip -q
  pip install -r "$APP_DIR/requirements.txt" -q
  deactivate
  info "Python environment ready: $VENV"
}

setup_docker_inference() {
  info "Pulling Roboflow inference Docker image"
  # Roboflow's official edge inference container
  docker pull roboflow/roboflow-inference-server-cpu:latest || \
    warn "Could not pull inference container — ensure Docker is running and you have internet"

  info "To start Roboflow inference server:"
  echo "  docker run -p 9001:9001 --env ROBOFLOW_API_KEY=\$YOUR_KEY roboflow/roboflow-inference-server-cpu"
}

install_systemd_service() {
  local source="${1:-rtsp://camera.local:554/stream1}"
  local api_key="${2:-}"
  info "Installing systemd service: $SERVICE_NAME"
  cat > "/etc/systemd/system/${SERVICE_NAME}.service" << EOF
[Unit]
Description=Edge CV Safety Monitor
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$SUDO_USER
WorkingDirectory=$APP_DIR
ExecStart=$VENV/bin/python $APP_DIR/edge_monitor.py \\
    --source "$source" \\
    --model safety-ppe-monitor/1 \\
    --api-key "$api_key" \\
    --telemetry-port $TELEMETRY_PORT
Restart=always
RestartSec=5
StandardOutput=append:$LOG_FILE
StandardError=append:$LOG_FILE
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
EOF

  systemctl daemon-reload
  systemctl enable "$SERVICE_NAME"
  info "Service installed. Start with: systemctl start $SERVICE_NAME"
  info "Check logs with:            journalctl -u $SERVICE_NAME -f"
}

verify_camera() {
  local source="${1:-0}"
  info "Verifying camera source: $source"
  if [[ "$source" =~ ^[0-9]+$ ]]; then
    # USB camera — check v4l2
    device="/dev/video$source"
    if [[ -e "$device" ]]; then
      info "Found USB camera: $device"
      v4l2-ctl --device "$device" --list-formats-ext 2>/dev/null | head -20 || true
    else
      error "USB camera $device not found"
    fi
  else
    # RTSP — test with ffprobe
    info "Testing RTSP stream (5s timeout)..."
    if command -v ffprobe &>/dev/null; then
      timeout 5 ffprobe -v quiet -print_format json -show_streams "$source" \
        && info "RTSP stream OK" || warn "RTSP stream unreachable — check VPN/network"
    else
      warn "ffprobe not installed — cannot pre-check RTSP"
    fi
  fi
}

print_status() {
  info "=== Edge Device Status Report ==="
  echo ""
  echo "  Platform:       $(detect_platform)"
  echo "  Hostname:       $(hostname)"
  echo "  IP addresses:   $(hostname -I)"
  echo "  Uptime:         $(uptime -p)"
  echo ""

  echo "  Network interfaces:"
  ip -brief addr show | awk '{printf "    %-12s %-12s %s\n", $1, $2, $3}'
  echo ""

  echo "  CPU temp:       $(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null | awk '{printf "%.1f°C", $1/1000}' || echo "N/A")"
  echo "  GPU util:       $(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits 2>/dev/null || echo "N/A")"
  echo ""

  echo "  Docker:         $(docker info --format '{{.ServerVersion}}' 2>/dev/null || echo 'not running')"
  if systemctl is-active --quiet "$SERVICE_NAME" 2>/dev/null; then
    echo "  Monitor svc:    RUNNING"
  else
    echo "  Monitor svc:    STOPPED"
  fi
}

# ── subcommand dispatcher ─────────────────────────────────────────────────────
usage() {
  cat << EOF
Usage: $0 <command> [options]

Commands:
  install [--source <rtsp|dev>] [--api-key <key>]
      Full install: deps, venv, systemd service, firewall

  status          Print device status report
  check-camera [source]   Test camera/RTSP connectivity
  set-ip <iface> <ip> <gateway>   Configure static IP
  logs            Tail the application log
  start           Start the systemd service
  stop            Stop the systemd service

Examples:
  sudo $0 install --source rtsp://192.168.1.10:554/stream1 --api-key rf_abc123
  sudo $0 check-camera rtsp://192.168.1.10:554/stream1
  sudo $0 set-ip eth0 192.168.1.100 192.168.1.1
  $0 status
EOF
}

CMD="${1:-help}"
shift || true

case "$CMD" in
  install)
    require_root
    SOURCE="0"; API_KEY=""
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --source)  SOURCE="$2"; shift 2 ;;
        --api-key) API_KEY="$2"; shift 2 ;;
        *) shift ;;
      esac
    done
    check_network
    install_deps
    setup_python_env
    setup_docker_inference
    install_systemd_service "$SOURCE" "$API_KEY"
    configure_rtsp_firewall
    print_status
    info "Installation complete."
    ;;
  status)
    print_status
    ;;
  check-camera)
    verify_camera "${1:-0}"
    ;;
  set-ip)
    require_root
    set_static_ip "${1:-eth0}" "${2:-192.168.1.100}" "${3:-192.168.1.1}"
    ;;
  logs)
    tail -f "$LOG_FILE" 2>/dev/null || journalctl -u "$SERVICE_NAME" -f
    ;;
  start)
    require_root
    systemctl start "$SERVICE_NAME"
    info "Service started"
    ;;
  stop)
    require_root
    systemctl stop "$SERVICE_NAME"
    info "Service stopped"
    ;;
  *)
    usage
    ;;
esac
