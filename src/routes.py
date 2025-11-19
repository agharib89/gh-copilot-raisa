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


def get_learning_resources() -> List[Dict[str, Any]]:
    """
    Get list of GitHub Copilot learning resources.

    Returns:
        List of dictionaries containing resource information.
    """
    return [
        {
            "title": "GitHub Copilot Documentation",
            "description": "Official documentation for GitHub Copilot",
            "url": "https://docs.github.com/en/copilot",
            "category": "Official Docs",
        },
        {
            "title": "Getting Started with Copilot",
            "description": "Quick start guide for GitHub Copilot",
            "url": "https://docs.github.com/en/copilot/quickstart",
            "category": "Getting Started",
        },
        {
            "title": "Copilot Best Practices",
            "description": (
                "Learn best practices for using GitHub Copilot "
                "effectively"
            ),
            "url": (
                "https://github.blog/2023-06-20-how-to-write-better"
                "-prompts-for-github-copilot/"
            ),
            "category": "Best Practices",
        },
        {
            "title": "Copilot Chat",
            "description": (
                "Using GitHub Copilot Chat for interactive "
                "assistance"
            ),
            "url": (
                "https://docs.github.com/en/copilot/"
                "github-copilot-chat"
            ),
            "category": "Features",
        },
        {
            "title": "Copilot for Business",
            "description": (
                "Information about GitHub Copilot for organizations"
            ),
            "url": (
                "https://docs.github.com/en/copilot/"
                "overview-of-github-copilot/"
                "about-github-copilot-for-business"
            ),
            "category": "Enterprise",
        },
        {
            "title": "Awesome Copilot",
            "description": (
                "Curated list of GitHub Copilot resources and "
                "examples"
            ),
            "url": "https://github.com/github/awesome-copilot",
            "category": "Community",
        },
    ]


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
