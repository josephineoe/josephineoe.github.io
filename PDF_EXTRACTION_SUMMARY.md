# PDF Extraction: Structured Summary for Markdown Documentation

## PROJECT 1: PERSISTENCE OF VISION (POV) EDUCATIONAL KIT

### Project Title and Objective
- **Full Title:** Mechatronics Project Report - Persistence of Vision Educational Kit with Basic Stamp 2
- **Core Objective:** Design a mechatronics-enabled pre-college level science experiment that teaches concepts of memory-efficient programming, gearing, mechanical structures, and visual perception through a practical Persistence of Vision (POV) display system
- **Educational Goal:** Create an alternative to existing expensive robot kits (like Parallax BoeBot and Arduino Science Kit) that is fun, unique, and inexpensive while teaching signal modelling through both mechanical and optical outputs

### Key Concept
Persistence of Vision (POV) is an optical phenomenon where the human eye perceives a visual image for longer than its actual duration. By rapidly moving LEDs in specific patterns, the display creates the illusion of a stable image or text. The kit exploits the fact that the human eye can only process 10-12 separate images per second, retaining an image for up to 1/15th of a second.

### Team Members
- **Vedvyas Danturi** (vsd2027)
- **Josephine Odusanya** (joo9964)
- **Sven Sunny Kottuppallil** (ssk10038)

### Key System Components and Specifications

#### Stage I Implementation
**Hardware Components:**
- Basic Stamp 2 (BS2) Microcontroller - Primary system controller
- DC Motor (16k RPM) - Drives LED array rotation (reduced to ~4k RPM via 4:1 gearing)
- Hall Effect Sensor - Detects magnet position for synchronization
- Digital Potentiometer - Manual control of LED brightness
- 6 RGB LEDs - Core visual components
- Ambient Light Sensor (Photodiode) - Measures ambient light for brightness adjustment
- Magnet - Works with Hall effect sensor for positional feedback
- Slip Ring - Enables continuous electrical connection to rotating LED array
- 3D Printed Motor Mount - Holds motor securely

**Operational Parameters:**
- Rotation Speed: ≤1800 RPM (or ~30 rotations per second for smooth illusion)
- LED Pattern Synchronization: Real-time adjustment based on motor speed
- Programming Language: PBASIC
- Control Method: Proportional feedback control algorithm

#### Stage II Implementation (Advanced/Scalable)
**Hardware Components:**
- Basic Stamp 2 (BS2) - Maintains user interface and actuator control
- DC Motor - Same as Stage I
- Hall Effect Sensor - Synchronization (enhanced with 3 magnets)
- Adafruit NeoPixel Ring - 24 individually addressable RGB LEDs (vs 6 in Stage I)
- Ambient Light Sensor - Enhanced capability
- Teensy 4.1 Microcontroller - Acts as dedicated LED driver for NeoPixel Ring
- ADC (Analog-to-Digital Converter) - Converts analog signals from photodiode
- 555 Timer - Timing signal generation or PWM control
- WS2812B SMD Addressable RGB LEDs - Within NeoPixel Ring
- Slip Ring - High-speed rated
- 3D Printed Motor Mount - Enhanced design

**Key Component Details:**
- **WS2812B LED Challenge:** Requires precise microsecond-level timing; BS2 limitations required workaround using Teensy 4.1
- **Teensy Integration:** Used purely as LED driver; BS2 maintains overall control
- **NeoPixel Ring:** Provides 4x resolution improvement for more detailed patterns

### Technical Approach and Methodology

#### Design Philosophy
The project demonstrates scalability in two stages:
1. **Stage I:** Foundational approach with individual LED control
2. **Stage II:** Advanced implementation showing how to overcome hardware limitations through intelligent component selection

#### Control Architecture
**Mathematical Background:**
- POV Frequency: 10 Hz minimum (1/10 second retention) for basic effect
- Smooth Illusion: 30 Hz equivalent (30 rotations per second = 1800 RPM single-side, 900 RPM for ring)
- Flicker Fusion Threshold: Rapid flickering simulates constant illumination while reducing power consumption

**Proportional Control Algorithm:**
- Error Signal: e(t) = r(t) - y(t) (desired vs actual output)
- Control Output: u(t) = Kp * e(t) (proportional gain applied to error)
- Purpose: Maintains synchronization between LED patterns and motor rotation
- Limitation: May cause oscillations if gain is too high

