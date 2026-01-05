/**
 * Roses & Vines Interactive Effects
 * Save as assets/js/decorations.js
 */

(function() {
  'use strict';

  // Configuration
  const config = {
    floatingPetals: {
      enabled: true,
      count: 5, // Moderate amount
      interval: 4000, // milliseconds between petals
      colors: ['#f4c2c2', '#e8a8a8', '#d89494', '#ffd4d4']
    },
    animateVines: true,
    hoverEffects: true
  };

  /**
   * Create and animate floating rose petals
   */
  function createFloatingPetal() {
    const petal = document.createElement('div');
    petal.className = 'floating-petal';
    
    // Random starting position
    petal.style.left = Math.random() * 100 + '%';
    
    // Random size
    const size = Math.random() * 20 + 15; // 15-35px
    petal.style.width = size + 'px';
    petal.style.height = size + 'px';
    
    // Random color from palette
    const color = config.floatingPetals.colors[
      Math.floor(Math.random() * config.floatingPetals.colors.length)
    ];
    
    // Create SVG petal
    petal.innerHTML = `
      <svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="10" cy="10" rx="8" ry="12" fill="${color}" opacity="0.8"/>
      </svg>
    `;
    
    // Random animation duration (8-15 seconds)
    const duration = Math.random() * 7 + 8;
    petal.style.animationDuration = duration + 's';
    
    // Random delay
    petal.style.animationDelay = Math.random() * 2 + 's';
    
    document.body.appendChild(petal);
    
    // Remove petal after animation completes
    setTimeout(() => {
      petal.remove();
    }, (duration + 2) * 1000);
  }

  /**
   * Start floating petals effect
   */
  function startFloatingPetals() {
    if (!config.floatingPetals.enabled) return;
    
    // Create initial petals
    for (let i = 0; i < config.floatingPetals.count; i++) {
      setTimeout(() => {
        createFloatingPetal();
      }, i * 500);
    }
    
    // Continue creating petals at intervals
    setInterval(() => {
      createFloatingPetal();
    }, config.floatingPetals.interval);
  }

  /**
   * Animate vines on scroll into view
   */
  function animateVinesOnScroll() {
    if (!config.animateVines) return;
    
    const vines = document.querySelectorAll('.vine-decoration path');
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('vine-animated');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    
    vines.forEach(vine => observer.observe(vine));
  }

  /**
   * Add interactive hover effects to roses
   */
  function addRoseHoverEffects() {
    if (!config.hoverEffects) return;
    
    const roses = document.querySelectorAll('.rose-accent');
    
    roses.forEach(rose => {
      rose.addEventListener('mouseenter', () => {
        // Create sparkle effect
        const sparkle = document.createElement('div');
        sparkle.style.position = 'absolute';
        sparkle.style.top = '50%';
        sparkle.style.left = '50%';
        sparkle.style.transform = 'translate(-50%, -50%)';
        sparkle.style.fontSize = '1.2rem';
        sparkle.textContent = '✨';
        sparkle.style.animation = 'fade-out 1s ease-out forwards';
        sparkle.style.pointerEvents = 'none';
        
        rose.appendChild(sparkle);
        
        setTimeout(() => sparkle.remove(), 1000);
      });
    });
  }

  /**
   * Create rose burst effect on click
   */
  function addRoseClickEffect() {
    const roses = document.querySelectorAll('.rose-accent');
    
    roses.forEach(rose => {
      rose.style.cursor = 'pointer';
      
      rose.addEventListener('click', (e) => {
        const rect = rose.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        
        // Create burst of small petals (fewer for moderate effect)
        for (let i = 0; i < 4; i++) {
          const petal = document.createElement('div');
          petal.style.position = 'fixed';
          petal.style.left = centerX + 'px';
          petal.style.top = centerY + 'px';
          petal.style.width = '8px';
          petal.style.height = '8px';
          petal.style.pointerEvents = 'none';
          petal.style.zIndex = '9999';
          
          const angle = (Math.PI * 2 * i) / 4;
          const distance = 40;
          const endX = Math.cos(angle) * distance;
          const endY = Math.sin(angle) * distance;
          
          petal.innerHTML = `
            <svg viewBox="0 0 10 10">
              <ellipse cx="5" cy="5" rx="3" ry="5" fill="#f4c2c2" opacity="0.8"/>
            </svg>
          `;
          
          document.body.appendChild(petal);
          
          // Animate outward
          petal.style.transition = 'all 0.6s ease-out';
          setTimeout(() => {
            petal.style.transform = `translate(${endX}px, ${endY}px)`;
            petal.style.opacity = '0';
          }, 10);
          
          setTimeout(() => petal.remove(), 700);
        }
      });
    });
  }

  /**
   * Add CSS animations dynamically
   */
  function addDynamicStyles() {
    const style = document.createElement('style');
    style.textContent = `
      @keyframes fade-out {
        from {
          opacity: 1;
          transform: translate(-50%, -50%) scale(1);
        }
        to {
          opacity: 0;
          transform: translate(-50%, -50%) scale(1.5);
        }
      }
    `;
    document.head.appendChild(style);
  }

  /**
   * Create vine border that follows scroll
   */
  function createScrollingVineBorder() {
    const vineBorder = document.createElement('div');
    vineBorder.className = 'vine-scroll-border';
    vineBorder.style.position = 'fixed';
    vineBorder.style.left = '0';
    vineBorder.style.top = '0';
    vineBorder.style.width = '4px';
    vineBorder.style.background = 'linear-gradient(to bottom, #555d50, #f4c2c2, #555d50)';
    vineBorder.style.height = '0%';
    vineBorder.style.zIndex = '1000';
    vineBorder.style.transition = 'height 0.1s ease-out';
    vineBorder.style.pointerEvents = 'none';
    
    document.body.appendChild(vineBorder);
    
    window.addEventListener('scroll', () => {
      const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
      vineBorder.style.height = scrollPercent + '%';
    });
  }

  /**
   * Initialize all decorative effects
   */
  function init() {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
      return;
    }
    
    addDynamicStyles();
    startFloatingPetals();
    animateVinesOnScroll();
    addRoseHoverEffects();
    addRoseClickEffect();
    createScrollingVineBorder();
    
    console.log('🌹 Roses & Vines decorations initialized');
  }

  // Start initialization
  init();

  // Expose config for customization
  window.decorationsConfig = config;
  
})();