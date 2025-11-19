# GitHub Copilot Quick Reference Guide

Quick reference for customizing GitHub Copilot at user and project levels.

## 📁 File Locations Cheat Sheet

| Configuration              | Location                                 | Level     | Version Control |
| -------------------------- | ---------------------------------------- | --------- | --------------- |
| Main Instructions          | `.github/copilot-instructions.md`        | Project   | ✅ Yes          |
| File-Specific Instructions | `.github/instructions/*.instructions.md` | Project   | ✅ Yes          |
| Reusable Prompts           | `.github/prompts/*.prompt.md`            | Project   | ✅ Yes          |
| Custom Agents              | `.github/agents/*.agent.md`              | Project   | ✅ Yes          |
| Workspace Settings         | `.vscode/settings.json`                  | Workspace | ✅ Yes          |
| User Settings              | `~/.vscode/settings.json`                | User      | ❌ No           |
| MCP Configuration          | `.vscode/settings.json` or user settings | Both      | Depends         |

---

## 🚀 Quick Setup Commands

### Create Project Structure

```bash
# Create all necessary folders
mkdir -p .github/instructions .github/prompts .github/agents .vscode

# Create main instructions file
touch .github/copilot-instructions.md

# Create workspace settings
touch .vscode/settings.json
```

### Initialize Configuration Files

```bash
# Python project
cat > .github/instructions/python.instructions.md << 'EOF'
---
description: Python coding standards
applyTo: '**/*.py'
---

# Python Standards
- Follow PEP 8
- Use type hints
- Write docstrings
EOF

# JavaScript/TypeScript project
cat > .github/instructions/javascript.instructions.md << 'EOF'
---
description: JavaScript/TypeScript standards
applyTo: '**/*.js,**/*.ts,**/*.jsx,**/*.tsx'
---

# JavaScript/TypeScript Standards
- Use ESLint
- Prefer const over let
- Use async/await
EOF
```

---

## 📝 File Templates

### Custom Instruction Template

```markdown
---
description: Brief description
applyTo: "**/*.ext"
---

# Title

## Section 1

Content...

## Section 2

Content...
```

### Prompt File Template

```markdown
# Prompt Title

Brief description of what this prompt does.

## Context

[Optional context about when to use this]

## Instructions

1. First instruction
2. Second instruction
3. Third instruction

## Output Format

[Specify expected output format]
```

### Agent File Template

```markdown
---
name: Agent Name
description: Brief description
icon: 🤖
---

# Agent Name

I am specialized in [area of expertise].

## What I Help With

- Task 1
- Task 2
- Task 3

## My Approach

1. Step 1
2. Step 2
3. Step 3
```

---

## ⚙️ Common Settings Snippets

