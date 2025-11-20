# Python Project with GitHub Copilot

A Python Flask application demonstrating GitHub Copilot capabilities with comprehensive instructions, prompts, and agents.

🌐 **Live Demo**: [https://copilot.agharib.com](https://copilot.agharib.com)

## 🚀 Quick Start

### View Online

Visit the live site at [https://copilot.agharib.com](https://copilot.agharib.com) to explore the GitHub Copilot resources and examples.

### Prerequisites

- Python 3.11 or higher
- Visual Studio Code with GitHub Copilot extension
- Git

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd gh-copilot-raisa
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running the Application Locally

#### Option 1: Static Site (Recommended)

Build and serve the static site:

```bash
# Build the static site
python build.py

# Serve locally (requires Python 3)
cd docs
python -m http.server 8000
```

Then open your browser and navigate to `http://localhost:8000/`

#### Option 2: Flask Development Server

Start the Flask development server:

```bash
python src/app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000`

The application provides:
- **Home Page** - Introduction to GitHub Copilot
- **Resources** - Curated learning resources
- **Examples** - Feature demonstrations
- **About** - Project information

## 📁 Project Structure

```
gh-copilot-raisa/
├── .github/
│   ├── copilot-instructions.md      # Main Copilot instructions
│   ├── instructions/                # Language-specific guidelines
│   │   ├── python.instructions.md
│   │   ├── testing.instructions.md
│   │   ├── security.instructions.md
│   │   ├── documentation.instructions.md
│   │   ├── performance.instructions.md
│   │   └── code-review.instructions.md
│   ├── prompts/                     # Reusable prompts
│   │   ├── setup-component.prompt.md
│   │   ├── write-tests.prompt.md
│   │   ├── code-review.prompt.md
│   │   ├── refactor-code.prompt.md
│   │   ├── generate-docs.prompt.md
│   │   └── debug-issue.prompt.md
│   ├── agents/                      # Specialized agents
│   │   ├── architect.agent.md
│   │   ├── reviewer.agent.md
│   │   └── debugger.agent.md
│   └── workflows/
│       └── copilot-setup-steps.yml  # CI/CD workflow
├── src/                             # Source code
│   ├── app.py                       # Flask application
│   ├── routes.py                    # Route handlers
│   ├── example.py                   # Example module
│   ├── templates/                   # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── resources.html
│   │   ├── examples.html
│   │   ├── about.html
│   │   ├── 404.html
│   │   └── 500.html
│   └── static/                      # Static files
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── tests/                           # Test files
│   ├── test_app.py                  # Flask app tests
│   └── test_example.py              # Example tests
├── requirements.txt                 # Production dependencies
├── requirements-dev.txt             # Development dependencies
└── README.md
```

## 🤖 GitHub Copilot Configuration

This project includes a comprehensive GitHub Copilot setup:

### Instructions Files

These files guide Copilot's behavior for different aspects of development:

- **python.instructions.md**: Python coding conventions and best practices
- **testing.instructions.md**: Testing standards using pytest
- **security.instructions.md**: Security best practices
- **documentation.instructions.md**: Documentation standards (PEP 257)
- **performance.instructions.md**: Performance optimization guidelines
- **code-review.instructions.md**: Code review standards

### Prompts

Reusable prompts for common development tasks:

- **setup-component.prompt.md**: Create new Python modules
- **write-tests.prompt.md**: Generate test cases
- **code-review.prompt.md**: Perform code reviews
- **refactor-code.prompt.md**: Refactor existing code
- **generate-docs.prompt.md**: Generate documentation
- **debug-issue.prompt.md**: Debug and fix issues

### Agents

Specialized chat modes for different scenarios:

- **architect.agent.md**: Architecture planning and design
- **reviewer.agent.md**: Code review mode
- **debugger.agent.md**: Debugging assistance

## 🎯 Usage

### Using Instructions

Instructions are automatically applied when you work with relevant files. For example, when editing a `.py` file, Copilot will follow `python.instructions.md`.

### Using Prompts

1. Open GitHub Copilot Chat
2. Type `#` to see available prompts
3. Select a prompt or type `#filename` (e.g., `#write-tests`)
4. Follow the prompt's guidance

### Using Agents

1. Open GitHub Copilot Chat
2. Type `@` to see available agents
3. Select an agent (e.g., `@architect`)
4. Ask your question in that specialized mode

## 💻 Development Workflow

### Creating a New Module

1. Use the setup-component prompt: `#setup-component`
2. Provide module name and purpose
3. Copilot will generate the module with tests

### Writing Tests

1. Use the write-tests prompt: `#write-tests`
2. Specify the module to test
3. Copilot generates comprehensive test cases

### Code Review

1. Use the reviewer agent: `@reviewer`
2. Provide code to review
3. Get structured feedback with categories

### Debugging

1. Use the debugger agent: `@debugger`
2. Describe the issue
3. Get systematic debugging assistance

### Planning Architecture

1. Use the architect agent: `@architect`
2. Describe the feature or refactoring
3. Get a detailed implementation plan

## 🧪 Testing

Run tests with pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_module.py

# Run tests with specific marker
pytest -m slow
```

## 📝 Code Style

This project follows PEP 8 guidelines. To check code style:

```bash
# Run flake8
flake8 src tests

# Format code with black
black src tests

# Sort imports with isort
isort src tests

# Type checking with mypy
mypy src
```

## 🔒 Security

Security considerations are built into the development process:

- Input validation required for all user inputs
- No hardcoded secrets (use environment variables)
- Dependencies checked with `pip-audit`
- Security best practices enforced through instructions

## 📚 Documentation

All code should be documented following PEP 257:

- Module-level docstrings
- Class docstrings with attributes
- Function docstrings with Args, Returns, and Raises sections
- Type hints for all parameters and return values

## 🚀 CI/CD and Deployment

### GitHub Pages Deployment

The site is automatically deployed to GitHub Pages on every push to the `main` branch.

**Deployment Workflow** (`.github/workflows/deploy-pages.yml`):

1. Triggers on push to main or manual workflow dispatch
2. Sets up Python 3.11
3. Installs dependencies
4. Runs `build.py` to generate static HTML files
5. Deploys the `docs/` directory to GitHub Pages

**Manual Deployment**:

```bash
# Build the static site
python build.py

# Commit and push
git add docs/
git commit -m "Update static site"
git push origin main
```

### Testing Workflow

GitHub Actions workflow (`copilot-setup-steps.yml`) runs on:

- Manual trigger (workflow_dispatch)
- Changes to the workflow file

The workflow:

1. Sets up Python 3.11
2. Installs dependencies
3. Runs linting with flake8
4. Runs tests with pytest and coverage

### Build Process

The `build.py` script converts the Flask application to static HTML:

1. **Renders all routes** to static HTML files
2. **Updates asset paths** for GitHub Pages (repo-based hosting with `/gh-copilot-raisa/` base URL)
3. **Copies static assets** (CSS, JS) to the output directory
4. **Outputs to `docs/`** directory for GitHub Pages

To rebuild the static site:

```bash
python build.py        # Outputs to docs/
python build.py dist   # Custom output directory
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Follow the coding standards in `.github/instructions/`
4. Write tests for new functionality
5. Update documentation
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Python instructions adapted from [awesome-copilot](https://github.com/github/awesome-copilot)
- Follows PEP 8 and PEP 257 conventions

## 📞 Support

For questions or issues:

- Review the instruction files in `.github/instructions/`
- Use the appropriate agent or prompt for assistance
- Consult the Python documentation

---

**Happy Coding with GitHub Copilot! 🚀**
