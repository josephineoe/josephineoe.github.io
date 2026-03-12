---
layout: default
title: About
permalink: /about/
---

<div class="hero-section" style="padding: 100px 0; background: var(--background-color); border-bottom: 1px solid var(--border-color); text-align: center;">
    <div class="container">
        <h1 style="font-size: var(--font-size-3xl); letter-spacing: -0.02em; color: var(--text-primary);">About Me</h1>
        <p style="color: var(--text-secondary); opacity: 0.7; max-width: 600px; margin: 0 auto; font-weight: 300;">Roboticist and Biomechatronics Engineer.</p>
    </div>
</div>

<div class="about-content">
    <div class="container">
        
        <section class="about-section">
            <h2>Background</h2>
            <p>I am a passionate roboticist and biomechatronics engineer with hands-on experience designing and developing innovative robotic systems, from wearable assistive devices to industrial automation platforms. My work spans mechanical engineering, embedded systems, computer vision, and control systems—with a focus on creating technology that solves real-world problems and improves human capabilities.</p>
            
            <p>Beyond traditional engineering, I'm deeply passionate about leveraging robotics as an educational tool. My POV educational quadrotor kit exemplifies this commitment—making advanced robotics concepts accessible to students through hands-on, engaging learning experiences that inspire the next generation of engineers and innovators.</p>
            
            <p>I'm equally fascinated by the intersection of technology and experience design. My work with immersive design and interactive environments drives me to explore how sensors, sound, and spatial design can create multisensory experiences that transform physical spaces into responsive, engaging environments. This creative pursuit merges art, technology, and human interaction—crafting soundscapes and interactive installations where the environment itself becomes a medium for engagement and expression.</p>
            
            <p>Throughout my career, I've developed expertise in parallel manipulators, pneumatic actuation systems, autonomous navigation, and assistive technology design. I'm driven by a commitment to patient-centered design and creating accessible solutions for individuals with mobility challenges.</p>
        </section>

        <section class="about-section">
            <h2>Education</h2>
            <div class="education-timeline">
                <div class="education-item">
                    <div class="education-logo">
                        <img src="/assets/images/uni/nyu.png" alt="NYU Logo" style="max-height: 60px;">
                    </div>
                    <div class="education-content">
                        <h3>Master of Science in Mechanical Engineering</h3>
                        <p class="education-meta"><strong>New York University (NYU)</strong> — 2025</p>
                        <p>Focus areas: Biomechatronics, assistive technology, human-robot interaction, mechanical design</p>
                    </div>
                </div>

                <div class="education-item">
                    <div class="education-logo">
                        <img src="/assets/images/uni/zust.jpeg" alt="Zhejiang University of Science and Technology Logo" style="max-height: 60px;">
                    </div>
                    <div class="education-content">
                        <h3>Bachelor of Science in [Discipline]</h3>
                        <p class="education-meta"><strong>[University Name]</strong> — [Graduation Year]</p>
                        <p>[Add description of undergraduate focus and relevant coursework]</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="about-section">
            <h2>Technical Expertise</h2>
            <div class="expertise-grid">
                <div class="expertise-category">
                    <h3>Mechanical Engineering</h3>
                    <ul>
                        <li>Parallel Kinematics (3-RPS systems)</li>
                        <li>Pneumatic Actuation & Control</li>
                        <li>Wearable Exoskeleton Design</li>
                        <li>3D Modeling (CAD)</li>
                        <li>Mechanical Simulation & Analysis</li>
                    </ul>
                </div>
                
                <div class="expertise-category">
                    <h3>Embedded Systems & Control</h3>
                    <ul>
                        <li>Propeller Microcontroller Architecture</li>
                        <li>Real-time Control Systems</li>
                        <li>IMU Integration & Sensor Fusion</li>
                        <li>PWM Servo Control</li>
                        <li>I2C & Serial Communication</li>
                    </ul>
                </div>

                <div class="expertise-category">
                    <h3>Robotics & Automation</h3>
                    <ul>
                        <li>Industrial Robot Programming (ABB RAPID)</li>
                        <li>ROS (Robot Operating System)</li>
                        <li>SLAM & Autonomous Navigation</li>
                        <li>Path Planning Algorithms</li>
                        <li>Multi-robot Coordination</li>
                    </ul>
                </div>

                <div class="expertise-category">
                    <h3>Software & Vision</h3>
                    <ul>
                        <li>Computer Vision (OpenCV)</li>
                        <li>Eye-Gaze Tracking Algorithms</li>
                        <li>C/C++ & Python Programming</li>
                        <li>Real-time Image Processing</li>
                        <li>Calibration & Optimization</li>
                    </ul>
                </div>

                <div class="expertise-category">
                    <h3>Hardware Design</h3>
                    <ul>
                        <li>PCB Design & Fabrication</li>
                        <li>3D Printing & Prototyping</li>
                        <li>Sensor Integration</li>
                        <li>Power Management Systems</li>
                        <li>Electronics Troubleshooting</li>
                    </ul>
                </div>

                <div class="expertise-category">
                    <h3>Assistive Technology</h3>
                    <ul>
                        <li>Patient-Centered Design</li>
                        <li>Accessibility Engineering</li>
                        <li>Rehabilitation Robotics</li>
                        <li>Human-Robot Interaction</li>
                        <li>User Experience Optimization</li>
                    </ul>
                </div>
            </div>
        </section>



    </div>
