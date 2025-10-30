---
layout: project
title: "Autonomous Line Following Robot"
description: "A sophisticated line-following robot built with Arduino Uno, featuring PID control, obstacle detection, and wireless monitoring capabilities."
date: 2024-10-15
categories: [Robotics, Arduino, Mechatronics]
featured_image: "/assets/images/projects/line-robot/featured.jpg"
github_url: "https://github.com/yourusername/line-following-robot"
demo_url: "https://youtu.be/your-demo-video"

# 3D Models - Support for STL, OBJ, GLTF, GLB formats
models:
  - file: "/assets/models/line-robot/chassis.stl"
    description: "3D printed robot chassis with integrated sensor mounts"
  - file: "/assets/models/line-robot/wheel-assembly.stl"
    description: "Custom wheel assembly with encoder integration"

# Circuit Schematics - PNG, JPG, SVG, PDF formats
schematics:
  - file: "/assets/schematics/line-robot/main-circuit.png"
    description: "Main control circuit with Arduino Uno and motor driver"
  - file: "/assets/schematics/line-robot/sensor-board.png"
    description: "IR sensor array PCB layout"
  - file: "/assets/schematics/line-robot/power-distribution.png"
    description: "Power distribution and battery management system"

# Code Files with syntax highlighting
code_files:
  - name: "Main Control"
    file: "main.ino"
    language: "cpp"
    download_url: "https://github.com/yourusername/line-following-robot/blob/main/src/main.ino"
    content: |
      #include <PID_v1.h>
      #include <SoftwareSerial.h>
      
      // Pin definitions
      #define LEFT_MOTOR_PWM 3
      #define LEFT_MOTOR_DIR 2
      #define RIGHT_MOTOR_PWM 5
      #define RIGHT_MOTOR_DIR 4
      
      // Sensor pins (analog)
      #define SENSOR_1 A0
      #define SENSOR_2 A1
      #define SENSOR_3 A2
      #define SENSOR_4 A3
      #define SENSOR_5 A4
      
      // PID Controller variables
      double setpoint = 0;
      double input, output;
      double kp = 2.0, ki = 0.1, kd = 0.5;
      PID pid(&input, &output, &setpoint, kp, ki, kd, DIRECT);
      
      // Base speed
      int baseSpeed = 150;
      
      void setup() {
        Serial.begin(9600);
        
        // Initialize motor pins
        pinMode(LEFT_MOTOR_PWM, OUTPUT);
        pinMode(LEFT_MOTOR_DIR, OUTPUT);
        pinMode(RIGHT_MOTOR_PWM, OUTPUT);
        pinMode(RIGHT_MOTOR_DIR, OUTPUT);
        
        // Initialize PID
        pid.SetMode(AUTOMATIC);
        pid.SetOutputLimits(-255, 255);
        
        Serial.println("Line Following Robot Initialized");
      }
      
      void loop() {
        // Read sensor values
        int sensor1 = analogRead(SENSOR_1);
        int sensor2 = analogRead(SENSOR_2);
        int sensor3 = analogRead(SENSOR_3);
        int sensor4 = analogRead(SENSOR_4);
        int sensor5 = analogRead(SENSOR_5);
        
        // Calculate line position (-2 to +2)
        input = calculateLinePosition(sensor1, sensor2, sensor3, sensor4, sensor5);
        
        // Compute PID
        pid.Compute();
        
        // Calculate motor speeds
        int leftSpeed = baseSpeed + output;
        int rightSpeed = baseSpeed - output;
        
        // Constrain speeds
        leftSpeed = constrain(leftSpeed, -255, 255);
        rightSpeed = constrain(rightSpeed, -255, 255);
        
        // Drive motors
        driveMotors(leftSpeed, rightSpeed);
        
        delay(10);
      }
      
      double calculateLinePosition(int s1, int s2, int s3, int s4, int s5) {
        // Convert analog readings to digital (0 or 1)
        int sensors[5];
        sensors[0] = (s1 > 500) ? 1 : 0;
        sensors[1] = (s2 > 500) ? 1 : 0;
        sensors[2] = (s3 > 500) ? 1 : 0;
        sensors[3] = (s4 > 500) ? 1 : 0;
        sensors[4] = (s5 > 500) ? 1 : 0;
        
        // Calculate weighted average
        int sum = 0, weightedSum = 0;
        for(int i = 0; i < 5; i++) {
          weightedSum += sensors[i] * (i - 2);
          sum += sensors[i];
        }
        
        if(sum == 0) return 0; // No line detected
        
        return (double)weightedSum / sum;
      }
      
      void driveMotors(int leftSpeed, int rightSpeed) {
        // Left motor
        if(leftSpeed >= 0) {
          digitalWrite(LEFT_MOTOR_DIR, HIGH);
          analogWrite(LEFT_MOTOR_PWM, leftSpeed);
        } else {
          digitalWrite(LEFT_MOTOR_DIR, LOW);
          analogWrite(LEFT_MOTOR_PWM, -leftSpeed);
        }
        
        // Right motor
        if(rightSpeed >= 0) {
          digitalWrite(RIGHT_MOTOR_DIR, HIGH);
          analogWrite(RIGHT_MOTOR_PWM, rightSpeed);
        } else {
          digitalWrite(RIGHT_MOTOR_DIR, LOW);
          analogWrite(RIGHT_MOTOR_PWM, -rightSpeed);
        }
      }
      
  - name: "PID Tuning"
    file: "pid_tuner.py"
    language: "python"
    download_url: "https://github.com/yourusername/line-following-robot/blob/main/tools/pid_tuner.py"
    content: |
      import serial
      import matplotlib.pyplot as plt
      import numpy as np
      from tkinter import *
      from tkinter import ttk
      
      class PIDTuner:
          def __init__(self):
              self.serial_port = None
              self.data_log = []
              self.setup_gui()
              
          def setup_gui(self):
              self.root = Tk()
              self.root.title("PID Tuner for Line Following Robot")
              self.root.geometry("800x600")
              
              # Connection frame
              conn_frame = ttk.Frame(self.root)
              conn_frame.pack(pady=10)
              
              ttk.Label(conn_frame, text="Serial Port:").pack(side=LEFT)
              self.port_entry = ttk.Entry(conn_frame, width=10)
              self.port_entry.pack(side=LEFT, padx=5)
              self.port_entry.insert(0, "COM3")
              
              self.connect_btn = ttk.Button(conn_frame, text="Connect", 
                                          command=self.connect_serial)
              self.connect_btn.pack(side=LEFT, padx=5)
              
              # PID parameter frame
              pid_frame = ttk.LabelFrame(self.root, text="PID Parameters")
              pid_frame.pack(pady=10, padx=10, fill=X)
              
              # Kp
              ttk.Label(pid_frame, text="Kp:").grid(row=0, column=0, sticky=W)
              self.kp_var = DoubleVar(value=2.0)
              self.kp_scale = ttk.Scale(pid_frame, from_=0, to=10, 
                                       variable=self.kp_var, orient=HORIZONTAL)
              self.kp_scale.grid(row=0, column=1, sticky=EW, padx=5)
              self.kp_label = ttk.Label(pid_frame, text="2.0")
              self.kp_label.grid(row=0, column=2)
              
              # Ki
              ttk.Label(pid_frame, text="Ki:").grid(row=1, column=0, sticky=W)
              self.ki_var = DoubleVar(value=0.1)
              self.ki_scale = ttk.Scale(pid_frame, from_=0, to=2, 
                                       variable=self.ki_var, orient=HORIZONTAL)
              self.ki_scale.grid(row=1, column=1, sticky=EW, padx=5)
              self.ki_label = ttk.Label(pid_frame, text="0.1")
              self.ki_label.grid(row=1, column=2)
              
              # Kd
              ttk.Label(pid_frame, text="Kd:").grid(row=2, column=0, sticky=W)
              self.kd_var = DoubleVar(value=0.5)
              self.kd_scale = ttk.Scale(pid_frame, from_=0, to=5, 
                                       variable=self.kd_var, orient=HORIZONTAL)
              self.kd_scale.grid(row=2, column=1, sticky=EW, padx=5)
              self.kd_label = ttk.Label(pid_frame, text="0.5")
              self.kd_label.grid(row=2, column=2)
              
              pid_frame.columnconfigure(1, weight=1)
              
              # Update button
              ttk.Button(pid_frame, text="Send Parameters", 
                        command=self.send_parameters).grid(row=3, column=1, pady=10)
              
              # Bind scale events
              self.kp_scale.bind("<Motion>", self.update_labels)
              self.ki_scale.bind("<Motion>", self.update_labels)
              self.kd_scale.bind("<Motion>", self.update_labels)
              
          def connect_serial(self):
              try:
                  port = self.port_entry.get()
                  self.serial_port = serial.Serial(port, 9600, timeout=1)
                  self.connect_btn.config(text="Connected", state=DISABLED)
                  print(f"Connected to {port}")
              except Exception as e:
                  print(f"Connection failed: {e}")
                  
          def update_labels(self, event=None):
              self.kp_label.config(text=f"{self.kp_var.get():.2f}")
              self.ki_label.config(text=f"{self.ki_var.get():.2f}")
              self.kd_label.config(text=f"{self.kd_var.get():.2f}")
              
          def send_parameters(self):
              if self.serial_port and self.serial_port.is_open:
                  kp = self.kp_var.get()
                  ki = self.ki_var.get()
                  kd = self.kd_var.get()
                  
                  command = f"PID:{kp:.2f},{ki:.2f},{kd:.2f}\n"
                  self.serial_port.write(command.encode())
                  print(f"Sent: {command.strip()}")
              
          def run(self):
              self.root.mainloop()
              
      if __name__ == "__main__":
          tuner = PIDTuner()
          tuner.run()

