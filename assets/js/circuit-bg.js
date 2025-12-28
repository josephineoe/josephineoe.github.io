/**
 * Circuit Background Animation
 * Creates a connecting node network effect
 */

class CircuitBackground {
    constructor() {
        this.canvas = document.getElementById('canvas-bg');
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.nodes = [];
        this.resize();
        this.init();

        window.addEventListener('resize', () => this.resize());
        this.animate();
    }

    resize() {
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.initNodes();
    }

    initNodes() {
        this.nodes = [];
        // Density based on screen size
        const density = Math.floor((this.width * this.height) / 25000);

        for (let i = 0; i < density; i++) {
            this.nodes.push({
                x: Math.random() * this.width,
                y: Math.random() * this.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                size: Math.random() * 2 + 1
            });
        }
    }

    init() {
        this.initNodes();
    }

    animate() {
        if (!this.ctx) return;

        this.ctx.clearRect(0, 0, this.width, this.height);

        // Get theme color for particles
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        const particleColor = isDark ? 'rgba(255, 255, 255, 0.15)' : 'rgba(0, 0, 0, 0.1)';
        const lineColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';

        // Update and draw nodes
        this.nodes.forEach(node => {
            node.x += node.vx;
            node.y += node.vy;

            // Bounce off edges
            if (node.x < 0 || node.x > this.width) node.vx *= -1;
            if (node.y < 0 || node.y > this.height) node.vy *= -1;

            // Draw node
            this.ctx.beginPath();
            this.ctx.arc(node.x, node.y, node.size, 0, Math.PI * 2);
            this.ctx.fillStyle = particleColor;
            this.ctx.fill();

            // Connect nearby nodes
            this.nodes.forEach(otherNode => {
                const dx = node.x - otherNode.x;
                const dy = node.y - otherNode.y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 150) {
                    this.ctx.beginPath();
                    this.ctx.lineWidth = 1 - (distance / 150);
                    this.ctx.strokeStyle = lineColor;
                    this.ctx.moveTo(node.x, node.y);
                    this.ctx.lineTo(otherNode.x, otherNode.y);
                    this.ctx.stroke();
                }
            });
        });

        requestAnimationFrame(() => this.animate());
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new CircuitBackground();
});
