---
layout: project
title: "3-RPS Gantry System"
description: "A three revolute-prismatic-spherical parallel manipulator gantry system with real-time control, IMU integration, and servo-driven actuation."
date: 2024-12-15
categories: [Robotics, Parallel Kinematics, Embedded Systems, Propeller-based Control]
featured_image: "/assets/images/projects/3rps_gantry/preview.png"
github_url: "https://github.com/josephineoe"
demo_url: "#"

code_files:
  - name: "Main Control System"
    file: "3RPS.c"
    language: "c"
    description: "Multi-cog control system with parallel servo and input handling"
    content: |
      #include "simpletools.h"
      #include "adcDCpropab.h"
      #include "imu_sensor.h"
      
      // Pin Definitions
      #define RPS_LEG1_PIN 12
      #define RPS_LEG2_PIN 13
      #define RPS_LEG3_PIN 14
      #define GANTRY_PIN1 15
      #define GANTRY_PIN2 16

  - name: "IMU Sensor Interface (Header)"
    file: "imu_sensor.h"
    language: "c"
    description: "Custom header file for MPU-6050 IMU sensor integration"
    content: |
      #ifndef IMU_SENSOR_H
      #define IMU_SENSOR_H
      
      #define MPU6050_ADDR 0x68
      #define PWR_MGMT_1     0x6B
      #define GYRO_CONFIG    0x1B
      #define ACCEL_CONFIG   0x1C
      
      typedef struct {
          int16_t accel[3];
          int16_t gyro[3];
          int16_t temp;
      } imu_data_t;
      
      void mpu6050_init();
      void mpu6050_read(imu_data_t *data);
      void calibrate_gyro(volatile int samples, volatile int16_t *offsets);
      void current_pos();
      
      #endif

  - name: "IMU Sensor Implementation"
    file: "imu_sensor.c"
    language: "c"
    description: "Complete MPU-6050 implementation with I2C communication"

components:
  - name: "Propeller Microcontroller"
    quantity: 1
    description: "8-core processor for real-time multi-tasking control"
    
  - name: "Servo Motors"
    quantity: 4
    description: "Three RPS leg actuators plus one gantry motor for XY positioning"
    
  - name: "MPU-6050 IMU"
    quantity: 1
    description: "6-axis inertial measurement unit (3-axis gyroscope + 3-axis accelerometer) for roll/pitch tracking"
    
  - name: "Analog Joystick Controller"
    quantity: 1
    description: "3-axis input for platform control (forward/backward, up/down, rotation)"
    
  - name: "ADC Module"
    quantity: 1
    description: "Analog-to-digital converter for joystick signal reading"

gallery:
  - type: "image"
    file: "/assets/images/projects/3rps_gantry/full_system.jpg"
    description: "Complete 3-RPS gantry system overview"
  - type: "image"
    file: "/assets/images/projects/3rps_gantry/preview.png"
    description: "System preview and configuration"
  - type: "video"
    file: "/assets/images/projects/3rps_gantry/prototype.mp4"
    description: "Prototype demonstration"
  - type: "video"
    file: "/assets/images/projects/3rps_gantry/test.mp4"
    description: "System testing and validation"
  - type: "video"
    file: "/assets/images/projects/3rps_gantry/test2.mp4"
    description: "Advanced motion testing"
  - type: "document"
    file: "/assets/images/projects/3rps_gantry/Project 2 Proposal.pdf"
    description: "Project proposal and initial specifications"
  - type: "document"
    file: "/assets/images/projects/3rps_gantry/Project 2 Report-commented.pdf"
    description: "Comprehensive project report with design analysis"
---

## Project Overview

The 3-RPS (Revolute-Prismatic-Spherical) gantry system is an advanced parallel manipulator designed for precise three-degree-of-freedom positioning (X-Y translation with rotation). This project demonstrates a real-time embedded control system with IMU integration, multi-cog architecture, and joystick-based human input handling on the Propeller microcontroller platform.

## System Architecture

### Mechanical Configuration
The system utilizes three independently actuated RPS kinematic chains arranged in a 120° pattern around the base. Each chain consists of:
- **Revolute Joint**: Base rotation axis
- **Prismatic Joint**: Servo-controlled linear extension
- **Spherical Joint**: Platform attachment point allowing 3DOF orientation

This parallel architecture provides:
- High structural stiffness with distributed load paths
- Synchronized three-point support for platform stability
- Full 3DOF platform control (X, Y, rotation)

### Key Components

#### Propeller Microcontroller
- **8 Independent Cores (Cogs)**: Enables true parallel processing
- **Real-time Control**: 100MHz operation without OS overhead
- **Pin-out**: 32 I/O pins for servo and sensor interfacing