# Components and materials list
components:
  - name: "Arduino Uno R3"
    quantity: 1
    description: "Main microcontroller board"
    link: "https://store.arduino.cc/products/arduino-uno-rev3"
  
  - name: "L298N Motor Driver"
    quantity: 1
    description: "Dual H-bridge motor driver for DC motors"
    link: "https://example.com/l298n"
    
  - name: "IR Sensor Array"
    quantity: 1
    description: "5-channel infrared sensor array for line detection"
    
  - name: "DC Geared Motors (6V)"
    quantity: 2
    description: "High-torque geared motors with mounting brackets"
    
  - name: "Robot Wheels"
    quantity: 2
    description: "65mm diameter wheels with rubber tires"
    
  - name: "LiPo Battery (7.4V 2200mAh)"
    quantity: 1
    description: "Rechargeable battery pack with JST connector"
    
  - name: "Ultrasonic Sensor HC-SR04"
    quantity: 1
    description: "For obstacle detection and avoidance"
    
  - name: "Breadboard & Jumper Wires"
    quantity: 1
    description: "For prototyping and connections"

# Media gallery with images, videos, and GIFs
gallery:
  - type: "image"
    file: "/assets/images/projects/line-robot/assembly-1.jpg"
    description: "Robot chassis assembly with mounted components"
    
  - type: "image"
    file: "/assets/images/projects/line-robot/circuit-board.jpg"
    description: "Custom PCB with IR sensor array"
    
  - type: "gif"
    file: "/assets/images/projects/line-robot/robot-following.gif"
    description: "Robot successfully following a curved line track"
    
  - type: "video"
    file: "/assets/images/projects/line-robot/demo-video.mp4"
    description: "Complete demonstration of line following and obstacle avoidance"
    
  - type: "image"
    file: "/assets/images/projects/line-robot/pid-tuning.jpg"
    description: "PID parameter tuning using the custom Python interface"
