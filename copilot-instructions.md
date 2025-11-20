# GitHub Copilot Instructions

## Repository Purpose

This is a Python Flask web application that demonstrates GitHub Copilot capabilities with comprehensive instructions, prompts, and agents for Python development. It serves as a reference implementation for setting up GitHub Copilot in Python projects.

## Project Structure

```
gh-copilot-raisa/
├── src/                    # Source code
│   ├── app.py             # Main Flask application
│   ├── routes.py          # Route handlers
│   ├── example.py         # Example module with utilities
│   ├── templates/         # Jinja2 HTML templates
│   └── static/            # Static assets (CSS, JS)
├── tests/                 # Test files
│   ├── test_app.py        # Flask application tests
│   └── test_example.py    # Example module tests
├── .github/               # GitHub configurations
│   ├── copilot-instructions.md  # Detailed Copilot instructions
│   ├── instructions/      # Language-specific guidelines
│   ├── prompts/          # Reusable prompts
│   ├── agents/           # Specialized agents
│   └── workflows/        # GitHub Actions workflows
├── requirements.txt       # Production dependencies
└── requirements-dev.txt   # Development dependencies
```

## How to Build

This project uses Python 3.11+ with Flask. To set up the development environment:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## How to Test

The project uses pytest as the testing framework:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html --cov-report=term

# Run specific test file
pytest tests/test_app.py

# Run tests with verbose output
pytest -v
```

## How to Lint

Code quality is maintained using flake8:

```bash
# Run flake8 linter
flake8 src tests

# Check for critical errors only
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Run full linting with statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## Coding Conventions

This project follows Python best practices:

- **Style Guide**: PEP 8 (Python Enhancement Proposal 8)
- **Docstrings**: PEP 257 conventions with Google/NumPy style
- **Type Hints**: Required for all function parameters and return values
- **Line Length**: Maximum 79 characters (120 for comments/docstrings)
- **Indentation**: 4 spaces (no tabs)
- **Testing**: Pytest framework with aim for 80%+ code coverage
- **Imports**: Organized with isort, grouped by stdlib, third-party, local

### Key Principles

1. **Type Safety**: Use type hints from the `typing` module
2. **Documentation**: All public modules, classes, and functions must have docstrings
3. **Testing**: Write tests for all new features and bug fixes
4. **Error Handling**: Use specific exceptions, provide meaningful error messages
5. **Security**: Never hardcode secrets, validate all inputs, use parameterized queries

## Detailed Instructions

For comprehensive coding guidelines, refer to:

- **Python Guidelines**: `.github/instructions/python.instructions.md`
- **Testing Standards**: `.github/instructions/testing.instructions.md`
- **Security Best Practices**: `.github/instructions/security.instructions.md`
- **Documentation Requirements**: `.github/instructions/documentation.instructions.md`
- **Performance Optimization**: `.github/instructions/performance.instructions.md`
- **Code Review Standards**: `.github/instructions/code-review.instructions.md`

## Reusable Prompts

The `.github/prompts/` directory contains prompts for common tasks:

- `setup-component.prompt.md` - Create new Python modules
- `write-tests.prompt.md` - Generate test cases
- `code-review.prompt.md` - Perform code reviews
- `refactor-code.prompt.md` - Refactor existing code
- `generate-docs.prompt.md` - Generate documentation
- `debug-issue.prompt.md` - Debug and fix issues

## Specialized Agents

The `.github/agents/` directory contains specialized agents:

- `architect.agent.md` - Architecture planning and design
- `reviewer.agent.md` - Code review mode
- `debugger.agent.md` - Debugging assistance

## Development Workflow

1. Create a new branch for your feature or fix
2. Follow the coding conventions and guidelines
3. Write tests for new functionality
4. Run linter and tests before committing
5. Ensure all checks pass in CI/CD
6. Submit a pull request for review

## CI/CD

The project uses GitHub Actions for continuous integration:

- **Workflow**: `.github/workflows/copilot-setup-steps.yml`
- **Triggers**: Manual dispatch, workflow file changes, pull requests
- **Jobs**: Setup Python → Install dependencies → Run linter → Run tests

## Important Notes

- All code changes should be minimal and focused
- Update documentation when adding new features
- Never commit secrets or sensitive data
- Follow the principle of least surprise
- Prioritize readability over cleverness

## Dependencies

- **Flask**: Web framework for the application
- **pytest**: Testing framework
- **flake8**: Code linting and style checking
- **pytest-cov**: Coverage reporting for tests

For the complete list, see `requirements.txt` and `requirements-dev.txt`.
