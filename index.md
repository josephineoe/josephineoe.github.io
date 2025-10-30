---
layout: default
---

<div class="hero-section">
  <div class="container">
    <h1 class="hero-title">{{ site.title }}</h1>
    <p class="hero-description">{{ site.description }}</p>
    <a href="/projects/" class="btn-primary">View Projects</a>
  </div>
</div>

<div class="features-section">
  <div class="container">
    <h2>Features</h2>
    <div class="features-grid">
      <div class="feature">
        <div class="feature-icon">🤖</div>
        <h3>3D Model Viewer</h3>
        <p>Interactive 3D visualization of mechanical designs, STL files, and prototypes</p>
      </div>
      <div class="feature">
        <div class="feature-icon">⚡</div>
        <h3>Circuit Schematics</h3>
        <p>Zoomable circuit diagrams and electrical schematics with detailed component views</p>
      </div>
      <div class="feature">
        <div class="feature-icon">💻</div>
        <h3>Code Integration</h3>
        <p>Syntax-highlighted code blocks with GitHub integration and download links</p>
      </div>
      <div class="feature">
        <div class="feature-icon">📱</div>
        <h3>Responsive Design</h3>
        <p>Mobile-friendly interface that works seamlessly across all devices</p>
      </div>
    </div>
  </div>
</div>

<div class="projects-preview">
  <div class="container">
    <h2>Recent Projects</h2>
    <div class="projects-grid">
      {% for project in site.projects limit:6 %}
        <div class="project-card">
          {% if project.featured_image %}
            <img src="{{ project.featured_image | relative_url }}" alt="{{ project.title }}" class="project-image">
          {% endif %}
          <div class="project-content">
            <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
            <p>{{ project.description | truncate: 120 }}</p>
            <div class="project-tags">
              {% for tag in project.categories %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
    <div class="text-center">
      <a href="/projects/" class="btn-secondary">View All Projects</a>
    </div>
  </div>
</div>