"""
Test suite for the example module.

This test file demonstrates testing best practices using pytest.
"""

import pytest
from src.example import greet, sum_numbers, Person


class TestGreet:
    """Tests for the greet function."""

    def test_greet_default_greeting(self):
        """Test that greet uses default greeting when none provided."""
        result = greet("Alice")
        assert result == "Hello, Alice!"

    def test_greet_custom_greeting(self):
        """Test that greet uses custom greeting when provided."""
        result = greet("Bob", "Hi")
        assert result == "Hi, Bob!"

    def test_greet_empty_name_raises_error(self):
        """Test that greet raises ValueError for empty name."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    def test_greet_whitespace_name_raises_error(self):
        """Test that greet raises ValueError for whitespace-only name."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("   ")

    @pytest.mark.parametrize("name,greeting,expected", [
        ("Alice", None, "Hello, Alice!"),
        ("Bob", "Hi", "Hi, Bob!"),
        ("Charlie", "Hey", "Hey, Charlie!"),
    ])
    def test_greet_parametrized(self, name, greeting, expected):
        """Test greet with multiple parameter combinations."""
        result = greet(name, greeting)
        assert result == expected


class TestSumNumbers:
    """Tests for the sum_numbers function."""

    def test_sum_positive_numbers(self):
        """Test sum of positive numbers."""
        result = sum_numbers([1, 2, 3, 4, 5])
        assert result == 15

    def test_sum_empty_list(self):
        """Test sum of empty list returns zero."""
        result = sum_numbers([])
        assert result == 0

    def test_sum_negative_numbers(self):
        """Test sum with negative numbers."""
        result = sum_numbers([-1, -2, -3])
        assert result == -6

    def test_sum_mixed_numbers(self):
        """Test sum with mixed positive and negative numbers."""
        result = sum_numbers([10, -5, 3, -8])
        assert result == 0

    def test_sum_single_number(self):
        """Test sum with single number."""
        result = sum_numbers([42])
        assert result == 42


class TestPerson:
    """Tests for the Person class."""

    def test_person_initialization(self):
        """Test Person can be initialized with valid data."""
        person = Person("Alice", 30)
        assert person.name == "Alice"
        assert person.age == 30

    def test_person_negative_age_raises_error(self):
        """Test Person raises ValueError for negative age."""
        with pytest.raises(ValueError, match="Age cannot be negative"):
            Person("Bob", -1)

    def test_person_introduce(self):
        """Test Person.introduce returns correct introduction."""
        person = Person("Charlie", 25)
        result = person.introduce()
        assert result == "Hi, I am Charlie and I am 25 years old."

    def test_person_zero_age(self):
        """Test Person accepts zero as valid age."""
        person = Person("Baby", 0)
        assert person.age == 0

    @pytest.fixture
    def sample_person(self):
        """Fixture providing a sample Person instance."""
        return Person("Test User", 42)

    def test_person_with_fixture(self, sample_person):
        """Test Person using a fixture."""
        assert sample_person.name == "Test User"
        assert sample_person.age == 42