</div>

<style>
.about-content {
    padding: var(--spacing-2xl) 0;
}

.about-section {
    margin-bottom: var(--spacing-3xl);
}

.about-section h2 {
    color: var(--text-primary);
    margin-bottom: var(--spacing-lg);
    padding-bottom: var(--spacing-sm);
    border-bottom: 1px solid var(--border-color);
    font-size: var(--font-size-2xl);
    letter-spacing: -0.01em;
}

.education-timeline {
    margin-top: var(--spacing-lg);
}

.education-item {
    display: flex;
    gap: var(--spacing-lg);
    padding: var(--spacing-lg);
    background-color: var(--surface-color);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
    margin-bottom: var(--spacing-md);
    align-items: flex-start;
}

.education-logo {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 80px;
    height: 80px;
    background-color: var(--background-color);
    border-radius: var(--radius-md);
}

.education-logo img {
    max-height: 60px;
    max-width: 60px;
}

.education-content h3 {
    color: var(--text-primary);
    margin-bottom: var(--spacing-sm);
}

.education-meta {
    color: var(--text-secondary);
    font-weight: var(--font-weight-medium);
    margin-bottom: var(--spacing-sm);
}

.expertise-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--spacing-lg);
    margin-top: var(--spacing-lg);
}

.expertise-category {
    padding: var(--spacing-lg);
    background-color: var(--surface-color);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
}

.expertise-category h3 {
    color: var(--primary-color);
    margin-bottom: var(--spacing-md);
    font-size: var(--font-size-lg);
}

.expertise-category ul {
    list-style: none;
    padding: 0;
}

.expertise-category li {
    color: var(--text-secondary);
    padding: var(--spacing-xs) 0;
    padding-left: var(--spacing-md);
    position: relative;
}

.expertise-category li:before {
    content: "→";
    position: absolute;
    left: 0;
    color: var(--primary-color);
}

.features-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-xl);
    margin-top: var(--spacing-lg);
}

.feature-item {
    padding: var(--spacing-lg);
    background-color: var(--surface-color);
    border-radius: var(--radius-sm);
    border: none;
    box-shadow: 0 4px 20px var(--shadow-color);
    transition: transform var(--transition-normal), box-shadow var(--transition-normal);
}

.feature-item:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px var(--shadow-hover);
}

.feature-item h3 {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
}

.feature-item h3 i {
    color: var(--primary-color);
    font-size: var(--font-size-lg);
}

.tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-lg);
    justify-content: center;
    margin-top: var(--spacing-lg);
}

.tech-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--spacing-sm);
    padding: var(--spacing-lg);
    background-color: var(--surface-color);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
    min-width: 120px;
}

.tech-item i {
    font-size: var(--font-size-2xl);
    color: var(--accent-color);
}

.tech-item span {
    font-weight: var(--font-weight-medium);
    color: var(--text-primary);
    text-align: center;
    font-size: var(--font-size-sm);
}

.getting-started-steps {
    background-color: var(--surface-color);
    padding: var(--spacing-xl);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
    margin: var(--spacing-lg) 0;
}

.getting-started-steps li {
    margin-bottom: var(--spacing-md);
    line-height: var(--line-height-relaxed);
}

.getting-started-steps a {
    color: var(--primary-color);
    text-decoration: none;
}

.getting-started-steps a:hover {
    text-decoration: underline;
}

.cta-buttons {
    display: flex;
    gap: var(--spacing-md);
    justify-content: center;
    flex-wrap: wrap;
    margin-top: var(--spacing-xl);
}

@media (max-width: 640px) {
    .features-list {
        grid-template-columns: 1fr;
    }
    
    .expertise-grid {
        grid-template-columns: 1fr;
    }
    
    .education-item {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .tech-stack {
        justify-content: center;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
}
</style>