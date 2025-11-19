# Contributing to the Project

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. Create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details (Python version, OS, etc.)
   - Any relevant error messages or logs

### Suggesting Enhancements

1. Check if the enhancement has already been suggested
2. Create a new issue with:
   - Clear, descriptive title
   - Detailed description of the proposed feature
   - Use cases and benefits
   - Any relevant examples or mockups

### Pull Requests

1. **Fork the repository**

2. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Follow coding standards**

   - Read `.github/instructions/python.instructions.md`
   - Follow PEP 8 style guide
   - Use type hints
   - Write docstrings following PEP 257
   - Keep functions small and focused

4. **Write tests**

   - Add tests for new functionality
   - Ensure tests pass: `pytest`
   - Maintain or improve code coverage
   - Follow testing guidelines in `.github/instructions/testing.instructions.md`

5. **Update documentation**

   - Update docstrings
   - Update README if needed
   - Add entry to CHANGELOG.md
   - Update relevant instruction files

6. **Run quality checks**

   ```bash
   # Format code
   black src tests
   isort src tests

   # Lint code
   flake8 src tests

   # Type check
   mypy src

   # Run tests
   pytest --cov=src

   # Check security
   pip-audit
   ```

7. **Commit your changes**

   - Write clear, descriptive commit messages
   - Follow conventional commits format:

     ```
     type(scope): subject

     body

     footer
     ```

   - Types: feat, fix, docs, style, refactor, test, chore

   Example:

   ```
   feat(auth): add JWT authentication

   - Implement token generation
   - Add token validation
   - Create authentication middleware

   Closes #123
   ```

8. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request**
   - Use a clear, descriptive title
   - Reference related issues
   - Describe what changes were made and why
   - Include any breaking changes
   - Add screenshots for UI changes

### Pull Request Review Process

1. **Automated checks**

   - CI workflow must pass
   - Code coverage should not decrease
   - Linting and type checks must pass

2. **Code review**

   - At least one approval required
   - Address all review comments
   - Update code based on feedback

3. **Merge**
   - Squash commits if needed
   - Update CHANGELOG.md
   - Delete feature branch after merge

## Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/agharib89/gh-copilot-raisa.git
   cd gh-copilot-raisa
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Run tests**
   ```bash
   pytest
   ```

## Coding Guidelines

### Python Code

- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for all public APIs
- Keep functions under 50 lines when possible
- Maximum line length: 79 characters
- Use meaningful variable names

### Testing

- Write tests for all new features
- Aim for at least 80% code coverage
- Use descriptive test names
- Follow Arrange-Act-Assert pattern
- Mock external dependencies

### Documentation

- Update docstrings with code changes
- Keep README.md current
- Document breaking changes
- Add examples for complex features
- Update CHANGELOG.md

### Git Workflow

- Keep commits atomic and focused
- Write descriptive commit messages
- Rebase feature branches on main
- Squash commits before merging
- Keep commit history clean

## Using GitHub Copilot

When contributing, leverage the GitHub Copilot features:

- Use `#write-tests` to generate test cases
- Use `@reviewer` to review your changes before submitting
- Use `#generate-docs` to create documentation
- Use `@architect` to plan complex features

## Questions?

If you have questions:

- Open a discussion on GitHub
- Check existing issues and discussions
- Review the setup guide (SETUP_GUIDE.md)
- Consult instruction files in `.github/instructions/`

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🎉
