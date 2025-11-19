<!-- Based on: https://github.com/github/awesome-copilot/blob/main/instructions/python.instructions.md -->
---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## Python Instructions

- Write clear and concise comments for each function.
- Ensure functions have descriptive names and include type hints.
- Provide docstrings following PEP 257 conventions.
- Use the `typing` module for type annotations (e.g., `List[str]`, `Dict[str, int]`).
- Break down complex functions into smaller, more manageable functions.

## General Instructions

- Always prioritize readability and clarity.
- For algorithm-related code, include explanations of the approach used.
- Write code with good maintainability practices, including comments on why certain design decisions were made.
- Handle edge cases and write clear exception handling.
- For libraries or external dependencies, mention their usage and purpose in comments.
- Use consistent naming conventions and follow language-specific best practices.
- Write concise, efficient, and idiomatic code that is also easily understandable.

## Code Style and Formatting

- Follow the **PEP 8** style guide for Python.
- Maintain proper indentation (use 4 spaces for each level of indentation).
- Ensure lines do not exceed 79 characters.
- Place function and class docstrings immediately after the `def` or `class` keyword.
- Use blank lines to separate functions, classes, and code blocks where appropriate.

## Type Hints and Annotations

- Use type hints for function parameters and return values.
- Leverage the `typing` module for complex types (List, Dict, Optional, Union, etc.).
- Use `Optional[Type]` for parameters that can be None.
- Document type expectations in docstrings when type hints alone aren't sufficient.

## Error Handling

- Use specific exception types rather than catching generic exceptions.
- Provide meaningful error messages that help with debugging.
- Handle edge cases explicitly and document expected behavior.
- Use try-except blocks judiciously and avoid bare except clauses.

## Edge Cases and Testing

- Always include test cases for critical paths of the application.
- Account for common edge cases like empty inputs, invalid data types, and large datasets.
- Include comments for edge cases and the expected behavior in those cases.
- Write unit tests for functions and document them with docstrings explaining the test cases.

## Documentation Standards

- Follow PEP 257 for docstring conventions.
- Include Parameters, Returns, and Raises sections in docstrings.
- Document the purpose and behavior of functions and classes.
- Keep comments up-to-date with code changes.

## Best Practices

- Prefer list comprehensions and generator expressions for better readability and performance.
- Use context managers (with statements) for resource management.
- Follow the principle of least surprise - write code that behaves as expected.
- Use descriptive variable and function names that convey intent.
- Avoid magic numbers - use named constants instead.