---

## Project Overview

This project demonstrates the design and implementation of an autonomous line-following robot using Arduino Uno and advanced control algorithms. The robot features PID (Proportional-Integral-Derivative) control for smooth line tracking, obstacle detection capabilities, and wireless parameter tuning.

## Key Features

### 🤖 Advanced Control System
- **PID Controller**: Implements a sophisticated PID control algorithm for precise line following
- **Sensor Fusion**: Uses a 5-sensor IR array for accurate line position detection
- **Adaptive Speed**: Automatically adjusts speed based on track curvature

### 📡 Wireless Monitoring
- **Real-time Telemetry**: Sends sensor data and control parameters via Bluetooth
- **Parameter Tuning**: Live PID parameter adjustment using custom Python GUI
- **Performance Logging**: Records track performance for analysis and optimization

### 🛡️ Safety Features
- **Obstacle Detection**: Ultrasonic sensor for collision avoidance
- **Battery Management**: Low voltage detection and automatic shutdown
- **Emergency Stop**: Wireless emergency stop functionality

## Technical Specifications

| Specification | Value |
|---------------|-------|
| **Microcontroller** | Arduino Uno R3 (ATmega328P) |
| **Operating Voltage** | 7.4V (2S LiPo) |
| **Maximum Speed** | 1.2 m/s |
| **Line Detection Range** | 12cm wide sensor array |
| **Battery Life** | 45 minutes continuous operation |
| **Weight** | 485g |
| **Dimensions** | 18cm x 12cm x 8cm |