#### Motor Control
- **RPS Leg Actuators**: Three servo motors (Pins 12, 13, 14)
  - 1400 microseconds: Fully retracted (down)
  - 1500 microseconds: Neutral position
  - 1600 microseconds: Extended (up)
  
- **Gantry Motors**: Linear actuation (Pin 15)
  - 1400 microseconds: Left movement
  - 1475 microseconds: Neutral/stop
  - 1600 microseconds: Right movement

#### Sensing System
**IMU Sensor (MPU-6050)** integrated via I2C interface:
- **Accelerometer**: ±2g range with 16384 LSB/g sensitivity
- **Gyroscope**: ±250°/s range with 131 LSB/°/s sensitivity
- **Temperature Sensor**: Onboard thermal monitoring
- **Real-time Orientation**: Roll and pitch calculation from sensor fusion

**Analog Joystick Controller**:
- 3-axis analog input via ADC (Pins 18-21)
- Threshold-based control mapping:
  - Upper threshold (>3.0V): Forward/up/rotation positive
  - Lower threshold (<2.0V): Backward/down/rotation negative
  - Dead zone (2.0-3.0V): No command

## Software Architecture

### Multi-Cog Design Pattern

The control system uses Propeller's unique multi-cog architecture for true parallel execution:

```
Main Cog (cog0):
├─ System initialization
├─ IMU calibration
└─ Monitoring loop (500ms cycle)

Servo Control Cogs (cog1, cog2, cog3):
├─ RPS Leg 1 PWM generation
├─ RPS Leg 2 PWM generation
└─ RPS Leg 3 PWM generation

Gantry Control Cog (cog4):
└─ Platform XY actuation

Input Processing Cog (cog5):
├─ ADC sampling (joystick)
├─ Threshold logic processing
└─ Command state management
```

### Control Flow

#### 1. Initialization Phase
```c
mpu6050_init()      // Initialize I2C and IMU registers
cogstart(...)       // Launch servo control cogs
cogstart(...)       // Launch input processing cog
calibrate_gyro()    // Collect 1000+ samples for offset determination
```

#### 2. Real-time Operation
- **Servo Cogs**: Continuous PWM pulse generation (20ms cycle)
- **Input Cog**: 50ms ADC sampling interval
- **Main Loop**: 500ms monitoring/telemetry output

#### 3. Command Processing
Joystick input → ADC Conversion → Threshold Logic → Servo Command

## Implementation Details

### Custom IMU Header File (imu_sensor.h)

This custom header provides the interface for the MPU-6050 sensor:

```c
/**
 * @file include/imu_sensor.h
 * @brief Provides IMU 6050 specific functions
 * Copyright (c) 2025 by Josephine Odusanya
 */

#define MPU6050_ADDR 0x68    // I2C slave address
#define PWR_MGMT_1   0x6B    // Power management register
#define GYRO_CONFIG  0x1B    // Gyroscope configuration
#define ACCEL_CONFIG 0x1C    // Accelerometer configuration

// Data structure for all 6 sensor axes + temperature
typedef struct {
    int16_t accel[3];  // X, Y, Z acceleration
    int16_t gyro[3];   // X, Y, Z angular velocity
    int16_t temp;      // Temperature reading
} imu_data_t;
```

**Key Functions**:
- `mpu6050_init()`: Configures sensor ranges and enables I2C communication
- `mpu6050_read()`: Reads all 14 bytes of sensor data
- `calibrate_gyro()`: Averages stationary gyroscope readings for offset correction
- `current_pos()`: Computes roll and pitch using complementary angle formulas

### Main Control Program (3RPS.c)

The main program orchestrates multi-cog execution with volatile flag-based communication:

```c
// Control state flags (volatile for inter-cog communication)
static volatile int forward = 0, backward = 0;
static volatile int up = 0, down = 0;
static volatile int xR = 0;  // Rotation command

// Voltage readings from joystick
static volatile float lrV, udV, xrV;

// Configuration
#define RPS_LEG1_PIN 12     // Leg 1 servo PWM
#define RPS_LEG2_PIN 13     // Leg 2 servo PWM
#define RPS_LEG3_PIN 14     // Leg 3 servo PWM
#define GANTRY_PIN1 15      // Gantry motor PWM
```