### Basic Copilot Settings

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false
  },
  "editor.inlineSuggest.enabled": true,
  "github.copilot.editor.enableAutoCompletions": true
}
```

### Python Project Settings

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

### JavaScript/TypeScript Project Settings

```json
{
  "eslint.enable": true,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

### MCP Servers Configuration

```json
{
  "mcp.servers": {
    "azure": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure/mcp@latest", "server", "start"]
    },
    "microsoft-learn": {
      "type": "http",
      "url": "https://mcp-server.microsoft.com/learn"
    },
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["@github/mcp-server"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

---

## 🎯 Glob Patterns for `applyTo`

| Pattern               | Matches                             |
| --------------------- | ----------------------------------- |
| `**/*.py`             | All Python files                    |
| `**/*.{js,ts}`        | All JavaScript and TypeScript files |
| `**/*.tsx`            | All TypeScript React files          |
| `src/**/*.py`         | Python files in src directory       |
| `**/test_*.py`        | Python test files                   |
| `**`                  | All files                           |
| `*.md`                | Markdown files in root only         |
| `**/*.md`             | All Markdown files recursively      |
| `!**/node_modules/**` | Exclude node_modules                |

---

## 🔧 VS Code Commands

| Command                      | Shortcut                                     | Description                   |
| ---------------------------- | -------------------------------------------- | ----------------------------- |
| Chat: Configure Instructions | `Ctrl+Shift+P` → Type command                | Configure custom instructions |
| MCP: Add Server              | `Ctrl+Shift+P` → Type command                | Add new MCP server            |
| MCP: Show Servers            | `Ctrl+Shift+P` → Type command                | View active MCP servers       |
| Open Settings (UI)           | `Ctrl+,`                                     | Open settings interface       |
| Open Settings (JSON)         | `Ctrl+Shift+P` → "Open User Settings (JSON)" | Edit settings directly        |
| Reload Window                | `Ctrl+Shift+P` → "Reload Window"             | Reload VS Code                |
| GitHub Copilot: Sign In      | `Ctrl+Shift+P` → Type command                | Sign in to Copilot            |

---

## 💡 Using Custom Configurations

### Using Custom Instructions

1. Create `.github/copilot-instructions.md`
2. Copilot automatically uses it in all interactions
3. No special syntax needed in chat

### Using Prompts

1. In Copilot Chat, type `#`
2. Select from available prompts
3. Or type `#prompt-name`
4. Add additional context if needed

### Using Agents

1. In Copilot Chat, type `@`
2. Select custom agent
3. Ask your question
4. Agent responds with specialized knowledge

### Using MCP Tools

1. Enable Agent Mode in Copilot Chat
2. Click tools icon to see available MCP servers
3. Ask questions that require MCP tools
4. Copilot automatically uses appropriate tools

---

## 📋 Common Patterns

### Security-Focused Instructions

```markdown
# Security Requirements

- Never hardcode API keys, passwords, or secrets
- Use environment variables for configuration
- Validate all user inputs
- Sanitize data before database queries
- Use parameterized queries to prevent SQL injection
- Implement proper error handling without exposing sensitive information
- Use HTTPS for all external communications
- Implement rate limiting on public APIs
- Follow OWASP Top 10 security practices
```

### Testing Standards

```markdown
# Testing Requirements

- Write tests before code (TDD)
- Aim for 90%+ code coverage
- Include unit tests for all business logic
- Write integration tests for API endpoints
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)
- Mock external dependencies
- Test both success and failure scenarios
- Include edge cases in tests
```

### Documentation Standards

```markdown
# Documentation Requirements

- All public APIs must have docstrings
- Include usage examples for complex functions
- Document all parameters and return values
- Add inline comments for complex logic
- Keep README.md up to date
- Document architectural decisions (ADRs)
- Include setup instructions
- Document environment variables
```

---

## 🔍 Troubleshooting Checklist

| Issue                     | Solution                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| Instructions not working  | ✅ Check file location<br>✅ Verify YAML frontmatter<br>✅ Restart VS Code                   |
| Prompts not appearing     | ✅ Check `.prompt.md` extension<br>✅ Ensure files in `.github/prompts/`<br>✅ Reload window |
| MCP server not connecting | ✅ Verify configuration syntax<br>✅ Check authentication<br>✅ View Output → MCP logs       |
| Agent mode unavailable    | ✅ Update VS Code<br>✅ Update Copilot extension<br>✅ Check Copilot plan                    |
| Settings not applying     | ✅ Check settings level (User/Workspace)<br>✅ Verify JSON syntax<br>✅ Restart VS Code      |

---

## 📚 Essential Examples

### Complete Python Project Setup

```bash
# Create structure
mkdir -p .github/instructions .github/prompts .vscode

# Main instructions
cat > .github/copilot-instructions.md << 'EOF'
# Python FastAPI Project
- Python 3.11+
- FastAPI framework
- PostgreSQL database
- pytest for testing
- Follow PEP 8 standards
EOF

# Python-specific instructions
cat > .github/instructions/python.instructions.md << 'EOF'
---
description: Python standards
applyTo: '**/*.py'
---
# Python Standards
- Use type hints
- Write Google-style docstrings
- Follow PEP 8
- Use Black formatting
EOF

# Workspace settings
cat > .vscode/settings.json << 'EOF'
{
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
EOF
```

### Complete React/TypeScript Setup

```bash
# Create structure
mkdir -p .github/instructions .github/prompts .vscode

# Main instructions
cat > .github/copilot-instructions.md << 'EOF'
# React TypeScript Project
- React 18 with TypeScript
- Use functional components and hooks
- Material-UI for components
- React Query for data fetching
- Jest and React Testing Library
EOF

# TypeScript instructions
cat > .github/instructions/typescript.instructions.md << 'EOF'
---
description: TypeScript React standards
applyTo: '**/*.tsx,**/*.ts'
---
# React TypeScript Standards
- Use functional components
- Define interfaces for props
- Use hooks for state and effects
- Export components as default
EOF

# Workspace settings
cat > .vscode/settings.json << 'EOF'
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "typescript.preferences.importModuleSpecifier": "relative"
}
EOF
```

---

## 🎓 Learning Path

### Beginner (Week 1)

- [ ] Set up basic Copilot in VS Code
- [ ] Create `.github/copilot-instructions.md`
- [ ] Configure basic workspace settings
- [ ] Learn to use inline suggestions

### Intermediate (Week 2-3)

- [ ] Create file-specific instructions
- [ ] Set up reusable prompts
- [ ] Configure MCP servers
- [ ] Use Copilot Chat effectively

### Advanced (Week 4+)

- [ ] Create custom agents
- [ ] Integrate multiple MCP servers
- [ ] Build custom MCP servers
- [ ] Optimize team workflows

---

## 📞 Getting Help

- [📖 Official Documentation](https://docs.github.com/en/copilot)
- [💬 Community Discussions](https://github.com/orgs/community/discussions/categories/copilot)
- [🐛 Report Issues](https://github.com/community/community/discussions/categories/copilot)
- [📺 Video Tutorials](https://www.youtube.com/@GitHub)
- [🎓 Microsoft Learn](https://learn.microsoft.com/en-us/training/paths/copilot/)

---

## 🔗 Quick Links

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/copilot/overview)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Azure MCP Server](https://github.com/Azure/azure-mcp)
- [Awesome Copilot](https://github.com/github/awesome-copilot)
