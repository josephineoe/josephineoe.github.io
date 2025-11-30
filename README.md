# MESGRO - Robotics & Mechatronics Portfolio Template

![MESGRO Banner](assets/images/mesgro-banner.png)

**MESGRO** (Mechatronics Engineering Showcase Gallery for Robotics Operations) is a comprehensive Jekyll template designed specifically for robotics and mechatronics engineers to create stunning portfolios that showcase their technical projects with interactive 3D models, circuit schematics, and detailed documentation.

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-green.svg)](https://pages.github.com/)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3+-red.svg)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## 🌟 Features

### 📱 Modern & Responsive Design
- **Mobile-First Approach**: Optimized for all devices and screen sizes
- **Dark/Light Themes**: Toggle between themes with smooth transitions
- **Accessible**: Built with accessibility best practices
- **Fast Loading**: Optimized performance and loading times

### 🤖 3D Model Viewer
- **Interactive 3D Models**: Display STL, OBJ, GLTF, and GLB files
- **Model Controls**: Rotate, zoom, pan, and fullscreen viewing
- **Auto-rotation**: Optional automatic model rotation
- **Model Error Handling**: Graceful fallbacks for unsupported files

### ⚡ Circuit Schematic Display
- **Zoomable Schematics**: Pan and zoom circuit diagrams
- **Multiple Formats**: Support for PNG, JPG, SVG, and PDF
- **Fullscreen Mode**: Detailed examination of complex circuits
- **Touch Optimization**: Mobile-friendly zoom and pan gestures

### 💻 Code Integration
- **Syntax Highlighting**: Support for 20+ programming languages
- **Tabbed Interface**: Organize multiple code files cleanly
- **Download Links**: Direct links to source code repositories
- **Copy to Clipboard**: Easy code sharing functionality

### 🎨 Rich Media Support
- **Image Galleries**: Showcase project photos and results
- **Video Integration**: Embed demonstration videos
- **GIF Support**: Show project animations and processes
- **Medium Zoom**: Click to zoom images for detailed viewing

## 🚀 Quick Start

### 1. Fork & Clone
```bash
# Fork this repository on GitHub, then clone it
git clone https://github.com/yourusername/MESGRO.git
cd MESGRO
```

### 2. Install Dependencies
```bash
# Install Ruby dependencies
bundle install

# Optional: Install Node.js dependencies for additional tools
npm install
```

### 3. Configure Your Site
Edit `_config.yml` to customize your portfolio:

```yaml
title: "Your Name - Robotics Portfolio"
description: "Your portfolio description"
url: "https://yourusername.github.io"
baseurl: "/MESGRO"
author: "Your Name"
email: "your.email@example.com"
```

### 4. Run Locally
```bash
# Start the Jekyll development server
bundle exec jekyll serve

# Your site will be available at http://localhost:4000
```

### 5. Deploy to GitHub Pages
1. Push your changes to the `main` branch
2. Go to your repository settings
3. Enable GitHub Pages from the `main` branch
4. Your portfolio will be live at `https://yourusername.github.io/MESGRO`

## 📁 Project Structure

```
MESGRO/
├── _config.yml                 # Site configuration
├── _layouts/                   # Page layouts
│   ├── default.html           # Base layout
│   └── project.html           # Project page layout
├── _includes/                  # Reusable components
│   ├── header.html            # Site header
│   └── footer.html            # Site footer
├── _sass/                      # Sass stylesheets
│   ├── _base.scss             # Base styles and variables
│   ├── _layout.scss           # Layout styles
│   ├── _components.scss       # Component styles
│   ├── _project.scss          # Project-specific styles
│   └── _responsive.scss       # Responsive design
├── _projects/                  # Your project markdown files
│   └── example-project.md     # Example project
├── assets/                     # ⭐ STATIC ASSETS (Add your files here!)
│   ├── css/                   # Compiled CSS
│   ├── js/                    # JavaScript files
│   ├── images/                # 🖼️ Images and photos
│   │   └── projects/          # Project-specific images
│   ├── models/                # 🤖 3D model files (STL, GLTF, GLB)
│   │   └── your-project/      # Create a folder per project
│   └── schematics/            # ⚡ Circuit diagrams (SVG, PNG)
│       └── your-project/      # Create a folder per project
├── scripts/                    # 🛠️ Utility scripts
│   ├── cad_to_gltf.py         # CAD to GLTF converter
│   ├── spice_to_svg.py        # SPICE to SVG schematic generator
│   ├── requirements.txt       # Python dependencies
│   └── README.md              # Scripts documentation
├── Gemfile                     # Ruby dependencies
└── README.md                   # This file
```

### 📂 Adding Your Project Assets

To add a new project, create the following folder structure:

```bash
assets/
├── images/projects/your-project/
│   ├── featured.jpg           # Main project image
│   └── gallery/               # Additional photos
├── models/your-project/
│   └── model.gltf             # 3D models (use cad_to_gltf.py to convert)
└── schematics/your-project/
    └── circuit.svg            # Circuit diagrams
```

> **💡 Tip:** Use the CAD-to-GLTF converter script to convert your STL/STEP files:
> ```bash
> conda run -n mesgro python scripts/cad_to_gltf.py -i model.stl -o assets/models/your-project/model.gltf
> ```

## 📝 Creating Projects

### Project Front Matter
Each project is a Markdown file in the `_projects/` directory with YAML front matter:

```yaml
---
layout: project
title: "Your Project Title"
description: "Brief project description"
date: 2024-10-30
categories: [Robotics, Arduino, Mechatronics]
featured_image: "/assets/images/projects/your-project/featured.jpg"
github_url: "https://github.com/yourusername/your-project"
demo_url: "https://youtu.be/your-demo-video"

# 3D Models
models:
  - file: "/assets/models/your-project/model.stl"
    description: "Your 3D model description"

# Circuit Schematics
schematics:
  - file: "/assets/schematics/your-project/circuit.png"
    description: "Your circuit description"

# Code Files
code_files:
  - name: "Main Code"
    file: "main.cpp"
    language: "cpp"
    download_url: "https://github.com/yourusername/your-project/blob/main/src/main.cpp"
    content: |
      // Your code here
      #include <Arduino.h>
      
      void setup() {
        Serial.begin(9600);
      }
      
      void loop() {
        // Main loop
      }

# Components List
components:
  - name: "Arduino Uno"
    quantity: 1
    description: "Main microcontroller"
    link: "https://store.arduino.cc/products/arduino-uno-rev3"

# Media Gallery
gallery:
  - type: "image"
    file: "/assets/images/projects/your-project/photo1.jpg"
    description: "Project photo description"
  - type: "video"
    file: "/assets/images/projects/your-project/demo.mp4"
    description: "Demo video description"
---

Your project content goes here. Use Markdown for formatting.

## Project Overview
Describe your project here...

## Technical Details
Add technical specifications, algorithms, etc...
```

### Supported File Formats

#### 3D Models
- **STL**: Most common 3D printing format
- **OBJ**: Wavefront OBJ files with materials
- **GLTF**: Modern 3D format with PBR materials
- **GLB**: Binary GLTF format

#### Schematics
- **PNG/JPG**: Raster images
- **SVG**: Scalable vector graphics
- **PDF**: Portable document format

#### Code Languages
- C/C++, Arduino, Python, JavaScript, MATLAB, Java, and 15+ more

## 🎨 Customization

### Themes
The template includes both light and dark themes. Users can toggle between them using the theme switcher in the header.

### Colors
Customize colors by editing the CSS custom properties in `_sass/_base.scss`:

```scss
:root {
  --primary-color: #2563eb;
  --secondary-color: #10b981;
  --accent-color: #f59e0b;
  /* Add your custom colors */
}
```

### Layout
Modify layouts in the `_layouts/` directory:
- `default.html`: Base layout for all pages
- `project.html`: Layout for project pages

### Components
Add or modify reusable components in `_includes/`:
- `header.html`: Site navigation
- `footer.html`: Site footer

## 🛠️ Development

### Prerequisites
- Ruby 2.7+ with Bundler
- Node.js 14+ (optional, for additional tooling)
- Git
- Python 3.11+ with conda (for CAD converter scripts)

### CAD-to-GLTF Converter

Convert your CAD files (STL, STEP) to web-ready GLTF format:

```bash
# Setup (one-time)
conda create -n mesgro python=3.11 -y
conda activate mesgro
pip install -r scripts/requirements.txt

# Convert STL to GLTF
python scripts/cad_to_gltf.py -i model.stl -o output.gltf

# Convert STEP to GLTF
python scripts/cad_to_gltf.py -i assembly.step -o output.gltf
```

**Supported formats:** `.stl`, `.step`, `.stp`

> **Note:** SolidWorks (`.sldprt`) and Autodesk (`.f3d`) files are not directly supported.
> Export to STL or STEP from your CAD software first.

See [scripts/README.md](scripts/README.md) for detailed documentation.

### Local Development
```bash
# Install dependencies
bundle install

# Start development server with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build
```

### Adding Features
1. Create feature branch: `git checkout -b feature/new-feature`
2. Make your changes
3. Test locally
4. Submit pull request

### JavaScript Development
The template uses vanilla JavaScript for better performance:
- `assets/js/main.js`: Core functionality
- `assets/js/project-viewer.js`: Project-specific features

### Sass Development
Styles are organized using the 7-1 Sass architecture:
- `_base.scss`: Variables, mixins, base styles
- `_layout.scss`: Header, footer, navigation
- `_components.scss`: Buttons, cards, UI components
- `_project.scss`: Project-specific styles
- `_responsive.scss`: Mobile optimization

## 📦 Deployment Options

### GitHub Pages (Recommended)
1. Fork this repository
2. Enable GitHub Pages in repository settings
3. Your site will be available at `https://yourusername.github.io/MESGRO`

### Netlify
1. Connect your GitHub repository to Netlify
2. Set build command: `bundle exec jekyll build`
3. Set publish directory: `_site`

### Custom Server
1. Build the site: `bundle exec jekyll build`
2. Upload `_site/` directory to your web server

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Types of Contributions
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 Design enhancements
- 🧪 Testing

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📋 Roadmap

### Version 2.0
- [ ] Plugin system for custom components
- [ ] Advanced 3D model annotations
- [ ] Interactive circuit simulators
- [ ] Multi-language support
- [ ] Advanced analytics integration

### Version 1.1
- [ ] Search functionality
- [ ] Project filtering by tags
- [ ] RSS feed for projects
- [ ] SEO optimizations
- [ ] Performance improvements

## 🔧 Troubleshooting

### Common Issues

**Models not loading?**
```bash
# Check file format and path
# Ensure files are in assets/models/ directory
# Verify file permissions
```

**Styles not applying?**
```bash
# Rebuild CSS
bundle exec jekyll build

# Check for Sass compilation errors
bundle exec jekyll serve --verbose
```

**Site not deploying?**
```bash
# Check Jekyll configuration
bundle exec jekyll doctor

# Verify GitHub Pages settings
# Check repository permissions
```

## 📚 Resources

### Learning Materials
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Three.js Documentation](https://threejs.org/docs/)
- [Model Viewer](https://modelviewer.dev/)
- [Sass Guidelines](https://sass-guidelin.es/)

### Inspiration
- [Robotics Portfolio Examples](https://github.com/topics/robotics)
- [Jekyll Themes](https://jekyllthemes.io/)
- [Web Design Inspiration](https://www.awwwards.com/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Jekyll Team**: For the amazing static site generator
- **Google Model Viewer**: For the 3D model viewing capabilities
- **Three.js Community**: For 3D graphics inspiration
- **GitHub Pages**: For free hosting
- **Contributors**: Everyone who helps improve this template

## 📞 Support

- 📧 **Email**: [support@mesgro.dev](mailto:support@mesgro.dev)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/aojedao/MESGRO/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/aojedao/MESGRO/issues)
- 📖 **Wiki**: [Project Wiki](https://github.com/aojedao/MESGRO/wiki)

## ⭐ Show Your Support

If this project helped you create an amazing portfolio, please consider:
- ⭐ Starring the repository
- 🐦 Sharing on social media
- 📝 Writing a blog post about your experience
- 💰 [Sponsoring the project](https://github.com/sponsors/aojedao)

---

<div align="center">
  <p>Built with ❤️ for the robotics and mechatronics community</p>
  <p><strong>MESGRO</strong> - Showcase Your Engineering Excellence</p>
</div>