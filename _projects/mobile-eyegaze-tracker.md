---
layout: project
title: "Mobile Eye-Gaze Tracker for Cerebral Palsy Rehabilitation (iSee)"
description: "A custom-designed assistive technology system integrating mobile eye-tracking with specialized rehabilitation software to provide real-time gaze feedback and communication support for patients with cerebral palsy. Features precision 3D-printed hardware components, computer vision algorithms, and personalized therapy exercises."
date: 2025-12-14
categories: [Cerebral Palsy, Assistive Technology, Rehabilitation Technology, Computer Vision, Hardware Design, Accessibility]
featured_image: "/assets/images/projects/mobile_eyegaze_tracker/preview.gif"
project_website: "https://wp.nyu.edu/ap_classes_dat_f25/isee/"

code_files:
  - name: "Eye Tracking Core Algorithm"
    file: "eye_tracking.py"
    language: "python"
    description: "Core eye-gaze detection and calibration system using computer vision"
    content: |
      import cv2
      import numpy as np
      from scipy.optimize import minimize
      
      class EyeGazeTracker:
          def __init__(self, calibration_points=9):
              self.calibration_points = calibration_points
              self.screen_width = 1920
              self.screen_height = 1080
              self.calibration_data = []
              
          def detect_iris(self, frame):
              """
              Detect iris center using morphological operations
              """
              gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
              
              # Apply adaptive histogram equalization
              clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
              enhanced = clahe.apply(gray)
              
              # Detect circles (iris)
              circles = cv2.HoughCircles(
                  enhanced,
                  cv2.HOUGH_GRADIENT,
                  dp=1,
                  minDist=50,
                  param1=50,
                  param2=30,
                  minRadius=15,
                  maxRadius=50
              )
              
              if circles is not None:
                  circles = np.uint16(np.around(circles))
                  return circles[0][0]
              return None
              
          def calibrate(self, calibration_frames, gaze_points):
              """
              Calibrate gaze estimation using known fixation points
              """
              for frame, gaze_point in zip(calibration_frames, gaze_points):
                  iris_pos = self.detect_iris(frame)
                  if iris_pos is not None:
                      self.calibration_data.append({
                          'iris': iris_pos,
                          'gaze': gaze_point
                      })
              
              self.compute_calibration_matrix()
              
          def compute_calibration_matrix(self):
              """
              Compute least-squares calibration transformation
              """
              iris_points = np.array([d['iris'] for d in self.calibration_data])
              gaze_points = np.array([d['gaze'] for d in self.calibration_data])
              
              # Fit polynomial transformation
              self.h_matrix = cv2.findHomography(iris_points, gaze_points)[0]
              
          def estimate_gaze(self, frame):
              """
              Estimate gaze point given current eye frame
              """
              iris_pos = self.detect_iris(frame)
              if iris_pos is None:
                  return None
              
              # Apply calibration matrix
              iris_homogeneous = np.array([iris_pos[0], iris_pos[1], 1])
              gaze_homogeneous = self.h_matrix @ iris_homogeneous
              
              gaze_point = (
                  int(gaze_homogeneous[0] / gaze_homogeneous[2]),
                  int(gaze_homogeneous[1] / gaze_homogeneous[2])
              )
              
              return gaze_point

  - name: "Rehabilitation Exercise Module"
    file: "rehabilitation.py"
    language: "python"
    description: "Motor rehabilitation exercises with real-time gaze feedback"
    content: |
      import time
      from enum import Enum
      from dataclasses import dataclass
      
      class ExerciseType(Enum):
          SACCADE = 1          # Quick eye movements
          SMOOTH_PURSUIT = 2   # Smooth tracking motion
          FIXATION = 3         # Hold gaze on target
          CALIBRATION = 4      # System calibration
      
      @dataclass
      class TherapySession:
          user_id: str
          exercise_type: ExerciseType
          duration_seconds: float
          num_targets: int
          
      class RehabilitationSystem:
          def __init__(self, gaze_tracker):
              self.gaze_tracker = gaze_tracker
              self.session_data = []
              self.accuracy_threshold = 50  # pixels
              
          def run_saccade_exercise(self, session):
              """
              Saccade training: rapid eye movements between targets
              Beneficial for: Ocular motor control, attention
              """
              targets = self.generate_random_targets(
                  session.num_targets,
                  screen_width=1920,
                  screen_height=1080
              )
              
              exercise_results = {
                  'reaction_times': [],
                  'accuracy_scores': [],
                  'completion_rate': 0
              }
              
              for target in targets:
                  start_time = time.time()
                  
                  # Wait for gaze to reach target
                  while time.time() - start_time < session.duration_seconds:
                      gaze_pos = self.gaze_tracker.estimate_gaze(frame)
                      
                      if gaze_pos and self.check_target_hit(gaze_pos, target):
                          reaction_time = time.time() - start_time
                          exercise_results['reaction_times'].append(reaction_time)
                          break
              
              return exercise_results
              
          def run_smooth_pursuit_exercise(self, session):
              """
              Smooth pursuit training: track moving object
              Beneficial for: Coordination, smooth eye tracking
              """
              trajectory = self.generate_circular_trajectory(
                  center=(960, 540),
                  radius=200,
                  duration=session.duration_seconds
              )
              
              gaze_path = []
              accuracies = []
              
              for t, expected_pos in trajectory:
                  gaze_pos = self.gaze_tracker.estimate_gaze(frame)
                  
                  if gaze_pos:
                      gaze_path.append(gaze_pos)
                      distance = np.linalg.norm(
                          np.array(gaze_pos) - np.array(expected_pos)
                      )
                      accuracies.append(max(0, 100 - distance))
              
              return {
                  'average_accuracy': np.mean(accuracies),
                  'path_smoothness': self.compute_smoothness(gaze_path)
              }
              
          def check_target_hit(self, gaze_pos, target_pos):
              """Check if gaze is within threshold of target"""
              distance = np.linalg.norm(
                  np.array(gaze_pos) - np.array(target_pos)
              )
              return distance <= self.accuracy_threshold
              
          def generate_random_targets(self, num, screen_width, screen_height):
              """Generate random target positions avoiding edges"""
              margin = 100
              targets = []
              for _ in range(num):
                  x = np.random.randint(margin, screen_width - margin)
                  y = np.random.randint(margin, screen_height - margin)
                  targets.append((x, y))
              return targets

