# Quick Start Guide

Get up and running with your GitHub Copilot-enabled Python project in 5 minutes!

## ⚡ 1-Minute Setup

```bash
# Navigate to project
cd "github-copilot"

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests to verify setup
pytest
```

## ✅ Verify GitHub Copilot Integration

### Test Instructions (Auto-Applied)

1. Open `src/example.py` in VS Code
2. Add a new function and start typing
3. Copilot should suggest code with type hints and docstrings

### Test a Prompt

1. Open Copilot Chat (Ctrl+Shift+I or Cmd+Shift+I)
2. Type: `#write-tests for the greet function`
3. Watch it generate pytest tests!

### Test an Agent

1. Open Copilot Chat
2. Type: `@architect plan a user authentication module`
3. Get a detailed implementation plan!

## 📖 Key Features

### Available Prompts (use `#`)

- `#setup-component` - Create new modules
- `#write-tests` - Generate tests
- `#code-review` - Review code
- `#refactor-code` - Refactor code
- `#generate-docs` - Generate docs
- `#debug-issue` - Debug issues

### Available Agents (use `@`)

- `@architect` - Plan architecture
- `@reviewer` - Review code
- `@debugger` - Debug issues

### Auto-Applied Instructions

- Python best practices (PEP 8, PEP 257)
- Security guidelines
- Testing standards
- Documentation requirements

## 🎯 Your First Task

Try creating a new module:

```
1. Open Copilot Chat
2. Type: #setup-component
3. Say: "Create a calculator module with add, subtract, multiply, and divide functions"
4. Watch it create the module with tests!
```

## 📚 Learn More

- **README.md** - Full project documentation
- **SETUP_GUIDE.md** - Detailed VS Code setup
- **PROJECT_SUMMARY.md** - Complete setup details
- **CONTRIBUTING.md** - Contribution guidelines

## 🚀 Start Coding!

You're all set! GitHub Copilot will now:

- ✅ Follow project coding standards
- ✅ Generate code with type hints
- ✅ Create comprehensive tests
- ✅ Provide security guidance
- ✅ Help with architecture planning

Happy coding! 🎉
