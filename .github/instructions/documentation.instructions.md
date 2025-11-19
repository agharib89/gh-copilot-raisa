---
description: 'Documentation requirements and standards'
applyTo: '**/*.py,**/*.md'
---

# Documentation Standards

## Code Documentation

- Follow PEP 257 docstring conventions for all Python code.
- Include docstrings for all public modules, classes, functions, and methods.
- Use the Google or NumPy docstring style for consistency.

## Docstring Structure

### Functions and Methods

```
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief description of what the function does.

    More detailed explanation if needed, including any important
    implementation details or usage notes.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of the return value.

    Raises:
        ExceptionType: Description of when this exception is raised.
    """
```

### Classes

```
class ClassName:
    """
    Brief description of the class.

    More detailed explanation of the class purpose, usage,
    and any important attributes or behaviors.

    Attributes:
        attr1: Description of attr1.
        attr2: Description of attr2.
    """
```

## Module Documentation

- Include module-level docstring at the top of each file.
- Describe the module's purpose and main components.
- List any important constants or configuration.

## README Documentation

- Maintain a comprehensive README.md in the project root.
- Include: project overview, installation instructions, usage examples, and contribution guidelines.
- Keep the README up-to-date with project changes.

## API Documentation

- Document all public APIs with clear examples.
- Include parameter types, return values, and possible exceptions.
- Provide usage examples for complex APIs.

## Comments

- Use inline comments sparingly - only when code intent isn't clear.
- Focus on explaining "why" rather than "what".
- Keep comments up-to-date with code changes.
- Remove commented-out code before committing.

## Changelog

- Maintain a CHANGELOG.md following Keep a Changelog format.
- Document all notable changes, bug fixes, and new features.
- Group changes by version and date.

## Best Practices

- Write documentation as you write code, not after.
- Use clear, concise language avoiding jargon where possible.
- Include examples for complex functionality.
- Keep documentation in sync with code changes.
- Use type hints to supplement documentation.
