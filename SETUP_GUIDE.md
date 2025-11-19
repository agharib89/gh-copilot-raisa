# VS Code Setup Guide for GitHub Copilot

This guide will help you set up and use the GitHub Copilot configuration in this project.

## Prerequisites

1. **Visual Studio Code**: Install the latest version from [code.visualstudio.com](https://code.visualstudio.com/)
2. **GitHub Copilot Extension**: Install from the VS Code marketplace
3. **Python Extension**: Install the official Python extension for VS Code

## Enabling GitHub Copilot Features

### 1. Enable Copilot Instructions

GitHub Copilot automatically reads instruction files from the `.github/instructions/` directory when the `applyTo` pattern matches your current file.

**No configuration needed!** Just start coding and Copilot will follow the guidelines.

### 2. Using Prompts

Prompts are available in the Copilot Chat interface:

1. Open Copilot Chat (Ctrl+Shift+I or Cmd+Shift+I)
2. Type `#` to see available prompts
3. Select a prompt or reference it by name (e.g., `#write-tests`)

**Available Prompts:**

- `#setup-component` - Create new Python modules
- `#write-tests` - Generate test cases
- `#code-review` - Perform code reviews
- `#refactor-code` - Refactor existing code
- `#generate-docs` - Generate documentation
- `#debug-issue` - Debug and fix issues

### 3. Using Agents (Chat Modes)

Agents provide specialized assistance for different tasks:

1. Open Copilot Chat
2. Type `@` to see available agents
3. Select an agent to enter that mode

**Available Agents:**

- `@architect` - Architecture planning and design
- `@reviewer` - Code review mode
- `@debugger` - Debugging assistance

## Verification Steps

### Test Instructions

1. Open or create a `.py` file
2. Start typing a function
3. Copilot should suggest code following PEP 8 and include type hints

### Test Prompts

1. Open Copilot Chat
2. Type `#write-tests`
3. Ask it to generate tests for `src/example.py`
4. Verify it generates pytest-style tests

### Test Agents

1. Open Copilot Chat
2. Type `@architect`
3. Ask it to plan a new feature
4. Verify it provides a structured implementation plan

## Customization

### Modifying Instructions

Edit files in `.github/instructions/` to customize guidelines:

```yaml
---
description: "Your custom description"
applyTo: "**/*.py"
---
# Your Instructions Here
```

### Creating New Prompts

Create a new `.prompt.md` file in `.github/prompts/`:

```yaml
---
agent: "agent"
model: Claude Sonnet 4.5
tools: ["codebase"]
description: "Your prompt description"
---
# Your Prompt Instructions
```

### Creating New Agents

Create a new `.agent.md` file in `.github/agents/`:

```yaml
---
description: "Your agent description"
tools: ["codebase", "search"]
model: Claude Sonnet 4.5
---
# Your Agent Instructions
```

## Troubleshooting

### Copilot Not Following Instructions

1. Check that the file extension matches the `applyTo` pattern
2. Verify the instruction file has correct YAML frontmatter
3. Reload VS Code window (Ctrl+Shift+P > "Reload Window")

### Prompts Not Appearing

1. Ensure files have `.prompt.md` extension
2. Check YAML frontmatter is correct
3. Verify `agent: 'agent'` is set (not deprecated `mode`)
4. Reload VS Code window

### Agents Not Working

1. Ensure files have `.agent.md` extension (not `.chatmode.md`)
2. Ensure files are in `.github/agents/` directory
3. Check YAML frontmatter is valid
4. Reload VS Code window

## Tips for Best Results

### With Instructions

- Instructions apply automatically based on file type
- More specific instructions take precedence
- Keep instructions concise and actionable

### With Prompts

- Provide clear, specific requests
- Include context about what you're trying to achieve
- Reference existing code when relevant

### With Agents

- Start conversations with clear goals
- Provide error messages and reproduction steps for debugging
- Give context about the codebase for architecture planning

## Example Workflows

### Creating a New Feature

1. Use `@architect` to plan the feature:

   ```
   @architect Plan a user authentication module with JWT tokens
   ```

2. Use `#setup-component` to create the module:

   ```
   #setup-component Create an auth module for JWT authentication
   ```

3. Use `#write-tests` to generate tests:

   ```
   #write-tests Generate tests for the auth module
   ```

4. Use `@reviewer` to review your code:
   ```
   @reviewer Review the auth module implementation
   ```

### Debugging an Issue

1. Use `@debugger` with error details:

   ```
   @debugger I'm getting "KeyError: 'user_id'" in auth.py line 42
   ```

2. Follow the systematic debugging steps provided

3. Use `#write-tests` to add regression tests:
   ```
   #write-tests Add test for the KeyError edge case
   ```

### Refactoring Code

1. Use `#refactor-code` to improve code quality:

   ```
   #refactor-code Improve the complexity of the validate_input function
   ```

2. Use `@reviewer` to verify improvements:
   ```
   @reviewer Check if the refactored code follows best practices
   ```

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [Python Documentation](https://docs.python.org/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [PEP 257 Docstring Conventions](https://peps.python.org/pep-0257/)

## Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review instruction files for proper formatting
3. Consult GitHub Copilot documentation
4. Ask in the project's discussion forum or issue tracker

---

**Ready to code with AI assistance! 🚀**
