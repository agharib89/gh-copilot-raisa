---
agent: 'agent'
model: Claude Sonnet 4.5
tools: ['codebase']
description: 'Generate comprehensive test cases for Python code'
---

# Test Generation

Your goal is to generate comprehensive test cases for existing Python code using pytest.

## Information Required

Ask for the following if not provided:
- Target module or function to test
- Specific scenarios or edge cases to cover

## Test Requirements

1. **Test Framework**:
   - Use pytest as the testing framework
   - Place tests in `tests/` directory
   - Name test files with `test_` prefix

2. **Test Structure**:
   - Follow Arrange-Act-Assert (AAA) pattern
   - One test function per behavior
   - Use descriptive test function names
   - Group related tests in classes when appropriate

3. **Coverage**:
   - Test happy path scenarios
   - Test edge cases (empty inputs, None values, boundaries)
   - Test error conditions and exceptions
   - Test with various input types

4. **Fixtures and Mocking**:
   - Use pytest fixtures for test setup
   - Mock external dependencies (APIs, databases, file I/O)
   - Use `@pytest.fixture` for reusable components

5. **Assertions**:
   - Use clear, specific assertions
   - Provide meaningful failure messages
   - Use `pytest.raises()` for exception testing
   - Use `pytest.approx()` for floating-point comparisons

## Test Categories

Generate tests for:
- **Unit Tests**: Individual functions and methods
- **Edge Cases**: Boundary conditions, empty inputs, None values
- **Error Cases**: Invalid inputs, exception scenarios
- **Integration Tests**: Component interactions (if applicable)

## Best Practices

- Keep tests independent and isolated
- Tests should be deterministic
- Use parameterized tests with `@pytest.mark.parametrize`
- Add docstrings to test functions
- Mock external dependencies
- Ensure tests are fast and focused

## Example Test Structure

```python
def test_function_name_scenario():
    """Test that function_name handles scenario correctly."""
    # Arrange
    input_data = setup_test_data()

    # Act
    result = function_name(input_data)

    # Assert
    assert result == expected_output
```

## Deliverables

1. Complete test file with all test cases
2. Necessary fixtures in `conftest.py` if needed
3. Test documentation explaining test scenarios
4. Parameterized tests for multiple scenarios where applicable
