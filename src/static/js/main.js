/**
 * Main JavaScript file for GitHub Copilot Demo application.
 *
 * This file contains client-side functionality for the application.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Theme Toggle Functionality
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle?.querySelector('.theme-icon');
    const themeText = themeToggle?.querySelector('.theme-text');
    const html = document.documentElement;

    // Check for saved theme preference or default to 'light' mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', currentTheme);
    updateThemeButton(currentTheme);

    // Theme toggle button click handler
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeButton(newTheme);
        });
    }

    /**
     * Update theme button icon and text based on current theme.
     * 
     * @param {string} theme - The current theme ('light' or 'dark')
     */
    function updateThemeButton(theme) {
        if (theme === 'dark') {
            if (themeIcon) themeIcon.textContent = '☀️';
            if (themeText) themeText.textContent = 'Light';
        } else {
            if (themeIcon) themeIcon.textContent = '🌙';
            if (themeText) themeText.textContent = 'Dark';
        }
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add animation class to feature cards when they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe feature cards and other animated elements
    document.querySelectorAll('.feature-card, .resource-card, .example-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(card);
    });

    // Console message for developers
    console.log('%c🤖 GitHub Copilot Demo', 'font-size: 20px; font-weight: bold; color: #0969da;');
    console.log('%cThis project was built with GitHub Copilot assistance!', 'font-size: 14px; color: #57606a;');
    console.log('%cCheck out the source code: https://github.com/agharib89/gh-copilot-raisa', 'font-size: 12px; color: #0969da;');
});
