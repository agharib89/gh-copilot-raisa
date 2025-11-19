"""
Tests for resources.html template.

This module tests the HTML structure and content of the resources page
to ensure all required sections and resources are present.
"""

from pathlib import Path

import pytest


def get_resources_html_path() -> Path:
    """
    Get the path to the resources.html file.

    Returns:
        Path object pointing to resources.html.
    """
    return (
        Path(__file__).parent.parent
        / "src" / "templates" / "resources.html"
    )


def read_html_file(file_path: Path) -> str:
    """
    Read and return the contents of an HTML file.

    Args:
        file_path: Path to the HTML file.

    Returns:
        Contents of the HTML file as a string.

    Raises:
        FileNotFoundError: If the file doesn't exist.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"HTML file not found: {file_path}")

    return file_path.read_text(encoding='utf-8')


class TestResourcesHTML:
    """Test suite for resources.html template."""

    def test_resources_html_exists(self):
        """Test that resources.html file exists."""
        html_path = get_resources_html_path()
        assert html_path.exists(), (
            f"resources.html should exist at {html_path}"
        )

    def test_html_has_doctype(self):
        """Test that HTML file has DOCTYPE declaration."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        assert "<!DOCTYPE html>" in content, (
            "HTML should have DOCTYPE declaration"
        )

    def test_html_has_community_projects_section(self):
        """Test that HTML has Community Projects section."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        assert "Community Projects" in content, (
            "HTML should contain 'Community Projects' section"
        )

    def test_awesome_copilot_resource_exists(self):
        """Test that Awesome Copilot resource is present."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        assert "Awesome Copilot" in content, (
            "HTML should contain 'Awesome Copilot' resource"
        )

    def test_awesome_copilot_url(self):
        """Test that Awesome Copilot URL is correct."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        expected_url = "https://github.com/github/awesome-copilot"
        assert expected_url in content, (
            f"HTML should contain URL: {expected_url}"
        )

    def test_awesome_copilot_description(self):
        """Test that Awesome Copilot has the correct description."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        description_keywords = [
            "curated list",
            "GitHub Copilot",
            "official documentation",
            "community tutorials",
            "third-party integrations",
            "best practice collections"
        ]
        for keyword in description_keywords:
            assert keyword in content, (
                f"Description should contain '{keyword}'"
            )

    def test_html_structure_tags(self):
        """Test that HTML has proper structure tags."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)

        required_tags = [
            "<html",
            "<head>",
            "<body>",
            "</html>",
            "</head>",
            "</body>"
        ]

        for tag in required_tags:
            assert tag in content, f"HTML should contain {tag}"

    def test_community_projects_section_id(self):
        """Test that Community Projects section has the correct ID."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        assert 'id="community-projects"' in content, (
            "Section should have id='community-projects'"
        )

    def test_resource_has_proper_structure(self):
        """Test that resource has proper HTML structure with class."""
        html_path = get_resources_html_path()
        content = read_html_file(html_path)
        assert 'class="resource"' in content, (
            "Resource should have class='resource'"
        )


@pytest.mark.parametrize("tag", ["h1", "h2", "h3", "section", "div", "a", "p"])
def test_html_contains_semantic_tags(tag: str):
    """
    Test that HTML uses semantic tags.

    Args:
        tag: HTML tag to check for.
    """
    html_path = get_resources_html_path()
    content = read_html_file(html_path)
    assert f"<{tag}" in content, f"HTML should use <{tag}> tags"