#### Hardware Integration
**Challenges and Solutions:**
1. **Motor Slip Issue:** Solved by adjusting 3D mount parameters for snug fit
2. **Fragile 3D Mounts:** Improved through iterative design refinement
3. **BS2 Memory Constraints:** EEPROM exceeded limits; resolved by implementing Teensy 4.1 as dedicated LED driver in Stage II
4. **Slip Ring Wire Damage:** High RPMs cause wire burning; custom sliprings developed as innovation opportunity

#### Software Architecture
**Stage I Code Flow:**
- Initialize BS2 and sensors
- Read Hall effect sensor for synchronization signals
- Read photodiode for ambient light
- Adjust LED brightness based on ambient light
- Execute LED pattern based on motor RPM
- Loop and repeat

**Stage II Code Flow:**
- BS2 processes sensor data (Hall effect, photodiode)
- BS2 sends commands to Teensy 4.1
- Teensy 4.1 controls NeoPixel Ring with precise timing
- Feedback loop maintains synchronization
- More complex pattern generation possible

### Results and Findings

#### Stage I Results
- Successfully created a visually aesthetic ring of light with 6 RGB LEDs
- Demonstrated basic POV effect with synchronized LED patterns
- Achieved stable rotation with motor control
- Verified Hall effect sensor synchronization functionality

#### Stage II Results
- Successfully implemented advanced 24-LED NeoPixel Ring display
- Achieved more detailed and vibrant visual effects
- Demonstrated scalability from 6 to 24 LEDs
- Maintained synchronization with increased complexity
- Smoother transitions and more intricate patterns possible

#### Key Findings
1. **Power Efficiency:** Rapid flickering reduces overall power consumption vs continuous LED operation
2. **Individual Perception Variability:** Effectiveness varies among users due to different flicker fusion thresholds
3. **Visual Discomfort Risk:** Improper calibration can cause eye strain with prolonged use
4. **Learning Curve:** Complex system requires guidance for beginners; good for intermediate-advanced students

### Bill of Materials and Costs

#### Stage I Cost Breakdown
- RGB LEDs (10): $0.99 each = $9.90
- Micro Motor DC 7V (6700-6900 RPM): $8.99
- Sliprings (2): $8.00
- MOSFET with protector: $3.66
- Basic Stamp 2 module: $49.00
- Ambient light sensor (Photodiode): $2.00
- Digital potentiometer: $1.52
- Electronic Trimmer 1 MOhm: $1.00
- Electronic Trimmer 100K Ohm: $1.00
- Relay Module: $1.99
- Small DC Motor: $4.99
**Subtotal: $92.05**

#### Stage II Additional/Modified Components
- Adafruit NeoPixel Ring (24 LEDs): $11.50
- LED driver (Teensy 4.1): $29.60
- ADC: $0.98
- 555 Timer: $0.50
**Total Combined Cost: $125.10**

#### Mass Production Cost Analysis
- Estimated bulk cost significantly lower than retail
- Basic Stamp 2: $25.00 (bulk, vs $49 retail)
- DC Motor: $5.00
- Total estimated mass production cost: $81.71
- Potential for further reduction through:
  - Alternative microcontroller selection
  - LED configuration optimization
  - Alternative suppliers
  - Design optimizations

### Unique Features and Contributions

1. **Educational Scalability Model:** Two-stage implementation clearly demonstrates how to overcome hardware limitations through intelligent design decisions

2. **Memory-Efficient Programming:** Teaches students about microcontroller constraints and practical workarounds

3. **Interdisciplinary Learning:** Combines electronics, programming, physics, and mechanical engineering

4. **Affordability vs Competitors:**
   - More affordable than Parallax BoeBot Kit
   - More unique than Arduino Science Kit
   - Innovative approach to traditional robotics education

5. **Hands-On Sensor Integration:**
   - Hall Effect sensor for motion sensing
   - Photodiode for environmental feedback
   - Motor synchronization techniques
   - Real-time adaptive control

6. **Practical Visual Perception Concepts:**
   - Flicker fusion threshold
   - Persistence of vision phenomenon
   - Human eye perception timing

7. **Expandability:** Modular design allows integration of additional sensors and hardware

---

## PROJECT 2: ROS/RVIZ AUTONOMOUS NAVIGATION - TURTLEBOT3 MAZE

### Project Title and Objective
- **Full Title:** Applications of ROS: Exploring Autonomous Navigation
- **Course Context:** Robotic Operation System, Third year, 2nd semester, 2023
- **Primary Objective:** Demonstrate and test autonomous navigation capabilities using ROS Noetic and TurtleBot3 (Waffle Pi) in a simulated maze environment
- **Educational Focus:** Emphasize accessibility and educational value of autonomous systems in robotics, self-driving vehicles, and industrial automation

