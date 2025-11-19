"""
Example Python module demonstrating project standards.

This module serves as a template for creating new modules following
the project's coding conventions and best practices.
"""

from typing import List, Optional


def greet(name: str, greeting: Optional[str] = None) -> str:
    """
    Generate a greeting message.

    Args:
        name: The name of the person to greet.
        greeting: Optional custom greeting. Defaults to "Hello".

    Returns:
        A formatted greeting message.

    Raises:
        ValueError: If name is empty or contains only whitespace.

    Example:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("Bob", "Hi")
        'Hi, Bob!'
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    greeting_text = greeting if greeting else "Hello"
    return f"{greeting_text}, {name}!"


def sum_numbers(numbers: List[int]) -> int:
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers: List of integers to sum.

    Returns:
        The sum of all numbers in the list.

    Example:
        >>> sum_numbers([1, 2, 3, 4, 5])
        15
        >>> sum_numbers([])
        0
    """
    return sum(numbers)


class Person:
    """
    Represents a person with a name and age.

    Attributes:
        name: The person's name.
        age: The person's age in years.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person instance.

        Args:
            name: The person's name.
            age: The person's age.

        Raises:
            ValueError: If age is negative.
        """
        if age < 0:
            raise ValueError("Age cannot be negative")

        self.name = name
        self.age = age

    def introduce(self) -> str:
        """
        Generate a self-introduction.

        Returns:
            A formatted introduction string.

        Example:
            >>> person = Person("Alice", 30)
            >>> person.introduce()
            'Hi, I am Alice and I am 30 years old.'
        """
        return f"Hi, I am {self.name} and I am {self.age} years old."