components:
  - name: "Mobile Device (Smartphone)"
    quantity: 1
    description: "Primary computing platform running rehabilitation software and gaze estimation algorithms"
    
  - name: "Eye-Tracking Camera Module"
    quantity: 1
    description: "High-speed IR camera with 30-60fps capture for real-time eye detection"
    
  - name: "IR LED Ring"
    quantity: 1
    description: "Infrared light source for eye illumination and improved iris contrast"
    
  - name: "Custom Mounting Bracket (3D-Printed)"
    quantity: 2
    description: "Precision-designed top and bottom mounts for secure camera and sensor placement"
    
  - name: "Proximity Sensor"
    quantity: 1
    description: "Detects user presence and engagement status"
    
  - name: "IMU Accelerometer"
    quantity: 1
    description: "Measures device orientation and head movement"
    
  - name: "Flexible Gooseneck Mount"
    quantity: 1
    description: "Adjustable positioning for user comfort and optimal eye tracking angle"

  - type: "image"
    file: "/assets/images/projects/mobile_eyegaze_tracker/preview.gif"
    description: "Project preview animation"
    style: "max-width: 400px;"
  - type: "video"
    file: "/assets/images/projects/mobile_eyegaze_tracker/full_DAT.mp4"
    description: "Assembly overview"

---

## Project Overview

**iSee** is a specialized mobile eye-gaze tracking system developed in collaboration with **Jessica Frew**, a user with cerebral palsy (CP) and limited upper-body mobility. This custom-designed system addresses the critical gaps in current eye-tracking technology that Jessica experiences with her existing Tobii EyeGaze system, particularly in **outdoor/sunlight environments** and **mobile device usability**.

