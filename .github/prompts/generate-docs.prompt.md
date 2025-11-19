---
agent: 'agent'
model: Claude Sonnet 4.5
tools: ['edit', 'search/codebase']
description: 'Generate comprehensive documentation for Python code'
---

# Documentation Generation

Your goal is to generate comprehensive, clear documentation for Python code following PEP 257 and project standards.

## Information Required

Ask for the following if not provided:
- Target module, class, or function to document
- Documentation type needed (docstrings, README, API docs)
- Audience level (beginner, intermediate, expert)

## Documentation Types

### 1. Docstrings

Generate PEP 257 compliant docstrings:

**Module Docstrings**:
- Brief description of module purpose
- Main components and functionality
- Usage examples if applicable

**Function/Method Docstrings**:
- Brief description of functionality
- Args section with parameter descriptions
- Returns section describing return value
- Raises section for exceptions
- Examples for complex functions

**Class Docstrings**:
- Purpose and responsibility
- Attributes section
- Usage examples
- Related classes or modules

### 2. README Documentation

Generate or update README.md:
- Project overview and purpose
- Installation instructions
- Quick start guide
- Usage examples
- Configuration options
- API reference links
- Contributing guidelines
- License information

### 3. API Documentation

Generate API documentation:
- Endpoint descriptions (for web APIs)
- Request/response formats
- Authentication requirements
- Error codes and handling
- Usage examples

## Docstring Format

Use Google or NumPy style consistently:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief one-line description.

    More detailed explanation of what the function does,
    including any important behaviors or side effects.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of the return value.

    Raises:
        ValueError: When param1 is empty.
        TypeError: When param2 is not an integer.

    Example:
        >>> function_name("test", 42)
        True
    """
```

## Documentation Requirements

1. **Clarity**: Use clear, concise language
2. **Completeness**: Cover all parameters, returns, and exceptions
3. **Accuracy**: Ensure documentation matches implementation
4. **Examples**: Include usage examples for complex functionality
5. **Formatting**: Use proper Markdown and RST formatting

## Best Practices

- Write documentation as you write code
- Keep docs in sync with code changes
- Use type hints to supplement documentation
- Avoid redundant information
- Focus on the "why" not just the "what"
- Include common pitfalls and gotchas
- Link to related documentation

## Documentation Checklist

- [ ] All public modules have module docstrings
- [ ] All public classes have class docstrings
- [ ] All public functions/methods have docstrings
- [ ] Parameters are documented with types and descriptions
- [ ] Return values are documented
- [ ] Exceptions are documented
- [ ] Examples are provided for complex functionality
- [ ] README is comprehensive and up-to-date
- [ ] Code comments explain complex logic

## Special Cases

### Complex Algorithms
- Explain the approach and time/space complexity
- Provide references to resources or papers
- Include step-by-step explanation

### Configuration
- Document all configuration options
- Provide examples and default values
- Explain the impact of each setting

### Dependencies
- Document external dependencies and their purpose
- Specify version requirements
- Explain installation steps

## Deliverables

1. Complete docstrings for all specified code
2. Updated README if requested
3. API documentation if applicable
4. Examples demonstrating usage
5. Any additional documentation files needed