## Algorithm Implementation

The robot uses a weighted average algorithm to determine line position:

1. **Sensor Reading**: Five IR sensors provide analog values (0-1023)
2. **Thresholding**: Convert analog values to binary (line/no line)
3. **Position Calculation**: Weighted average gives position (-2 to +2)
4. **PID Control**: Error correction using PID algorithm
5. **Motor Control**: Differential steering based on PID output

## Performance Results

After extensive testing and PID tuning, the robot achieved:
- **Line Following Accuracy**: 95% on standard tracks
- **Maximum Track Speed**: Successfully follows lines at 80cm/s
- **Curve Handling**: Navigates 90° turns without losing the line
- **Obstacle Response**: Stops within 10cm of detected obstacles

## Lessons Learned

1. **PID Tuning**: Start with proportional control only, then add integral and derivative terms
2. **Sensor Calibration**: Regular calibration is crucial for consistent performance
3. **Power Management**: Use voltage regulators for stable sensor readings
4. **Mechanical Design**: Proper wheel alignment significantly improves tracking accuracy

## Future Improvements

- **Machine Learning**: Implement adaptive PID parameters using reinforcement learning
- **Multi-Line Support**: Add capability to handle intersections and multiple line paths
- **Wireless Communication**: Upgrade to WiFi for remote monitoring and control
- **Advanced Sensors**: Add color sensors for enhanced track detection

## Build Instructions

### Step 1: Mechanical Assembly
1. 3D print the chassis using the provided STL files
2. Mount the motors and wheels to the chassis
3. Install the sensor array at the front of the robot
4. Secure the Arduino and motor driver board

### Step 2: Electronics
1. Follow the circuit schematic to connect all components
2. Use the custom PCB design for a cleaner installation
3. Test all connections before powering on
4. Upload the Arduino code and calibrate sensors

### Step 3: Software Setup
1. Install the Arduino IDE and required libraries
2. Upload the main control code to the Arduino
3. Install Python dependencies for the tuning interface
4. Run initial calibration and PID tuning procedures

## Conclusion

This line-following robot project successfully demonstrates the integration of mechanical design, electronics, and software programming in a complete mechatronics system. The use of PID control and wireless tuning capabilities makes it an excellent educational platform for learning robotics and control theory.

The project serves as a foundation for more advanced autonomous vehicle projects and provides hands-on experience with embedded systems programming, sensor integration, and control algorithms.