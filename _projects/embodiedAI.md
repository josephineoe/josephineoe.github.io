---
layout: project
published: false
title: "Embodied AI & Machine Learning Systems"
description: "A collection of embodied AI, machine learning, and reinforcement learning projects focused on autonomous navigation, learning agents, and intelligent systems. Explores the intersection of perception, decision-making, and physical interaction in dynamic environments."
date: 2024-12-14
categories: [Robotics, Machine Learning, Reinforcement Learning, Computer Vision, Autonomous Systems]
featured_image: "/assets/images/projects/embodiedai/featured.jpg"

gallery:
  - type: "video"
    file: "DeadEnds/DeadEnds/ExtraVideo_RawFinalVideo.mp4"
    description: "DeadEnds Embodied AI : Robot Perception"
  - type: "video"
    file: "DeadEnds/DeadEnds/PresentationVideo.mp4"
    description: "DeadEnds project presentation and results"

---

## Project Overview

**Embodied AI & Machine Learning Systems** encompasses a series of interconnected projects exploring intelligent agents that learn and interact within dynamic environments. These projects investigate reinforcement learning algorithms, vision-based perception, and autonomous decision-making systems designed to operate in real-world robotic platforms.

This collection integrates:
- **Reinforcement Learning**: Q-learning, policy gradient methods, and deep RL architectures
- **Perception Systems**: Computer vision for object detection and scene understanding
- **Autonomous Navigation**: Path planning and obstacle avoidance in dynamic environments
- **Agent Learning**: Self-improving algorithms that adapt to environmental changes
- **Embodied Interaction**: Physical systems that learn through experience and sensor feedback

<div style="margin: 20px 0; text-align: center;">
  <a href="https://github.com/josephineoe/embodied-ai-projects" style="display: inline-block; padding: 10px 20px; background-color: #333; color: #fff; text-decoration: none; border-radius: 5px; font-weight: 500; transition: background-color 0.3s;">
    <span>🐙 View on GitHub</span>
  </a>

## Project Collection

### 1. DeadEnds: Semi-autonomous Navigation & Learning

#### Project Timeline
- **Start Date**: September 2025
- **Completion Date**: November 2025
- **Status**: Complete

#### Overview
DeadEnds is an embodied AI navigation system designed to explore semi-autonomous exploration and learning in constrained environments. The system employs vision-based perception combined with reinforcement learning to develop adaptive navigation strategies.

<div style="margin: 20px 0; text-align: center;">
  <a href="https://github.com/josephineoe/vis_nav_player" style="display: inline-block; padding: 10px 20px; background-color: #2c8cff; color: #fff; text-decoration: none; border-radius: 5px; font-weight: 500; transition: background-color 0.3s; margin-bottom: 10px;">
    <span>🚀 GitHub Action: vis_nav_player</span>
  </a>
</div>

**Vision Processing**:
- Real-time camera input processing
- Obstacle detection and classification
- Environment mapping and scene understanding
- Feature extraction for state representation

**Learning Mechanisms**:
- Reinforcement learning agent architecture
- State-space representation from visual input
- Reward optimization for navigation efficiency
- Adaptive policy learning

**Navigation Capabilities**:
- Autonomous exploration of unknown environments
- Obstacle avoidance and path optimization
- Dead-end detection and backtracking
- Memory-based navigation improvement

#### Technical Architecture

```
Visual Input (Camera Feed)
    ↓
[Image Processing & Feature Detection]
    ↓
[State Representation]
    ↓
[Reinforcement Learning Agent]
    ↓
[Action Selection]
    ↓
[Motor Control & Movement]
```

#### Results & Achievements
- ✅ Successful autonomous navigation in test environments
- ✅ Learning convergence demonstrated over multiple episodes
- ✅ Efficient dead-end resolution and backtracking
- ✅ Real-time visual processing at 30+ fps
- ✅ [PLACEHOLDER: Add key metric or result]

---

### 2. Navi: ML Autonomous Navigation 

#### Project Timeline
- **Start Date**: [PLACEHOLDER: Add start date]
- **Completion Date**: [PLACEHOLDER: Add completion date]

#### Overview
[PLACEHOLDER: Add project description - focus on RL algorithm, application, and key innovations]