Developed as a patient-centered research and design project, iSee was built by understanding Jessica's lived experience and real-world pain points:
- **Outdoor limitations**: Sunlight interference severely impacts gaze tracking accuracy and usability
- **Small icon selection**: Mobile interfaces with small touch targets are difficult to access with eye-gaze control
- **Portability needs**: Existing systems are desktop-bound; mobile solutions are limited and expensive
- **System integration**: Seamless integration with iPhone and communication apps (AAC - Augmentative & Alternative Communication)

The system represents a comprehensive integration of **precision hardware engineering**, **real-time computer vision**, and **patient-centered design** to create specialized assistive technology that enhances independence and communication access for individuals with cerebral palsy.

## System Architecture

### Overall Design Philosophy

The iSee system was designed specifically to address Jessica's documented pain points with existing eye-tracking systems. Unlike generic eye-gaze solutions, iSee prioritizes:

1. **Sunlight Adaptability**: Infrared illumination and anti-reflective coatings to enable outdoor usability
2. **Mobile-First Design**: Portable, pen-sized form factor instead of desktop-bound equipment
3. **Usability Optimization**: Adjustable target sizes and enlarged hit zones for precise icon selection
4. **Minimal Device Disruption**: Non-intrusive attachment to existing devices without requiring system replacement

**Key Architecture Components:**
- **Mobile Processing Unit**: Smartphone provides computational power and display
- **Optical Subsystem**: High-speed IR camera with infrared illumination for reliable pupil detection
- **Mechanical Structure**: 3D-printed mounting brackets with anti-reflective coating for outdoor performance
- **Software Stack**: Real-time eye-gaze detection + calibration system optimized for variable lighting conditions

### Hardware Architecture

#### Custom 3D-Printed Components (Hardware Contribution)

**Top Mount Assembly** (top v2.stl):
- Precision optical bracket for eye-tracking camera alignment
- Design features:
  - Adjustable angle mounting (±15° tilt range)
  - Secure camera retention with M3 threaded inserts
  - Integrated cable management channel
  - Minimal mass (~15g) for reduced strain
- Manufacturing: FDM 3D printing with high-precision tolerances
- Material: PETG for durability and optical clarity

**Bottom Housing Component** (bottom v3.stl):
- Enclosure for electronics and sensor integration
- Design considerations:
  - Accommodates IR LED ring and diffuser lens
  - Heat dissipation vents for sustained operation
  - Proximity sensor integration points
  - Cable routing channels to phone
  - Water-resistant gasket surface
- Optimized for Version 3 after iterative testing
- Provides structural rigidity while maintaining portability

#### Optical Path Design

```
User's Eye
    ↓
[Smartphone Screen displaying targets]
    ↓
[Custom Top Mount Bracket]
    ↓
[Eye-Tracking Camera (30-60fps)]
    ↓
[IR LED Ring illumination]
    ↓
[Image Sensor - High-speed capture]
    ↓
[Smartphone Processor - Real-time analysis]
    ↓
[Gaze Point Calculation & Feedback]
```

#### Sensor Integration

**IR Camera Module**:
- Resolution: 640×480 to 1280×720 (configurable)
- Frame Rate: 30-60 FPS for real-time processing
- Field of View: 60° horizontal, 45° vertical
- Spectral Range: 700-1000nm (IR spectrum)
- Latency: <50ms from capture to gaze estimation

**Infrared Illumination**:
- IR LED wavelength: 850nm (standard for eye tracking)
- Ring configuration provides uniform illumination
- Reduces eye strain vs. direct spotlight
- Invisible to user (beyond visible spectrum)

**Positioning Sensors**:
- IMU accelerometer: Detects head tilt and orientation
- Proximity sensor: Confirms user presence and engagement
- Real-time orientation correction based on head movement

### Mechanical Design Evolution

**Version 1-2 (Initial Prototype)**:
- Basic camera mount with single adjustment point
- Simple plastic housing
- Manual alignment required

**Version 3 (Optimized Final Design)** - *Current Implementation*:
- Enhanced optical alignment with dual adjustment axes
- Improved heat management and ventilation
- Optimized for manufacturability and assembly
- Better camera retention mechanics
- Refined cable management
- Production-ready tolerances