**Servo Control Cog Example** (rps_cog1):
```c
void rps_cog1(void *par1) {
    while(1) {
        if(down == 1)
            pulse_out(RPS_LEG1_PIN, 1600);  // Extend leg (up)
        else if(up == 1)
            pulse_out(RPS_LEG1_PIN, 1400);  // Retract leg (down)
        else if(xR == 1)
            pulse_out(RPS_LEG1_PIN, 1400);  // Rotation CCW
        else if(xR == -1)
            pulse_out(RPS_LEG1_PIN, 1600);  // Rotation CW
        else
            pulse_out(RPS_LEG1_PIN, 1500);  // Hold position
        
        pause(20);  // ~50Hz control rate
    }
}
```

**Input Processing Cog** (input_cog):
```c
void input_cog(void *par6) {
    adc_init(21, 20, 19, 18);  // Initialize 4-line SPI ADC
    
    while(1) {
        udV = adc_volts(1);     // Up/Down channel
        lrV = adc_volts(0);     // Left/Right channel
        xrV = adc_volts(2);     // Rotation channel
        
        // Threshold-based command generation
        if(lrV > 3.0) {
            forward = 1;
            backward = 0;
        } else if(lrV < 2.0) {
            backward = 1;
            forward = 0;
        } else {
            forward = 0;
            backward = 0;
        }
        
        // Similar logic for up/down and rotation...
    }
}
```

## Motion Characteristics

### Timing Specifications
- **Total Motion Duration**: ~17.9 seconds for full-range movement
- **Total Distance**: 0.095 meters (95mm platform travel)
- **Maximum Speed**: 1.7 pulses per millisecond (50 Hz control rate)

### Servo Pulse Mapping
| Command | Pulse Width | Effect |
|---------|-------------|--------|
| 1400 µs | Down/Retract | Minimum leg extension |
| 1475 µs | Stop | Neutral holding position |
| 1500 µs | Hold | Default static position |
| 1600 µs | Up/Extend | Maximum leg extension |

## IMU Sensor Integration

### I2C Communication Protocol
- **Address**: 0x68 (standard MPU-6050)
- **Pin 8**: SCL (Clock)
- **Pin 9**: SDA (Data)
- **Frequency**: Standard I2C rates

### Sensor Calibration
```c
void calibrate_gyro(volatile int samples, volatile int16_t *offsets) {
    int32_t sum[3] = {0};
    
    for(int i = 0; i < samples; i++) {
        mpu6050_read(&data);
        sum[0] += data.gyro[0];  // Sum X-axis gyro
        sum[1] += data.gyro[1];  // Sum Y-axis gyro
        sum[2] += data.gyro[2];  // Sum Z-axis gyro
        pause(10);
    }
    
    // Store average offsets for drift compensation
    offsets[0] = sum[0] / samples;
    offsets[1] = sum[1] / samples;
    offsets[2] = sum[2] / samples;
}
```

### Roll and Pitch Computation
Using accelerometer data with calibrated gyroscope:

$$\text{Roll} = \arctan2(a_y, a_z) \times \frac{180}{\pi}$$

$$\text{Pitch} = \arctan2(-a_x, \sqrt{a_y^2 + a_z^2}) \times \frac{180}{\pi}$$

Where $a_x, a_y, a_z$ are accelerometer readings converted from 16384 LSB/g format.

## Project Development

### Design Goals Achieved
- ✅ Three-degree-of-freedom parallel kinematics
- ✅ Real-time multi-core embedded control
- ✅ IMU-based orientation sensing
- ✅ Joystick human interface with analog input
- ✅ Synchronized three-leg actuation
- ✅ Extensible cog-based architecture

### Technical Challenges Addressed
1. **Synchronization**: Using volatile flags for safe inter-cog communication
2. **I2C Timing**: Custom I2C routines for reliable MPU-6050 communication
3. **Real-time Response**: Deterministic servo control at 50Hz
4. **Sensor Calibration**: Gyroscope offset collection during initialization
5. **Digital Filter Design**: Optional DLPF configuration for noise reduction (commented in code for future implementation)

## Future Enhancements

### Software Improvements
- Kalman filter fusion of accelerometer and gyroscope data
- PID-based closed-loop position control
- Trajectory planning and waypoint following
- SD card logging of sensor and command data

### Hardware Upgrades
- Force sensors for load monitoring
- Additional IMUs for real-time platform orientation feedback
- Higher-resolution servo motors with feedback encoders
- Wireless communication for remote control

### Extended Capabilities
- 4-DOF platform with tilting capability
- Multiple synchronized end-effectors
- Machine vision integration for autonomous positioning
- Mobile base integration for extended workspace

## Documentation

Complete technical specifications and design analysis are available in the included documentation:
- **Project Proposal PDF**: Initial specifications and design approach
- **Project Report PDF**: Detailed analysis, testing results, and implementation insights

For detailed specifications and technical information, refer to the included project proposal and report PDFs in the gallery above.
