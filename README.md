# MESGRO - Robotics & Mechatronics Portfolio Template

![Project Page Screenshot](assets/images/project_screenshot.png)

**MESGRO** (Mechatronics Engineering Showcase Gallery for Robotics Operations) is a comprehensive Jekyll template designed specifically for robotics and mechatronics engineers to create stunning portfolios that showcase their technical projects with interactive 3D models, circuit schematics, and detailed documentation.

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-green.svg)](https://pages.github.com/)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3+-red.svg)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Modern & Responsive Design
- 3D Model Viewer
- Circuit Schematic Display
- Code Integration
- Rich Media Support
- Interactive Data Visualization

## Cloud Development (No Installation Required)

You can develop and maintain your portfolio completely in the cloud without installing anything on your local machine.

1. **Fork the Repository**: simple click "Fork" on GitHub.
2. **Edit Online**: Use GitHub.dev (press `.` in the repo) to edit files directly in your browser.
3. **Automatic Deployment**: Any change you push to the `main` branch will automatically trigger a GitHub Action to build and deploy your site.
4. **Validation**: Check the "Actions" tab to see if your build passed.

## Quick Start

### 1. Fork & Clone
```bash
git clone https://github.com/yourusername/MESGRO.git
cd MESGRO
```

### 2. Configure Your Site
Edit `_config.yml` to customize your portfolio details.

### 3. Run Locally (Optional)
If you prefer local development:
```bash
bundle install
bundle exec jekyll serve
```

## Project Structure

```
MESGRO/
├── _config.yml                 # Site configuration
├── _layouts/                   # Page layouts
│   ├── default.html           # Base layout
│   └── project.html           # Project page layout
├── _includes/                  # Reusable components
│   ├── header.html            # Site header
│   ├── footer.html            # Site footer
│   └── interactive-plot.html  # Plotly integration
├── _sass/                      # Sass stylesheets
│   ├── _base.scss             # Base styles and variables
│   ├── _layout.scss           # Layout styles
│   ├── _components.scss       # Component styles
│   ├── _project.scss          # Project-specific styles
│   └── _responsive.scss       # Responsive design
├── _projects/                  # Your project markdown files
├── assets/                     # Static assets
│   ├── css/                   # Compiled CSS
│   ├── js/                    # JavaScript files
│   ├── images/                # Images and photos
│   ├── models/                # 3D model files (STL, GLTF, GLB)
│   └── schematics/            # Circuit diagrams (SVG, PNG)
└── scripts/                    # Utility scripts
```

## Customization

### Themes
The template includes both light and dark themes. Users can toggle between them using the theme switcher in the header.

### Colors
Customize colors by editing the CSS custom properties in `_sass/_base.scss`.

## Author

**Alejandro Ojeda Olarte**

- GitHub: [@aojedao](https://github.com/aojedao)
- Website: [aojedao.github.io](https://aojedao.github.io)

Built with ❤️ for the robotics and mechatronics community.
