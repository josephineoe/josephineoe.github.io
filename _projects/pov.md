---
layout: project
title: "POV (Persistence of Vision)"
description: "An autonomous quadrotor-mounted sensor system designed to maintain persistent visual surveillance of moving targets. Features custom mechanical design, real-time tracking algorithms, and synchronized multi-sensor payload integration."
date: 2024-11-15
categories: [Robotics, Autonomous Systems, Computer Vision, Mechanical Design, Embedded Systems]
featured_image: "/assets/images/projects/pov/pov.gif"
github_url: "https://github.com/josephineoe/POV"
interactive_plot: true

gallery:
  - type: "image"
    file: "/assets/images/projects/pov/pov.gif"
    description: "POV quadrotor system in action"
  - type: "image"
    file: "/assets/images/projects/pov/cad.png"
    description: "CAD design of sensor mount and gimbal system"
  - type: "image"
    file: "/assets/images/projects/pov/kit.png"
    description: "Complete quadrotor kit assembly"
  - type: "document"
    file: "/assets/images/projects/pov/Team 3-Report.pdf"
    description: "Project report and system documentation"

---

## Project Overview

**POV (Persistence of Vision)** is an autonomous quadrotor system designed to maintain continuous visual surveillance of moving targets. The system combines mechanical precision, real-time computer vision algorithms, and coordinated sensor control to track and monitor objects of interest with minimal human intervention.

This project integrates:
- **Aerodynamic platform**: Quadrotor-based aerial system for mobility and maneuverability
- **Gimbal mechanism**: Mechanically stabilized camera mount for steady visual tracking
- **Vision processing**: Real-time target detection and tracking algorithms
- **Autonomous control**: Flight controller integration with computer vision feedback

## System Architecture

### Overall Design

The POV system operates as an integrated platform combining:

1. **Aerial Platform**: Quadrotor with flight stabilization
2. **Sensor Payload**: Mounted camera system with real-time processing capability
3. **Gimbal Control**: Mechanical system for camera pointing and stabilization
4. **Target Tracking**: Vision-based tracking algorithms for autonomous surveillance

### Hardware Architecture

#### Quadrotor Frame Design
- **Configuration**: X-frame layout with 4 rotors
- **Motor system**: Brushless DC motors with electronic speed controllers
- **Battery**: LiPo power source with voltage regulation
- **Flight controller**: Autopilot with IMU and barometer

#### Sensor Mount & Gimbal
**Mechanical Design** (CAD visualization in gallery):
- **Camera bracket**: Lightweight precision mount for stable mounting
- **Gimbal mechanism**: Single or dual-axis stabilization system
- **Vibration isolation**: Isolation mounts to minimize airframe vibration
- **Integration points**: Tool-less assembly for field maintenance

**Features**:
- Lightweight carbon fiber/aluminum construction
- Adjustable viewing angles
- Quick-release payload system
- Balanced mass distribution for flight stability

#### Sensor Payload
- **Primary camera**: High-speed camera for real-time tracking
- **Processing unit**: Onboard computer for vision algorithm execution
- **Communication**: Wireless link to ground control station
- **Power management**: Regulated power distribution for sensors

## Software Architecture

### Vision Tracking Pipeline

```
Camera Frame (1080p @ 30fps)
    ↓
[Target Detection - Object Recognition]
    ↓
[Centroid Calculation]
    ↓
[Motion Prediction]
    ↓
[Gimbal Orientation Command]
    ↓
[Flight Controller Adjustment]
```

### Target Tracking Algorithm

The system processes video frames in real-time to:

1. **Detect targets** using computer vision techniques
2. **Calculate target centroid** in image space
3. **Predict motion** based on velocity vectors
4. **Generate gimbal commands** to keep target centered
5. **Adjust quadrotor flight** if target moves beyond gimbal range

### Autonomous Control Modes

1. **Gimbal tracking**: Camera follows target while quadrotor maintains altitude
2. **Full pursuit**: Quadrotor follows target with gimbal maintaining lock
3. **Surveillance**: Circular pattern while tracking vertically
4. **Return to home**: Autonomous return to launch point when battery low

## Key Features

### Mechanical Design
- **Precision machining**: CNC-fabricated components for repeatable assembly
- **Modular design**: Quick-swap camera and gimbal systems
- **Vibration damping**: Isolated sensor mounts for image stability
- **Lightweight structure**: Optimized for quadrotor weight budget

### Vision Capabilities
- **Real-time tracking**: Target detection and centroid calculation
- **Motion compensation**: Automatic gimbal adjustment for moving targets
- **Autonomous operation**: Minimal ground station intervention required
- **Multi-target support**: Ability to switch between targets

### Operational Specifications
| Specification | Value |
|---|---|
| **Flight time** | 15-25 minutes |
| **Max speed** | 12-15 m/s |
| **Altitude range** | 0-120m AGL |
| **Camera resolution** | 1080p @ 30fps |
| **Tracking accuracy** | ±5° in gimbal range |
| **Communication range** | 500m+ line-of-sight |

## Technical Challenges & Solutions

### Challenge 1: Gimbal Stability Under Motion
**Solution**: Gyroscopic stabilization with accelerometer feedback
- Real-time IMU data fusion
- PID control for smooth gimbal response
- Vibration isolation mounts

### Challenge 2: Real-time Vision Processing
**Solution**: Optimized OpenCV algorithms on embedded hardware
- Multi-threaded processing pipeline
- GPU acceleration where available
- Adaptive tracking thresholds

### Challenge 3: Flight Controller Integration
**Solution**: MAVLink protocol communication with autopilot
- Standardized communication interface
- Telemetry data logging
- Fail-safe Return-to-Home

## Project Documentation

Complete project details are available in:
- **Team Report PDF**: Comprehensive design documentation, test results, and performance analysis
- **Visual Assets**: CAD design files, assembly photos, and system demonstration video

See the gallery above for all documentation and visual materials.

## Conclusion

The POV system demonstrates the integration of mechanical design, embedded systems, and computer vision for autonomous surveillance applications. The modular architecture allows for adaptation to various missions, from research monitoring to industrial inspection.

**Key achievements:**
- ✅ Autonomous target tracking system fully operational
- ✅ Real-time gimbal stabilization with vision feedback
- ✅ Flight times exceeding design specifications
- ✅ Reliable autonomous operation in controlled environments

---

**For more information and system demonstration, see the project report and video in the gallery above.**