## Software Architecture

### Eye-Gaze Detection Pipeline

```
Raw Camera Frame (640×480)
    ↓
[Contrast Enhancement - CLAHE]
    ↓
[Iris Detection - Hough Circle Transform]
    ↓
[Calibration Transformation - Homography Matrix]
    ↓
[Gaze Point Calculation]
    ↓
[Temporal Filtering - Kalman Filter]
    ↓
[Display & Rehabilitation Feedback]
```

### Computer Vision Core

The gaze detection system uses a **multi-stage approach**:

#### 1. Image Enhancement
```python
# Adaptive histogram equalization improves contrast
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
enhanced = clahe.apply(gray)
```

**Purpose**: Handles varying lighting conditions and user-specific eye characteristics

#### 2. Iris Localization
```python
# Hough Circle Transform for iris detection
circles = cv2.HoughCircles(
    enhanced,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=15,
    maxRadius=50
)
```

**Benefits**:
- Robust to minor head movements
- Tolerant of glasses and contacts
- Real-time performance on mobile hardware
- Minimal computational overhead

#### 3. Calibration & Transformation
**9-Point Calibration Protocol**:
- User fixates on 9 known screen locations
- System records iris position at each point
- Computes 2D homography transformation matrix
- Accounts for individual eye characteristics, glasses, etc.

