"""
Shared pytest fixtures for the test suite.

This file contains fixtures that are automatically available
to all test files.
"""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "name": "Test User",
        "age": 30,
        "email": "test@example.com"
    }


@pytest.fixture
def number_list():
    """Provide a sample list of numbers."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