### Author and Institution
- **Author:** Josephine O.E. Odusanya (Student number: 9200353007)
- **Institution:** School of Automation and Electrical Engineering
- **Major:** Robotics Engineering 201

### Project Significance
- **Practical Relevance:** Addresses the growing demand for autonomous systems in dynamic environments
- **Real-World Applications:** Logistics, warehousing, manufacturing, self-driving vehicles, search and rescue, space exploration
- **Innovation Focus:** Demonstrates how ROS provides a robust framework for real-time decision-making, obstacle avoidance, and path planning

### Key System Components and Specifications

#### Software Stack
- **Ubuntu 20.04** ("Focal Fossa") - LTS release with GNOME desktop environment
- **ROS Noetic Ninjemys** - 13th ROS distribution (released May 23, 2020)
  - Still under LTS (Long Term Support)
  - Enhanced capabilities for ROS 1 exploration
  - Improved compatibility and stability
- **Gazebo** - Open-source simulation tool for robotics
  - Realistic physics engines
  - Sensor simulation
  - Pre-built models and environments
  - Extensive APIs and plugin support
- **TurtleBot3 Packages**
  - turtlebot3_msgs
  - turtlebot3
  - turtlebot3_simulations
  - turtlebot3_manipulation

#### Robot Platform
- **TurtleBot3 (Waffle Pi variant)**
  - Small, affordable, programmable ROS-based mobile robot
  - 360-degree distance sensors (LiDAR)
  - Cost-effective SBC (Single Board Computer)
  - 3D printing technology integration
  - Expandable design
  - Educational and research focused

#### Simulation Environment
- **Custom Maze Creation:**
  - Designed using PowerPoint
  - Built in Gazebo Building Editor
  - Configuration format (.config) and Simulation Description Format (.sdf) files
  - Includes interactive elements (trash can, dumpster)
  - Saved in user workspace (/home/jojo/.gazebo/models/my_maze)

#### Navigation Architecture
- **SLAM (Simultaneous Localization and Mapping)**
  - Creates and updates environment map
  - Tracks robot position on map in real-time
  - gmapping implementation used

### Technical Approach and Methodology

#### Experimental Setup Process

**Step 1: Workspace and Package Creation**
- Created new workspace: 'rosfinal'
- Created new package: 'my_simulations'
- Cloned turtlebot3, turtlebot3_msgs, and turtlebot3_simulations packages
- Added 'launch' and 'worlds' folders

**Step 2: Launch File Configuration**
- Created 'empty_world.launch' file
- Copied turtlebot3_empty_world.launch contents
- Modified launch file to reference custom 'my_world.world'

**Step 3: Maze Model Creation**
- Design: PowerPoint image-based design
- Implementation: Gazebo Building Editor
- Output: Two critical files
  - .config (configuration)
  - .sdf (Simulation Description Format)

**Step 4: SLAM Mapping Phase**
- Launched gmapping node: `roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping`
- Launched teleop (keyboard control): `roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`
- Manually drove robot to collect sensor data
- Goal: Create complete and accurate map of maze environment

**Step 5: Map Persistence**
- Saved maps to home directory: `rosrun map_server map_saver -f ~/map`
- Creates YAML file for map reference
- Enables reproducible autonomous navigation tests

**Step 6: Autonomous Navigation Launch**
- Launched navigation package: `roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml`

**Step 7: Navigation Control (RViz Interface)**
- Used 2D Pose Selector: Manually positioned robot on map with arrow indicating estimated position
- Used 2D NAV Goal: Robot autonomously navigates to selected destination

#### Core Algorithms and Techniques

**Path Planning:**
- Autonomous path planning to goal waypoints
- Obstacle avoidance in real-time
- Collision prevention

**Autonomous Navigation Features:**
- Intelligent path planning
- Obstacle detection and avoidance
- Goal-oriented navigation
- Real-time decision-making

**Sensor Integration:**
- LiDAR-based distance sensing (360 degrees)
- Environmental perception
- Dynamic obstacle detection

### Results and Findings

#### Successful Demonstrations
1. **Autonomous Navigation Capability:** Waffle Pi successfully navigated the custom maze environment autonomously
2. **Precision and Efficiency:** Robot demonstrated:
   - Precision path execution to designated goals
   - Efficient route planning
   - Reliable obstacle avoidance
3. **SLAM Functionality:** Successfully created and maintained accurate environment maps
4. **Synchronization:** Seamless integration of perception, planning, and execution