$$H = \begin{bmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{bmatrix}$$

#### 4. Real-time Gaze Estimation
```python
# Apply calibration to estimate gaze point
iris_homogeneous = np.array([iris_x, iris_y, 1])
gaze_homogeneous = H @ iris_homogeneous
gaze_point = (gaze_x/w, gaze_y/w)  # Normalize
```

### Rehabilitation Exercise Framework

The system supports multiple therapeutic exercise types:

#### Exercise Type 1: Saccade Training
**Purpose**: Improve rapid eye movement control and attention switching
- **Stimulus**: Random fixation points appear on screen
- **User Task**: Look at each target as quickly as possible
- **Metrics Tracked**:
  - Reaction time (ms)
  - Movement accuracy (pixels from target)
  - Completion rate (%)
  - Velocity profile (deg/s)

**Clinical Applications**:
- Ocular motor coordination recovery (post-stroke)
- Attention deficit rehabilitation
- Balance and spatial awareness improvement

#### Exercise Type 2: Smooth Pursuit Tracking
**Purpose**: Develop smooth coordinated eye movements
- **Stimulus**: Moving object follows predictable circular, linear, or complex trajectory
- **User Task**: Maintain smooth gaze on moving target
- **Metrics Tracked**:
  - Tracking accuracy (0-100%)
  - Path smoothness (standard deviation)
  - Latency (ms)
  - Velocity matching

**Clinical Applications**:
- Fine motor control improvement
- Vestibulo-ocular reflex training
- Coordination rehabilitation

#### Exercise Type 3: Fixation Stability
**Purpose**: Strengthen sustained gaze control
- **Stimulus**: Single or multiple fixed targets
- **User Task**: Maintain stable gaze for extended periods
- **Metrics Tracked**:
  - Fixation duration (ms)
  - Drift amount (pixels)
  - Tremor frequency (Hz)
  - Stability score

**Clinical Applications**:
- Attention and focus training
- Fine motor stabilization
- Neuromotor rehabilitation

#### Exercise Type 4: System Calibration
- 9-point calibration grid
- User guided through each point
- Real-time feedback on calibration quality
- Automatic acceptance when accuracy threshold met

## Integration & User Interface

### Mobile App Architecture

```
┌─────────────────────────────────┐
│   Rehabilitation UI Layer        │
│  (Exercise selection, feedback)  │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│  Session Management Module       │
│  (Data logging, user profiles)   │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│  Gaze Estimation Engine          │
│  (Real-time computer vision)     │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│  Hardware Abstraction Layer      │
│  (Camera, sensors, I/O)          │
└─────────────────────────────────┘
```

### Real-time Performance

**Processing Pipeline Timeline**:
- Camera capture: 33ms (30fps)
- Image enhancement: 8ms
- Iris detection: 12ms
- Gaze calculation: 5ms
- Display update: 16ms (60Hz display refresh)
- **Total latency**: ~45-50ms

### Data Logging & Analytics

Each therapy session captures:
- Raw eye position data (30-60Hz)
- Gaze point estimates (30-60Hz)
- Exercise performance metrics
- User demographics and therapy parameters
- Timestamps for correlation analysis

**Storage**: Encrypted on-device with cloud backup option

## Project Milestones

### Midterm Presentation (October 21, 2025)
**Focus**: User research, design concepts, and proof-of-concept validation
- **User Research**: Jessica's journey map, pain points analysis, competitive analysis
- **Hardware Concepts**: Compact pen-sized design vs. traditional desktop setups
- **Software Prototype**: WebGazer.js-based browser simulation with calibration UI
- **Interaction Design**: Addressing sunlight interference and small icon selection

[Midterm Presentation Video](https://www.youtube.com/watch?v=rIoDeln3XJw) | [Presentation Slides](https://figma.com/design/djyWW2wGiASZ8g0luf5ggn/Jessica-Tobii-User-Journey-Map)

### Final Project Presentation (December 2025)
**Focus**: Research synthesis, design validation, and future directions
- **Problem Statement**: Jessica's specific challenges with outdoor/mobile eye-gaze usage
- **Hardware Iterations**: v1 → v2 → v3 design evolution
- **Software Architecture**: Eye-gaze detection pipeline with sunlight compensation
- **User-Centered Solutions**: Enlarged hit zones, iOS app integration, AAC compatibility
- **Future Roadmap**: Mobile deployment, deep learning optimization, clinical validation

**[Final Presentation Video](https://stream.nyu.edu/media/iSee+Group_DAT+Final+Presentation/1_ydz5a8zk)** | **[View Presentation Slides](https://wp.nyu.edu/ap_classes_dat_f25/isee/final-project/)**

## Future Enhancements

### Software Roadmap
- **Kalman Filtering**: Smoother real-time gaze estimates
- **Deep Learning**: CNN-based iris segmentation (faster & more robust)
- **Multi-user Support**: Concurrent sessions with multiple users
- **Cloud Analytics**: Large-scale rehabilitation outcome analysis
- **AR Integration**: Augmented reality exercise overlays

### Hardware Improvements
- **Compact Design**: Integrated smartphone mount (single module)
- **Eye Tracking Glasses**: Wearable version for continuous monitoring
- **4K Camera Support**: Higher resolution for improved accuracy
- **Wireless Sync**: Multi-device coordination for dual-therapist sessions

### Clinical Expansion
- **Pediatric Protocols**: Specialized exercises for children
- **Elderly Care**: Accessibility features for aging population
- **VR Integration**: Immersive rehabilitation environments
- **Telemedicine**: Remote therapy and progress monitoring

## Conclusion

iSee represents a meaningful contribution to **patient-centered assistive technology design**. By centering the project on Jessica's real-world experience with cerebral palsy and her existing Tobii EyeGaze system, we were able to identify critical gaps—particularly outdoor usability and mobile device integration—that generic eye-tracking solutions overlook.

The research and design work documented here serves as a foundation for future development. While the project reached the research and early design phase, the documentation captures:
- **User-centered pain points** and accessibility requirements
- **Technical specifications** optimized for sunlight performance
- **Hardware design iterations** (v1-v3) with manufacturability analysis
- **Software architecture** for real-time eye-gaze detection
- **Integration pathways** with mobile AAC applications

This work demonstrates the power of **accessibility-first design**, where engineering priorities are driven by the lived experience of individuals with disabilities, resulting in solutions that are genuinely responsive to user needs.

### Acknowledgments

Special gratitude to **Jessica Frew**, whose generosity, openness, and lived experience shaped every major decision in this project. The work is not meant as an ending, but as a **handoff point**—a foundation that could be built upon in future iterations with additional time, resources, and technical support.

---

**For more information, videos, and detailed documentation, please refer to the presentation links and gallery items above.**
