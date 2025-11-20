"""
Route handlers for the GitHub Copilot demonstration application.

This module defines all the routes and their handlers for the Flask
application, including pages for home, resources, examples, and about.
"""

from typing import Any, Dict, List

from flask import Flask, render_template


def register_routes(app: Flask) -> None:
    """
    Register all application routes.

    Args:
        app: Flask application instance.
    """

    @app.route("/")
    def home() -> str:
        """
        Render the home page.

        Returns:
            Rendered home page template.
        """
        return render_template(
            "home.html",
            title="GitHub Copilot Demo",
            active_page="home",
        )

    @app.route("/resources")
    def resources() -> str:
        """
        Render the resources page with learning materials.

        Returns:
            Rendered resources page template.
        """
        learning_resources = get_learning_resources()
        return render_template(
            "resources.html",
            title="Learning Resources",
            active_page="resources",
            resources=learning_resources,
        )

    @app.route("/examples")
    def examples() -> str:
        """
        Render the examples page showcasing Copilot features.

        Returns:
            Rendered examples page template.
        """
        copilot_examples = get_copilot_examples()
        return render_template(
            "examples.html",
            title="Copilot Examples",
            active_page="examples",
            examples=copilot_examples,
        )

    @app.route("/about")
    def about() -> str:
        """
        Render the about page.

        Returns:
            Rendered about page template.
        """
        return render_template(
            "about.html",
            title="About This Project",
            active_page="about",
        )

    @app.route("/author")
    def author() -> str:
        """
        Render the author page with information about Raisa Energy.

        Returns:
            Rendered author page template.
        """
        return render_template(
            "author.html",
            title="About the Author",
            active_page="author",
        )

    @app.route("/tutorials")
    def tutorials() -> str:
        """
        Render the tutorials page with customization guides.

        Returns:
            Rendered tutorials page template.
        """
        return render_template(
            "tutorials.html",
            title="Customization Tutorials",
            active_page="tutorials",
        )

    @app.route("/copilot-integration")
    def copilot_integration() -> str:
        """
        Render the Copilot integration page with setup guides and prompts.

        Returns:
            Rendered copilot-integration page template.
        """
        return render_template(
            "copilot-integration.html",
            title="Use with GitHub Copilot",
            active_page="copilot-integration",
        )