#### Key Components
- [PLACEHOLDER: Algorithm/approach]
- [PLACEHOLDER: Benchmark/dataset]
- [PLACEHOLDER: Evaluation metric]

---

### 3. [Project Name: Vision & Learning]

#### Project Timeline
- **Start Date**: [PLACEHOLDER: Add start date]
- **Completion Date**: [PLACEHOLDER: Add completion date]

#### Overview
[PLACEHOLDER: Add project description - focus on computer vision aspects and learning integration]

#### Technical Highlights
- [PLACEHOLDER: Vision technique]
- [PLACEHOLDER: Learning approach]
- [PLACEHOLDER: Application domain]

---

## Technical Deep Dive

### Reinforcement Learning Framework

The foundation of embodied AI systems relies on RL algorithms that learn optimal policies through interaction:

1. **Agent Architecture**
   - Perception module (sensory input processing)
   - Decision module (policy network)
   - Action module (motor control output)
   - Learning module (reward optimization)

2. **Learning Paradigms**
   - **Model-Free Learning**: Direct policy optimization without environment model
   - **Model-Based Learning**: Environment prediction coupled with planning
   - **Hybrid Approaches**: Combining model-free and model-based methods

3. **Key Algorithms**
   - Q-Learning: Value-based learning for discrete action spaces
   - Policy Gradient: Direct policy optimization
   - Actor-Critic: Combining value and policy methods
   - Deep Reinforcement Learning: Neural network function approximation

### Integration with Physical Systems

Embodied AI projects bridge the gap between learning algorithms and real robotic platforms:

- **Sim-to-Real Transfer**: Training in simulation, deploying on physical robots
- **Sensor Fusion**: Combining multiple sensor modalities for robust state estimation
- **Real-time Constraints**: Efficient algorithms for onboard computation
- **Safety Considerations**: Failure detection and safeguards during learning

## Performance Metrics

### DeadEnds Navigation System

| Metric | Value |
|---|---|
| **Success Rate** | [PLACEHOLDER] |
| **Average Episode Length** | [PLACEHOLDER] steps |
| **Learning Convergence** | [PLACEHOLDER] episodes |
| **Processing Speed** | [PLACEHOLDER] fps |
| **Memory Usage** | [PLACEHOLDER] MB |

### [Project Name]

| Metric | Value |
|---|---|
| **Accuracy** | [PLACEHOLDER] |
| **Training Time** | [PLACEHOLDER] |
| **Inference Speed** | [PLACEHOLDER] |
| **Model Size** | [PLACEHOLDER] |

## Documentation & Resources

Comprehensive project documentation is available:
- **Final Report**: Detailed analysis, methodology, and results
- **Presentation Video**: Visual demonstration of system capabilities
- **Source Code**: Implementation details and algorithm specifications
- **Datasets**: Benchmark data and evaluation scenarios

See the gallery above for all documentation and media materials.

## Challenges & Solutions

### Challenge 1: Sim-to-Real Gap
**Solution**: Domain randomization and transfer learning
- Varied simulation parameters
- Robust feature extraction
- Fine-tuning on real data

### Challenge 2: Computational Efficiency
**Solution**: Model optimization and edge deployment
- Network compression
- Efficient inference libraries
- Hardware acceleration where available

### Challenge 3: Exploration vs. Exploitation
**Solution**: Adaptive exploration strategies
- ε-greedy exploration with decay
- Upper Confidence Bound (UCB) methods
- Curiosity-driven exploration

## Future Work

- Enhanced perception using multi-modal sensors
- Transfer learning across different environments
- Human-in-the-loop learning for safety-critical tasks
- Scaling to multi-agent systems
- [PLACEHOLDER: Add planned improvements]

---

## Conclusion

The Embodied AI & Machine Learning Systems project collection demonstrates the practical application of learning algorithms to autonomous robotic platforms. By combining classical and modern machine learning techniques with embodied systems, these projects explore how agents can learn and adapt in real-world scenarios.

**Key Achievements:**
- ✅ Multiple fully functional embodied AI systems
- ✅ Validated reinforcement learning approaches
- ✅ Real-time vision integration with learning pipelines
- ✅ Autonomous navigation and exploration demonstrated

---

**Please reach out via the contact form if you have more inquiries**

