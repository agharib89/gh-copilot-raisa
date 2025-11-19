"""
Test suite for the Flask application.

This test file demonstrates testing Flask routes and responses.
"""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from src.app import create_app


@pytest.fixture
def app() -> Flask:
    """
    Create and configure a test Flask application.

    Returns:
        Test Flask application instance.
    """
    app = create_app({"TESTING": True})
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    Create a test client for the Flask application.

    Args:
        app: Flask application fixture.

    Returns:
        Flask test client.
    """
    return app.test_client()


class TestRoutes:
    """Tests for application routes."""

    def test_home_page(self, client: FlaskClient) -> None:
        """Test that home page loads successfully."""
        response = client.get("/")
        assert response.status_code == 200
        assert b"GitHub Copilot Demo" in response.data

    def test_resources_page(self, client: FlaskClient) -> None:
        """Test that resources page loads successfully."""
        response = client.get("/resources")
        assert response.status_code == 200
        assert b"Learning Resources" in response.data

    def test_examples_page(self, client: FlaskClient) -> None:
        """Test that examples page loads successfully."""
        response = client.get("/examples")
        assert response.status_code == 200
        assert b"Copilot Examples" in response.data

    def test_about_page(self, client: FlaskClient) -> None:
        """Test that about page loads successfully."""
        response = client.get("/about")
        assert response.status_code == 200
        assert b"About This Project" in response.data

    def test_404_error(self, client: FlaskClient) -> None:
        """Test that 404 page is displayed for invalid routes."""
        response = client.get("/nonexistent")
        assert response.status_code == 404
        assert b"404" in response.data


class TestAppCreation:
    """Tests for application creation and configuration."""

    def test_create_app_default_config(self) -> None:
        """Test creating app with default configuration."""
        app = create_app()
        assert app is not None
        assert isinstance(app, Flask)
        assert app.config["SECRET_KEY"] is not None

    def test_create_app_with_config(self) -> None:
        """Test creating app with custom configuration."""
        test_config = {"TESTING": True, "DEBUG": False}
        app = create_app(test_config)
        assert app.config["TESTING"] is True
        assert app.config["DEBUG"] is False

    def test_app_has_routes(self, app: Flask) -> None:
        """Test that application has registered routes."""
        rules = [rule.rule for rule in app.url_map.iter_rules()]
        assert "/" in rules
        assert "/resources" in rules
        assert "/examples" in rules
        assert "/about" in rules


class TestResourcesData:
    """Tests for resources data functions."""

    def test_resources_page_contains_links(self, client: FlaskClient) -> None:
        """Test that resources page contains learning resource links."""
        response = client.get("/resources")
        assert response.status_code == 200
        assert b"docs.github.com" in response.data
        has_official = b"Official" in response.data
        has_getting_started = b"Getting Started" in response.data
        assert has_official or has_getting_started

    def test_examples_page_contains_features(
        self, client: FlaskClient
    ) -> None:
        """Test that examples page contains feature descriptions."""
        response = client.get("/examples")
        assert response.status_code == 200
        assert (
            b"Code Completion" in response.data
            or b"Documentation" in response.data
        )


class TestErrorHandlers:
    """Tests for error handlers."""

    def test_404_handler(self, client: FlaskClient) -> None:
        """Test 404 error handler returns correct template."""
        response = client.get("/this-route-does-not-exist")
        assert response.status_code == 404
        assert b"Page Not Found" in response.data or b"404" in response.data

    def test_404_has_home_link(self, client: FlaskClient) -> None:
        """Test that 404 page has link to home."""
        response = client.get("/invalid-route")
        assert response.status_code == 404
        assert b'href="/"' in response.data or b"Go Home" in response.data


class TestTemplateRendering:
    """Tests for template rendering."""

    def test_home_template_has_navigation(
        self, client: FlaskClient
    ) -> None:
        """Test that home page has navigation menu."""
        response = client.get("/")
        assert b"Resources" in response.data
        assert b"Examples" in response.data
        assert b"About" in response.data

    def test_resources_template_has_categories(
        self, client: FlaskClient
    ) -> None:
        """Test that resources page displays categories."""
        response = client.get("/resources")
        # Should have at least some category or resource title
        assert response.status_code == 200
        # Check for common category terms or structure
        assert (
            b"Official" in response.data
            or b"Getting Started" in response.data
            or b"Best Practices" in response.data
        )

    def test_examples_template_has_examples(
        self, client: FlaskClient
    ) -> None:
        """Test that examples page displays example cards."""
        response = client.get("/examples")
        assert response.status_code == 200
        # Check for example-related content
        assert (
            b"feature" in response.data.lower()
            or b"example" in response.data.lower()
        )
