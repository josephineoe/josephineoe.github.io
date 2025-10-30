---
layout: default
---

<div class="hero-personal">
  <div class="container">
    <div class="hero-content">
      <div class="hero-avatar">
        <img src="{{ '/assets/images/profile.svg' | relative_url }}" alt="Profile Picture" class="avatar-image">
        <div class="avatar-ring"></div>
      </div>
      <div class="hero-info">
        <h1 class="hero-name">{{ site.author | default: "Your Name" }}</h1>
        <p class="hero-title">Robotics & Mechatronics Engineer</p>
        <p class="hero-description">Passionate about creating intelligent systems that bridge the gap between mechanical design, electronics, and software. Specializing in autonomous robotics, computer vision, and IoT solutions.</p>
        
        <div class="hero-stats">
          <div class="stat">
            <span class="stat-number">{{ site.projects.size | default: "8" }}+</span>
            <span class="stat-label">Projects</span>
          </div>
          <div class="stat">
            <span class="stat-number">3+</span>
            <span class="stat-label">Years Experience</span>
          </div>
          <div class="stat">
            <span class="stat-number">15+</span>
            <span class="stat-label">Technologies</span>
          </div>
        </div>
        
        <div class="hero-actions">
          <a href="/projects/" class="btn-primary">
            <i class="fas fa-rocket"></i>
            View My Work
          </a>
          <a href="/about/" class="btn-secondary">
            <i class="fas fa-user"></i>
            About Me
          </a>
          <a href="mailto:{{ site.email }}" class="btn-outline">
            <i class="fas fa-envelope"></i>
            Get In Touch
          </a>
        </div>
        
        <div class="social-links">
          <a href="https://github.com/{{ site.github_username | default: 'aojedao' }}" target="_blank" class="social-link">
            <i class="fab fa-github"></i>
          </a>
          <a href="https://linkedin.com/in/{{ site.linkedin_username | default: 'your-linkedin' }}" target="_blank" class="social-link">
            <i class="fab fa-linkedin"></i>
          </a>
          <a href="https://twitter.com/{{ site.twitter_username | default: 'your-twitter' }}" target="_blank" class="social-link">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="mailto:{{ site.email | default: 'your.email@example.com' }}" class="social-link">
            <i class="fas fa-envelope"></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="skills-section">
  <div class="container">
    <div class="skills-content">
      <h2>Technical Expertise</h2>
      <div class="skills-grid">
        <div class="skill-category">
          <h3><i class="fas fa-robot"></i> Robotics</h3>
          <div class="skill-tags">
            <span class="skill-tag">ROS</span>
            <span class="skill-tag">Kinematics</span>
            <span class="skill-tag">Path Planning</span>
            <span class="skill-tag">SLAM</span>
          </div>
        </div>
        <div class="skill-category">
          <h3><i class="fas fa-microchip"></i> Electronics</h3>
          <div class="skill-tags">
            <span class="skill-tag">Arduino</span>
            <span class="skill-tag">ESP32</span>
            <span class="skill-tag">PCB Design</span>
            <span class="skill-tag">Sensors</span>
          </div>
        </div>
        <div class="skill-category">
          <h3><i class="fas fa-code"></i> Programming</h3>
          <div class="skill-tags">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">C/C++</span>
            <span class="skill-tag">MATLAB</span>
            <span class="skill-tag">JavaScript</span>
          </div>
        </div>
        <div class="skill-category">
          <h3><i class="fas fa-cube"></i> CAD/Design</h3>
          <div class="skill-tags">
            <span class="skill-tag">SolidWorks</span>
            <span class="skill-tag">Fusion 360</span>
            <span class="skill-tag">3D Printing</span>
            <span class="skill-tag">KiCad</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="projects-showcase">
  <div class="container">
    <div class="section-header">
      <h2>Featured Projects</h2>
      <p>Explore my latest robotics and mechatronics projects</p>
    </div>
    
    <div class="projects-grid-featured">
      {% for project in site.projects limit:9 %}
        <div class="project-card-featured">
          <div class="project-media">
            {% if project.featured_image %}
              <img src="{{ project.featured_image | relative_url }}" alt="{{ project.title }}" class="project-image">
            {% elsif project.models.first %}
              <div class="model-preview-small">
                <model-viewer 
                  src="{{ project.models.first.file | relative_url }}"
                  alt="{{ project.title }}"
                  camera-controls
                  auto-rotate
                  class="preview-model-small">
                </model-viewer>
              </div>
            {% else %}
              <div class="project-placeholder-small">
                <i class="fas fa-robot"></i>
              </div>
            {% endif %}
            
            <div class="project-overlay">
              <a href="{{ project.url | relative_url }}" class="project-link-overlay">
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>
          
          <div class="project-info-featured">
            <div class="project-categories-small">
              {% for category in project.categories limit:2 %}
                <span class="category-tag-small">{{ category }}</span>
              {% endfor %}
            </div>
            
            <h3 class="project-title-featured">
              <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
            </h3>
            
            <p class="project-excerpt-small">{{ project.description | truncate: 80 }}</p>
            
            <div class="project-features-small">
              {% if project.models %}
                <span class="feature-badge-small" title="3D Models">
                  <i class="fas fa-cube"></i>
                  {{ project.models.size }}
                </span>
              {% endif %}
              
              {% if project.schematics %}
                <span class="feature-badge-small" title="Schematics">
                  <i class="fas fa-microchip"></i>
                  {{ project.schematics.size }}
                </span>
              {% endif %}
              
              {% if project.code_files %}
                <span class="feature-badge-small" title="Code Files">
                  <i class="fas fa-code"></i>
                  {{ project.code_files.size }}
                </span>
              {% endif %}
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
    
    <div class="showcase-actions">
      <a href="/projects/" class="btn-primary-large">
        <i class="fas fa-th"></i>
        View All Projects
      </a>
    </div>
  </div>
</div>