#### Key Observations
1. **Navigation Performance:**
   - Robot intelligently planned paths
   - Avoided obstacles reliably
   - Reached designated goals consistently (when paths were clear and well-defined)

2. **System Reliability:**
   - ROS Noetic and TurtleBot3 integration functioned smoothly
   - Gazebo simulation provided realistic environment representation

#### Limitations Identified
- Performance dependent on clear, well-defined paths
- Complex environmental scenarios may require algorithm optimization

### Future Enhancements and Recommendations

**Path Planning Optimization:**
- Fine-tune algorithms for speed optimization
- Energy efficiency improvements
- Task-specific requirement customization

**Advanced Sensing:**
- Integration of LiDAR (already present, but could be enhanced)
- Stereo cameras for improved perception
- Additional sensor technologies for complex environments

**Scalability and Application:**
- Multi-robot coordination scenarios
- Real-world environment deployment
- Dynamic obstacle handling (moving obstacles)
- Extended mission planning

### Unique Features and Contributions

1. **Comprehensive Documentation:** Clear step-by-step methodology for autonomous navigation setup

2. **Custom Environment Design:** Demonstrated creation of custom maze environments in Gazebo

3. **Educational Approach:** Systematic breakdown of complex ROS concepts for accessibility

4. **Practical Integration:** Successfully integrated:
   - Simulation environment (Gazebo)
   - Mapping algorithm (gmapping)
   - Navigation framework (ROS navigation stack)
   - Visualization tool (RViz)

5. **Reproducible Methodology:** Map saving and reuse enables consistent testing scenarios

6. **Realistic Application Focus:** Direct connection to real-world robotics applications

7. **LTS Platform Choice:** Use of stable, long-term supported software (Ubuntu 20.04, ROS Noetic) for reliability

---

## SUMMARY TABLE: KEY METRICS COMPARISON

| Aspect | POV Educational Kit | ROS/RViz Autonomous Navigation |
|--------|-------------------|--------------------------------|
| **Type** | Hardware-Software Mechatronics | Software Simulation Study |
| **Primary Author** | Team of 3 | Josephine O.E. Odusanya |
| **Estimated Duration** | ~50 hours | Not specified |
| **Target Audience** | Students 13+, Pre-college | Robotics Engineering 3rd year |
| **Main Objective** | Visual perception learning via POV | Autonomous navigation demonstration |
| **Key Innovation** | Scalable two-stage LED display system | Custom maze simulation with ROS |
| **Primary Component Cost** | $125.10 (complete kit) | Simulation-based (no hardware cost) |
| **Programming Language(s)** | PBASIC, Teensy C++ | ROS/Python/Bash |
| **Sensor Integration** | Hall Effect, Photodiode, Motor | LiDAR (360°), TurtleBot3 sensors |
| **Control Method** | Proportional feedback control | SLAM & autonomous path planning |
| **Education Focus** | Mechatronics, signals, programming | ROS framework, autonomous systems |
| **Expandability** | Additional sensors and hardware | Multi-robot systems, real-world deployment |

---

## MARKDOWN DOCUMENTATION TEMPLATES

### For POV Project Page
Use the extracted information to create sections covering:
- Project overview and educational value
- Two-stage implementation approach
- Detailed hardware and software specifications
- Bill of materials with cost analysis
- Assembly and programming guides
- Troubleshooting tips from debugging section
- References and extensions

### For ROS/RViz Maze Project Page
Use the extracted information to create sections covering:
- ROS fundamentals and software stack introduction
- TurtleBot3 platform overview
- Step-by-step experimental methodology
- Gazebo environment setup
- SLAM mapping process
- Autonomous navigation implementation
- Results and observations
- Future improvements and scalability
- References to ROS documentation and repositories

---

## ADDITIONAL NOTES

### POV Project Highlights
- **Innovation Point:** Two-stage design showing hardware limitation workarounds
- **Real Cost:** $81.71 estimated for mass production (vs $125.10 prototype)
- **Key Challenge:** BS2 EEPROM memory limitations solved by Teensy integration
- **Unique Selling Point:** Affordable, educational alternative to commercial kits

### ROS/RViz Project Highlights
- **Methodology Strength:** Clear, reproducible experimental process
- **Tool Integration:** Effective combination of Gazebo, SLAM, and RViz
- **Author Enthusiasm:** Strong passion for autonomous systems evident in conclusion
- **Practical Application:** Direct relevance to real-world robotics challenges

---

*Document Generated: January 19, 2026*
*Source PDFs: POV Team 3-Report.pdf (30 pages) & Applications of ROS...pdf (11 pages)*
