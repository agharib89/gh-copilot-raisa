"""
Flask application to demonstrate GitHub Copilot capabilities.

This module sets up the Flask application with proper configuration
and integrates all routes for the GitHub Copilot demonstration.
"""

import os
from typing import Any, Dict

from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_app(config: Dict[str, Any] | None = None) -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config: Optional dictionary with configuration overrides.

    Returns:
        Configured Flask application instance.

    Example:
        >>> app = create_app()
        >>> app.run()
    """
    app = Flask(__name__)

    # Default configuration
    default_secret = "dev-secret-key-change-in-production"
    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY", default_secret),
        DEBUG=os.getenv("FLASK_DEBUG", "False").lower() == "true",
        TESTING=False,
    )

    # Override with custom config if provided
    if config:
        app.config.update(config)

    # Register routes
    from routes import register_routes

    register_routes(app)

    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error: Any) -> tuple[str, int]:
        """Handle 404 errors."""
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(error: Any) -> tuple[str, int]:
        """Handle 500 errors."""
        return render_template("500.html"), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
    )
