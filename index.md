---
layout: default
---

<div class="hero-personal" style="padding: 60px 0 40px 0;">
  <div class="container">
    <div class="hero-content" style="align-items: flex-start; text-align: left;">
      <div class="hero-info" style="width: 100%; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px;">
        <div>
           <h1 class="hero-name" style="font-size: var(--font-size-3xl); margin-bottom: 0;">{{ site.author | default: "Your Name" }}</h1>
           <p class="hero-title" style="font-size: var(--font-size-sm); margin-bottom: 0; opacity: 0.7;">Robotics & Mechatronics</p>
        </div>
        
        <div class="hero-actions" style="margin: 0;">
          <a href="{{ '/about/' | relative_url }}" class="btn-secondary" style="font-size: 12px; padding: 8px 16px;">
            About
          </a>
           <a href="mailto:{{ site.email }}" class="btn-secondary" style="font-size: 12px; padding: 8px 16px;">
            Contact
          </a>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="projects-showcase" style="padding: 20px 0 100px 0; border-top: none;">
  <div class="container">
    <div class="section-header" style="margin-bottom: 80px;">
      <h2 style="font-size: var(--font-size-3xl); letter-spacing: -0.01em;">Selected Works</h2>
      <p style="text-transform: uppercase; font-size: var(--font-size-xs); letter-spacing: 0.1em; opacity: 0.6;">A curated collection of my research and design</p>
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
      <a href="{{ '/projects/' | relative_url }}" class="btn-primary-large">
        <i class="fas fa-th"></i>
        View All Projects
      </a>
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