def get_learning_resources() -> Dict[str, List[Dict[str, Any]]]:
    """
    Get categorized GitHub Copilot learning resources.

    Returns:
        Dictionary of resource categories with lists of resources.
    """
    return {
        "documentation": [
            {
                "title": "GitHub Copilot Documentation",
                "description": (
                    "Comprehensive documentation for GitHub Copilot, "
                    "covering usage, integration, and best practices"
                ),
                "url": "https://docs.github.com/copilot",
                "cost": "Free",
            },
            {
                "title": "GitHub Copilot in VS Code",
                "description": (
                    "Official documentation for using GitHub Copilot in "
                    "Visual Studio Code, including advanced features"
                ),
                "url": "https://code.visualstudio.com/docs/copilot/overview",
                "cost": "Free",
            },
            {
                "title": "GitHub Copilot Quickstart",
                "description": (
                    "Quick start guide to get up and running with "
                    "GitHub Copilot in minutes"
                ),
                "url": "https://docs.github.com/en/copilot/quickstart",
                "cost": "Free",
            },
            {
                "title": "GitHub Copilot Chat Documentation",
                "description": (
                    "Documentation for GitHub Copilot Chat features "
                    "across different environments"
                ),
                "url": "https://docs.github.com/en/copilot/github-copilot-chat",
                "cost": "Free",
            },
            {
                "title": "GitHub Copilot CLI Documentation",
                "description": (
                    "Guide to using GitHub Copilot in the command "
                    "line interface"
                ),
                "url": (
                    "https://docs.github.com/en/copilot/"
                    "github-copilot-in-the-cli"
                ),
                "cost": "Free",
            },
        ],
        "getting_started": [
            {
                "title": "Essentials of GitHub Copilot",
                "description": (
                    "A learning pathway covering the basics of GitHub "
                    "Copilot, including common questions and expert insights"
                ),
                "url": (
                    "https://resources.github.com/learn/pathways/copilot/"
                    "essentials/essentials-of-github-copilot/"
                ),
                "cost": "Free",
            },
            {
                "title": "Getting Started with GitHub Copilot",
                "description": (
                    "Step-by-step tutorials for beginners to unlock the "
                    "full potential of GitHub Copilot"
                ),
                "url": "https://github.com/features/copilot/tutorials",
                "cost": "Free",
            },
            {
                "title": "GitHub Copilot Learning Pathways",
                "description": (
                    "Expert-guided learning pathways for AI-powered "
                    "development with GitHub Copilot"
                ),
                "url": "https://resources.github.com/learn/pathways/",
                "cost": "Free",
            },
        ],
        "microsoft_learn": [
            {
                "title": "GitHub Copilot Fundamentals (Microsoft Learn)",
                "description": (
                    "Official Microsoft training modules on GitHub Copilot "
                    "fundamentals, productivity, and business use cases"
                ),
                "url": "https://learn.microsoft.com/en-us/training/paths/copilot/",
                "platform": "Microsoft Learn",
                "level": "Beginner to Intermediate",
                "cost": "Free",
            },
            {
                "title": "Generate Documentation Using GitHub Copilot Tools",
                "description": (
                    "Intermediate module on using Copilot Chat for code "
                    "explanations and documentation"
                ),
                "url": (
                    "https://learn.microsoft.com/en-us/training/modules/"
                    "generate-documentation-using-github-copilot-tools/"
                ),
                "platform": "Microsoft Learn",
                "level": "Intermediate",
                "cost": "Free",
            },
        ],
        "courses": [
            {
                "title": "Boost Your Productivity with GitHub Copilot",
                "description": (
                    "Beginner-level course covering setup, prompt "
                    "engineering, and best practices for GitHub Copilot"
                ),
                "url": "https://www.coursera.org/learn/introduction-to-github-copilot",
                "platform": "Coursera",
                "level": "Beginner",
                "cost": "Free (with paid certificate)",
            },
            {
                "title": "Introduction to GitHub Copilot",
                "description": (
                    "Intermediate course covering setup, database "
                    "integration, and real-world scenarios"
                ),
                "url": (
                    "https://www.coursera.org/learn/"
                    "introduction-to-microsoft-github-copilot"
                ),
                "platform": "Coursera",
                "level": "Intermediate",
                "cost": "Free (with paid certificate)",
            },
            {
                "title": "GitHub Copilot: The AI Pair Programmer for Coding",
                "description": (
                    "Short course on AI-assisted programming and best "
                    "practices with GitHub Copilot"
                ),
                "url": (
                    "https://www.coursera.org/learn/"
                    "github-copilot-the-ai-pair-programmer-for-coding"
                ),
                "platform": "Coursera",
                "level": "Beginner",
                "cost": "Free (with paid certificate)",
            },
        ],
        "videos": [
            {
                "title": "Introduction to GitHub Copilot Tutorial",
                "description": (
                    "Beginner-friendly video tutorial covering "
                    "installation, usage, and productivity tips"
                ),
                "url": "https://www.youtube.com/watch?v=2pFPJYdPM7Q",
                "platform": "YouTube",
                "cost": "Free",
            },
            {
                "title": "First Hour with GitHub Copilot",
                "description": (
                    "Practical walkthrough of Copilot features, prompt "
                    "best practices, and code completion"
                ),
                "url": "https://www.youtube.com/watch?v=7GtrNVoJatE",
                "platform": "YouTube",
                "cost": "Free",
            },
            {
                "title": "How to Use GitHub Copilot (Complete Beginner's Guide)",
                "description": (
                    "In-depth beginner's guide covering prompt "
                    "engineering, security, and practical coding examples"
                ),
                "url": "https://www.youtube.com/watch?v=SJqGYwRq0uc",
                "platform": "YouTube",
                "cost": "Free",
            },
            {
                "title": "Coding with an AI Pair Programmer: Getting Started",
                "description": (
                    "Introduction to GitHub Copilot mechanics, data "
                    "handling, and workflow adaptation"
                ),
                "url": "https://www.youtube.com/watch?v=dhfTaSGYQ4o",
                "platform": "YouTube",
                "cost": "Free",
            },
            {
                "title": "GitHub YouTube Channel",
                "description": (
                    "Official GitHub YouTube channel with Copilot "
                    "tutorials and announcements"
                ),
                "url": "https://www.youtube.com/@GitHub",
                "platform": "YouTube",
                "cost": "Free",
            },
        ],
        "certification": [
            {
                "title": "GitHub Copilot Certification Study Guide",
                "description": (
                    "Official study guide and resources for preparing "
                    "for the GitHub Copilot certification exam"
                ),
                "url": "https://learn.github.com/certification/COPILOT",
                "cost": "Free",
            },
            {
                "title": (
                    "Free Official Learning Resources for Copilot Certification"
                ),
                "description": (
                    "Comprehensive guide to official resources, modules, "
                    "and exam preparation for GitHub Copilot certification"
                ),
                "url": (
                    "https://dellenny.com/free-official-learning-resources"
                    "-for-the-github-copilot-certification-exam/"
                ),
                "cost": "Free",
            },
        ],
        "community": [
            {
                "title": "GitHub Copilot Community Discussions",
                "description": (
                    "Official community forum for GitHub Copilot "
                    "discussions, questions, and feedback"
                ),
                "url": (
                    "https://github.com/orgs/community/discussions/"
                    "categories/copilot"
                ),
                "cost": "Free",
            },
            {
                "title": "Awesome GitHub Copilot",
                "description": (
                    "Curated list of GitHub Copilot resources, projects, "
                    "and extensions"
                ),
                "url": "https://github.com/github/awesome-copilot/tree/main",
                "cost": "Free",
            },

        ],
        "best_practices": [
            {
                "title": "How to write better prompts for GitHub Copilot",
                "description": (
                    "Learn best practices for crafting effective prompts "
                    "to get better results from Copilot"
                ),
                "url": (
                    "https://github.blog/2023-06-20-how-to-write-better"
                    "-prompts-for-github-copilot/"
                ),
                "cost": "Free",
            },
            {
                "title": "GitHub Copilot Best Practices",
                "description": (
                    "Official best practices for using GitHub Copilot "
                    "effectively"
                ),
                "url": (
                    "https://docs.github.com/en/copilot/using-github-copilot/"
                    "getting-started-with-github-copilot"
                    "#best-practices-for-using-github-copilot"
                ),
                "cost": "Free",
            },
        ],
    }


