---
description: 'Python testing standards and practices'
applyTo: '**/test_*.py,**/*_test.py,**/tests/**/*.py'
---

# Python Testing Standards

## Testing Framework

- Use `pytest` as the primary testing framework.
- Organize tests in a `tests/` directory mirroring the source structure.
- Name test files with `test_` prefix or `_test` suffix.

## Test Structure

- Follow the Arrange-Act-Assert (AAA) pattern.
- Use descriptive test function names that explain what is being tested.
- Group related tests using test classes or pytest markers.
- Keep tests focused - one test should verify one behavior.

## Test Coverage

- Aim for at least 80% code coverage.
- Focus on testing critical business logic and edge cases.
- Write tests for both success and failure scenarios.
- Test error handling and exception cases.

## Fixtures and Mocking

- Use pytest fixtures for test setup and teardown.
- Leverage `@pytest.fixture` for reusable test components.
- Use `unittest.mock` or `pytest-mock` for mocking external dependencies.
- Mock external API calls, database connections, and file I/O.

## Assertions

- Use clear, specific assertions that provide meaningful error messages.
- Prefer pytest's rich assertion introspection over custom assertion methods.
- Use `pytest.raises()` for testing exceptions.
- Use `pytest.approx()` for floating-point comparisons.

## Test Organization

- Group tests by functionality or module.
- Use `conftest.py` for shared fixtures across test modules.
- Separate unit tests, integration tests, and end-to-end tests.
- Use pytest markers to categorize tests (e.g., `@pytest.mark.slow`).

## Best Practices

- Tests should be independent and not rely on execution order.
- Avoid testing implementation details - focus on behavior.
- Keep tests simple and easy to understand.
- Run tests frequently during development.
- Ensure tests are deterministic and reproducible.

## Parameterized Testing

- Use `@pytest.mark.parametrize` for testing multiple input scenarios.
- Provide clear parameter names that describe the test case.
- Use descriptive IDs for parameterized test cases.

## Documentation

- Add docstrings to test functions explaining what is being tested.
- Document any non-obvious test setup or assumptions.
- Include comments for complex test scenarios or edge cases.
