---
agent: 'agent'
model: Claude Sonnet 4.5
tools: ['codebase']
description: 'Create a new Python module with proper structure'
---

# Python Module Setup

Your goal is to create a new Python module following project conventions and best practices.

## Information Required

Ask for the following if not provided:
- Module name and purpose
- Expected functionality
- Dependencies needed

## Module Structure

Create the module with:
- Proper file and directory structure
- `__init__.py` file if creating a package
- Type hints for all function parameters and return values
- PEP 257 compliant docstrings
- Error handling for common edge cases

## Requirements

1. **Code Style**:
   - Follow PEP 8 guidelines
   - Use 4 spaces for indentation
   - Keep lines under 79 characters
   - Use descriptive variable and function names

2. **Documentation**:
   - Module-level docstring explaining purpose
   - Function docstrings with Args, Returns, and Raises sections
   - Inline comments for complex logic

3. **Type Safety**:
   - Type hints for all parameters and return values
   - Use `typing` module for complex types
   - Use `Optional` for nullable parameters

4. **Testing**:
   - Create corresponding test file in `tests/` directory
   - Include basic test cases for main functionality
   - Use pytest framework

5. **Best Practices**:
   - Single Responsibility Principle
   - Proper error handling with specific exceptions
   - Use context managers for resource management
   - Follow existing project patterns

## Example Structure

For a module named `user_service`:
- `src/user_service.py` - Main module code
- `tests/test_user_service.py` - Test file
- Add necessary imports to `src/__init__.py`

## Deliverables

1. Main module file with complete implementation
2. Test file with test cases
3. Updated `__init__.py` if applicable
4. Brief usage example in docstring