def get_copilot_examples() -> List[Dict[str, Any]]:
    """
    Get list of GitHub Copilot feature examples.

    Returns:
        List of dictionaries containing example information.
    """
    return [
        {
            "title": "Code Completion",
            "description": "Copilot suggests code completions as you type",
            "features": [
                "Context-aware suggestions",
                "Multiple language support",
                "Function and class generation",
            ],
        },
        {
            "title": "Documentation Generation",
            "description": "Generate docstrings and comments automatically",
            "features": [
                "PEP 257 compliant docstrings",
                "Parameter descriptions",
                "Return value documentation",
            ],
        },
        {
            "title": "Test Generation",
            "description": "Create comprehensive test cases with pytest",
            "features": [
                "Unit test generation",
                "Edge case coverage",
                "Fixture creation",
            ],
        },
        {
            "title": "Code Refactoring",
            "description": "Refactor existing code following best practices",
            "features": [
                "Function extraction",
                "Variable renaming",
                "Code optimization",
            ],
        },
        {
            "title": "Bug Fixing",
            "description": "Identify and fix bugs with Copilot assistance",
            "features": [
                "Error analysis",
                "Solution suggestions",
                "Error handling improvements",
            ],
        },
        {
            "title": "Code Translation",
            "description": "Convert code between different languages",
            "features": [
                "Multi-language support",
                "Idiom preservation",
                "Best practices application",
            ],
        },
    ]
