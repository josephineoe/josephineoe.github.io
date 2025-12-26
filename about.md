---
layout: default
title: About
permalink: /about/
---

<div class="hero-section" style="padding: 100px 0; background: var(--background-color); border-bottom: 1px solid var(--border-color); text-align: center;">
    <div class="container">
        <h1 style="font-size: var(--font-size-3xl); letter-spacing: -0.02em; color: var(--text-primary);">About MESGRO</h1>
        <p style="color: var(--text-secondary); opacity: 0.7; max-width: 600px; margin: 0 auto; font-weight: 300;">An open-source portfolio template designed specifically for robotics and mechatronics engineers to showcase their innovative projects.</p>
    </div>
</div>

<div class="about-content">
    <div class="container">
        
        <section class="about-section">
            <h2>What is MESGRO?</h2>
            <p>MESGRO (Mechatronics Engineering Showcase Gallery for Robotics Operations) is a comprehensive Jekyll template that enables engineers, researchers, and students to create stunning portfolios for their robotics and mechatronics projects.</p>
            
            <p>Built with modern web technologies and designed with user experience in mind, MESGRO provides everything you need to showcase your technical projects professionally and effectively.</p>
        </section>

        <section class="about-section">
            <h2>Key Features</h2>
            <div class="features-list">
                <div class="feature-item">
                    <h3><i class="fas fa-cube"></i> Interactive 3D Model Viewer</h3>
                    <p>Display your mechanical designs, prototypes, and 3D printed parts with an interactive viewer that supports STL, OBJ, GLTF, and GLB formats. Users can rotate, zoom, and explore your designs in detail.</p>
                </div>
                
                <div class="feature-item">
                    <h3><i class="fas fa-microchip"></i> Circuit Schematic Display</h3>
                    <p>Showcase your electrical designs with zoomable and pannable circuit diagrams. Perfect for displaying PCB layouts, wiring diagrams, and system architectures.</p>
                </div>
                
                <div class="feature-item">
                    <h3><i class="fas fa-code"></i> Code Integration</h3>
                    <p>Present your source code with syntax highlighting, tabbed interfaces, and download links. Supports multiple programming languages including C/C++, Python, Arduino, and more.</p>
                </div>
                
                <div class="feature-item">
                    <h3><i class="fas fa-mobile-alt"></i> Responsive Design</h3>
                    <p>Your portfolio looks great on all devices - from desktop computers to mobile phones. The responsive design ensures optimal viewing experience across all screen sizes.</p>
                </div>
                
                <div class="feature-item">
                    <h3><i class="fab fa-github"></i> GitHub Pages Compatible</h3>
                    <p>Deploy your portfolio for free using GitHub Pages. The template is fully compatible with Jekyll and GitHub's hosting platform.</p>
                </div>
                
                <div class="feature-item">
                    <h3><i class="fas fa-palette"></i> Customizable Theme</h3>
                    <p>Dark and light themes with easy customization options. Modify colors, fonts, and layouts to match your personal brand.</p>
                </div>
            </div>
        </section>

        <section class="about-section">
            <h2>Perfect For</h2>
            <div class="perfect-for-grid">
                <div class="perfect-for-item">
                    <h4>Students</h4>
                    <p>Showcase your coursework, capstone projects, and research work to potential employers and graduate schools.</p>
                </div>
                
                <div class="perfect-for-item">
                    <h4>Engineers</h4>
                    <p>Display your professional projects, innovations, and technical expertise to colleagues and industry peers.</p>
                </div>
                
                <div class="perfect-for-item">
                    <h4>Researchers</h4>
                    <p>Present your research findings, prototypes, and experimental setups with rich media and detailed documentation.</p>
                </div>
                
                <div class="perfect-for-item">
                    <h4>Hobbyists</h4>
                    <p>Share your maker projects, Arduino creations, and DIY robotics builds with the maker community.</p>
                </div>
            </div>
        </section>

        <section class="about-section">
            <h2>Built With</h2>
            <div class="tech-stack">
                <div class="tech-item">
                    <i class="fab fa-html5"></i>
                    <span>HTML5</span>
                </div>
                <div class="tech-item">
                    <i class="fab fa-css3-alt"></i>
                    <span>CSS3/SCSS</span>
                </div>
                <div class="tech-item">
                    <i class="fab fa-js-square"></i>
                    <span>JavaScript</span>
                </div>
                <div class="tech-item">
                    <i class="fas fa-gem"></i>
                    <span>Jekyll</span>
                </div>
                <div class="tech-item">
                    <i class="fas fa-cube"></i>
                    <span>Three.js</span>
                </div>
                <div class="tech-item">
                    <i class="fab fa-github"></i>
                    <span>GitHub Pages</span>
                </div>
            </div>
        </section>

        <section class="about-section">
            <h2>Getting Started</h2>
            <p>Ready to create your own robotics portfolio? Get started with MESGRO in just a few steps:</p>
            
            <ol class="getting-started-steps">
                <li><strong>Fork the Repository:</strong> Start by forking the MESGRO repository to your GitHub account.</li>
                <li><strong>Customize Your Content:</strong> Add your projects, update the configuration, and personalize the design.</li>
                <li><strong>Enable GitHub Pages:</strong> Turn on GitHub Pages in your repository settings to publish your portfolio.</li>
                <li><strong>Share Your Work:</strong> Your portfolio is now live and ready to share with the world!</li>
            </ol>
            
            <div class="cta-buttons">
                <a href="https://github.com/aojedao/MESGRO" class="btn-primary" target="_blank">
                    <i class="fab fa-github"></i> Get Started on GitHub
                </a>
                <a href="{{ '/projects/' | relative_url }}" class="btn-secondary">
                    <i class="fas fa-eye"></i> View Example Projects
                </a>
            </div>
        </section>

        <section class="about-section">
            <h2>Contributing</h2>
            <p>MESGRO is an open-source project and we welcome contributions from the community. Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated.</p>
            
            <p>Check out our <a href="https://github.com/aojedao/MESGRO/blob/main/CONTRIBUTING.md" target="_blank">Contributing Guide</a> to get started.</p>
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

.perfect-for-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-lg);
    margin-top: var(--spacing-lg);
}

.perfect-for-item {
    text-align: center;
    padding: var(--spacing-lg);
    background-color: var(--surface-color);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-color);
}

.perfect-for-item h4 {
    color: var(--primary-color);
    margin-bottom: var(--spacing-sm);
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
    
    .perfect-for-grid {
        grid-template-columns: 1fr;
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