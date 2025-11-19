# GitHub Copilot Customization Guide

A comprehensive guide to customizing GitHub Copilot at both user and project levels.

## Table of Contents

1. [GitHub Copilot Settings](#github-copilot-settings)
2. [Custom Instructions](#custom-instructions)
3. [Custom Prompts](#custom-prompts)
4. [Custom Chat Modes (Agents)](#custom-chat-modes-agents)
5. [MCP Servers](#mcp-servers-model-context-protocol)
6. [Project vs User Level Configuration](#project-vs-user-level-configuration)

---

## GitHub Copilot Settings

### Accessing Settings in VS Code

1. **Open Settings**

   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
   - Or: File → Preferences → Settings

2. **Navigate to Copilot Settings**
   - Search for "GitHub Copilot" in the settings search bar
   - Or: Extensions → GitHub Copilot → Settings (gear icon)

### Key Settings to Configure

#### Code Suggestions

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false
  }
}
```

#### Inline Suggestions

```json
{
  "editor.inlineSuggest.enabled": true,
  "github.copilot.editor.enableAutoCompletions": true
}
```

#### Chat Settings

```json
{
  "github.copilot.chat.welcomeMessage": "always",
  "github.copilot.chat.localeOverride": "auto"
}
```

#### Advanced Settings

```json
{
  "github.copilot.advanced": {
    "debug.overrideEngine": "",
    "debug.testOverrideProxyUrl": "",
    "debug.filterLogCategories": []
  }
}
```

---

## Custom Instructions

Custom instructions allow you to automatically add context to every Copilot interaction.

### User-Level Instructions

**Location:** `~/.vscode/settings.json` or User Settings in VS Code

**Steps:**

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "Chat: Configure Instructions"
3. Select "User Instructions"
4. Add your custom instructions

**Example User Instructions:**

```markdown
---
description: My personal coding preferences
---

# My Coding Style

- Use TypeScript for all JavaScript projects
- Follow ESLint rules strictly
- Prefer functional components in React
- Use async/await over promises
- Write comprehensive JSDoc comments
- Follow Test-Driven Development (TDD)
```

### Project-Level Instructions

**Location:** `.github/copilot-instructions.md` (repository root)

**Steps:**

1. Create `.github` folder in your repository root
2. Create `copilot-instructions.md` file inside `.github`
3. Add project-specific instructions

**Example Project Instructions:**

```markdown
# Project: E-Commerce Platform

## Architecture

- This is a microservices-based e-commerce platform
- Backend: Node.js with Express
- Frontend: React with TypeScript
- Database: PostgreSQL
- Message Queue: RabbitMQ

## Coding Standards

- Use ES6+ syntax
- Follow Airbnb JavaScript Style Guide
- All functions must have JSDoc comments
- Use async/await for asynchronous operations
- Error handling: Use try-catch blocks

## Security Requirements

- Never hardcode API keys or passwords
- Use environment variables for configuration
- Validate all user inputs
- Sanitize data before database queries
- Use parameterized queries to prevent SQL injection

## Testing

- Write unit tests for all business logic
- Use Jest for testing
- Aim for 80%+ code coverage
- Include integration tests for API endpoints
```

### Targeted Instructions (File-Specific)

**Location:** `.github/instructions/*.instructions.md`

**Steps:**

1. Create `.github/instructions` folder
2. Create files with `.instructions.md` extension
3. Add frontmatter with `applyTo` pattern

**Example: Python Instructions**

```markdown
---
description: Python coding standards
applyTo: "**/*.py"
---

# Python Development Standards

## Code Style

- Follow PEP 8 style guide
- Use type hints for all function signatures
- Maximum line length: 79 characters
- Use 4 spaces for indentation

## Docstrings

- Use Google-style docstrings
- Include Args, Returns, and Raises sections
- Add usage examples for complex functions

## Testing

- Use pytest for unit tests
- Name test files as test\_\*.py
- Aim for 90%+ code coverage
```

**Example: React Instructions**

```markdown
---
description: React component standards
applyTo: "**/*.tsx,**/*.jsx"
---

# React Component Standards

## Component Structure

- Use functional components with hooks
- Export components as default
- Use named exports for utilities
- Keep components under 200 lines

## State Management

- Use useState for local state
- Use useContext for shared state
- Prefer React Query for server state

## Props

- Define PropTypes or TypeScript interfaces
- Destructure props in function parameters
- Provide default values for optional props
```

---

## Custom Prompts

Reusable prompts for common development tasks.

### Creating Prompt Files

**Location:** `.github/prompts/*.prompt.md`

**Steps:**

1. Create `.github/prompts` folder
2. Create files with `.prompt.md` extension
3. Write prompts using Copilot references

### Using Prompts

1. Open Copilot Chat
2. Type `#` to see available prompts
3. Select a prompt or type `#filename`
4. Add any additional context

### Example Prompts

**create-api-endpoint.prompt.md:**

```markdown
Create a new REST API endpoint with the following requirements:

- Method: [GET/POST/PUT/DELETE]
- Route: /api/[resource]
- Authentication: Required
- Request validation using Joi or Zod
- Error handling with try-catch
- Unit tests using Jest
- OpenAPI/Swagger documentation
- Rate limiting

Please include:

1. Controller function
2. Route definition
3. Input validation schema
4. Unit tests
5. API documentation
```

**refactor-component.prompt.md:**

```markdown
Refactor the selected component following these guidelines:

1. **Performance:**

   - Memoize expensive calculations with useMemo
   - Memoize callbacks with useCallback
   - Split into smaller components if over 200 lines

2. **Readability:**

   - Extract complex logic into custom hooks
   - Use descriptive variable names
   - Add comments for complex logic

3. **Maintainability:**

   - Follow single responsibility principle
   - Reduce prop drilling
   - Use TypeScript for type safety

4. **Testing:**
   - Ensure component is testable
   - Mock external dependencies
```

**generate-tests.prompt.md:**

```markdown
Generate comprehensive unit tests for #selection

Requirements:

- Test framework: Jest (JavaScript) / pytest (Python)
- Include happy path tests
- Include edge cases and error scenarios
- Mock external dependencies
- Aim for 90%+ code coverage
- Follow AAA pattern (Arrange, Act, Assert)

For each function, include tests for:

1. Valid inputs
2. Invalid inputs
3. Boundary conditions
4. Error handling
5. Side effects
```

**code-review.prompt.md:**

```markdown
Perform a thorough code review of #selection focusing on:

1. **Code Quality:**

   - Readability and maintainability
   - Adherence to coding standards
   - DRY principle violations

2. **Performance:**

   - Algorithmic efficiency
   - Memory usage
   - Database query optimization

3. **Security:**

   - Input validation
   - SQL injection vulnerabilities
   - XSS vulnerabilities
   - Authentication/authorization issues

4. **Best Practices:**
   - Error handling
   - Logging
   - Code reusability
   - Design patterns

Provide specific recommendations for improvements.
```

---

## Custom Chat Modes (Agents)

Custom chat modes (also called agents) provide specialized assistance for specific scenarios.

### Creating Agent Files

**Location:** `.github/agents/*.agent.md`

**Note:** Agent files are not officially supported yet, but you can create them following this proposed format:

**Steps:**

1. Create `.github/agents` folder (or `.github/chatmodes` for some tools)
2. Create files with `.agent.md` extension
3. Define agent behavior and expertise

### Example Agents

**architect.agent.md:**

```markdown
---
name: Architect
description: Software architecture planning and design expert
icon: 🏗️
---

# Architect Agent

I am a software architecture expert. I help you:

- Design system architectures
- Choose appropriate design patterns
- Plan database schemas
- Evaluate technology stacks
- Create technical documentation
- Assess scalability and performance

## My Approach

When you ask me for help, I will:

1. Understand your requirements and constraints
2. Ask clarifying questions about scale, budget, and timeline
3. Propose multiple architectural options
4. Explain trade-offs of each approach
5. Provide implementation roadmap
6. Suggest best practices and patterns

## Expertise Areas

- Microservices architecture
- Event-driven systems
- Database design (SQL and NoSQL)
- Cloud architecture (AWS, Azure, GCP)
- API design (REST, GraphQL, gRPC)
- Security architecture
- Performance optimization
- System scalability

## Example Interactions

- "Design a microservices architecture for an e-commerce platform"
- "What's the best database schema for a social media app?"
- "How should I structure a multi-tenant SaaS application?"
- "Review this system architecture diagram"
```

**security-reviewer.agent.md:**

```markdown
---
name: Security Reviewer
description: Security-focused code review and vulnerability detection
icon: 🔒
---

# Security Reviewer Agent

I specialize in security code reviews and vulnerability detection.

## My Focus

I examine code for:

- **Injection Vulnerabilities:** SQL, NoSQL, Command, LDAP
- **Authentication Issues:** Weak passwords, broken auth
- **Authorization Problems:** Privilege escalation, IDOR
- **XSS:** Cross-site scripting vulnerabilities
- **CSRF:** Cross-site request forgery
- **Sensitive Data Exposure:** Hardcoded secrets, logging
- **Cryptography:** Weak algorithms, poor key management
- **Dependencies:** Known vulnerabilities in packages

## Security Standards

I reference:

- OWASP Top 10
- CWE Top 25
- SANS Top 25
- PCI DSS requirements
- GDPR compliance

## My Process

1. Analyze code for security anti-patterns
2. Identify potential vulnerabilities
3. Rate severity (Critical, High, Medium, Low)
4. Provide remediation recommendations
5. Suggest secure coding alternatives
6. Reference security standards and best practices
```

**debugger.agent.md:**

```markdown
---
name: Debugger
description: Systematic debugging assistance
icon: 🐛
---

# Debugger Agent

I help you debug issues systematically and efficiently.

## My Debugging Process

1. **Reproduce:** Understand how to trigger the bug
2. **Isolate:** Narrow down the problem area
3. **Analyze:** Examine code, logs, and stack traces
4. **Hypothesize:** Form theories about the root cause
5. **Test:** Verify hypotheses with targeted changes
6. **Fix:** Implement the solution
7. **Verify:** Ensure the fix works and doesn't break anything

## What I Help With

- Interpreting error messages and stack traces
- Analyzing logs and debugging output
- Setting up debugging configurations
- Identifying root causes of bugs
- Suggesting debugging strategies
- Writing debug code and tests
- Performance profiling and optimization

## Debugging Techniques I Use

- Binary search (divide and conquer)
- Rubber duck debugging
- Time travel debugging
- Logging and tracing
- Memory profiling
- Performance profiling
- Static analysis
- Unit testing isolation

## Example Questions

- "Why is this function returning undefined?"
- "Help me debug this memory leak"
- "My API is slow - how can I find the bottleneck?"
- "This test is failing intermittently - why?"
```

---

## MCP Servers (Model Context Protocol)

MCP servers extend Copilot's capabilities by connecting to external tools and data sources.

### What is MCP?

Model Context Protocol (MCP) is an open protocol that allows AI assistants to:

- Access external data sources
- Use external tools
- Maintain context across interactions
- Provide specialized capabilities

### Installing MCP Servers

#### Method 1: VS Code Command Palette

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "MCP: Add Server"
3. Select server type (HTTP or stdio)
4. Follow configuration prompts

#### Method 2: Manual Configuration

**Location:** `.vscode/settings.json` or User Settings

```json
{
  "mcp.servers": {
    "azure-mcp": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure/mcp@latest", "server", "start"]
    },
    "microsoft-learn": {
      "type": "http",
      "url": "https://mcp.microsoft.com/learn"
    }
  }
}
```

### Popular MCP Servers

#### 1. Azure MCP Server

**Purpose:** Interact with Azure resources

**Installation:**

```bash
# Via Extension
# Install "Azure MCP Server" extension from VS Code marketplace

# Or via npm
npx -y @azure/mcp@latest server start
```

**Configuration:**

```json
{
  "mcp.servers": {
    "azure": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure/mcp@latest", "server", "start"]
    }
  }
}
```

**Usage:**

- "List my Azure resources"
- "Create a storage account in East US"
- "What's running in my subscription?"

#### 2. Microsoft Learn MCP Server

**Purpose:** Access Microsoft documentation

**Installation via Quick Add:**

- Click: [Add Microsoft Learn MCP](vscode:extension/microsoft-learn-mcp)

**Configuration:**

```json
{
  "mcp.servers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://mcp-server.microsoft.com/learn"
    }
  }
}
```

**Usage:**

- "How do I create an Azure Function?"
- "Show me TypeScript best practices from Microsoft docs"

#### 3. GitHub MCP Server

**Purpose:** Interact with GitHub repositories

**Configuration:**

```json
{
  "mcp.servers": {
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

**Usage:**

- "List open pull requests"
- "Create an issue for this bug"
- "Show recent commits"

#### 4. Database MCP Servers

**PostgreSQL:**

```json
{
  "mcp.servers": {
    "postgres": {
      "type": "stdio",
      "command": "mcp-server-postgres",
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

**Dataverse (Power Platform):**

```json
{
  "mcp.servers": {
    "dataverse": {
      "type": "http",
      "url": "https://your-org.crm.dynamics.com/api/mcp"
    }
  }
}
```

### Creating Custom MCP Servers

**Basic Structure:**

```typescript
import { MCPServer, Tool } from "@modelcontextprotocol/sdk";

const server = new MCPServer({
  name: "my-custom-server",
  version: "1.0.0",
});

// Define a tool
server.registerTool({
  name: "analyze_code",
  description: "Analyze code quality",
  parameters: {
    type: "object",
    properties: {
      code: { type: "string" },
      language: { type: "string" },
    },
  },
  handler: async ({ code, language }) => {
    // Your logic here
    return { quality: "good", issues: [] };
  },
});

server.start();
```

### Managing MCP Servers

**Enable/Disable Tools:**

1. Open Copilot Chat
2. Click tools icon (⚙️)
3. Check/uncheck MCP servers

**View Active Servers:**

1. Command Palette → "MCP: Show Servers"
2. See list of connected MCP servers

**Configure Instructions for MCP:**

Create `.github/instructions/mcp.instructions.md`:

```markdown
---
description: MCP Server Usage Guidelines
applyTo: "**"
---

# MCP Tool Usage

When using MCP tools:

- Always use microsoft_docs_search for Microsoft tech questions
- Use azure_mcp for Azure resource operations
- Prefer official documentation over general knowledge
```

---

## Project vs User Level Configuration

### Understanding Configuration Levels

| Level     | Scope             | Location                  | Use Case               |
| --------- | ----------------- | ------------------------- | ---------------------- |
| User      | All projects      | `~/.vscode/settings.json` | Personal preferences   |
| Workspace | Current workspace | `.vscode/settings.json`   | Team standards         |
| Project   | Repository        | `.github/` folder         | Project-specific rules |

### User-Level Configuration

**Location:** User Settings (applies to all projects)

**How to Configure:**

1. File → Preferences → Settings
2. Select "User" tab
3. Search for "GitHub Copilot"
4. Configure settings

**What to Configure at User Level:**

- Personal coding style preferences
- Editor behavior
- Language preferences
- Personal API keys (via env vars)
- General security practices

**Example User settings.json:**

```json
{
  "github.copilot.enable": {
    "*": true
  },
  "editor.inlineSuggest.enabled": true,
  "github.copilot.editor.enableAutoCompletions": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  }
}
```

### Project-Level Configuration

**Location:** `.github/` folder in repository root

**Structure:**

```
project-root/
├── .github/
│   ├── copilot-instructions.md       # Main project instructions
│   ├── instructions/                  # File-specific instructions
│   │   ├── python.instructions.md
│   │   ├── typescript.instructions.md
│   │   └── react.instructions.md
│   ├── prompts/                       # Reusable prompts
│   │   ├── create-component.prompt.md
│   │   ├── write-tests.prompt.md
│   │   └── code-review.prompt.md
│   └── agents/                        # Custom agents
│       ├── architect.agent.md
│       └── debugger.agent.md
└── .vscode/
    └── settings.json                  # Workspace settings
```

**What to Configure at Project Level:**

- Project architecture guidelines
- Team coding standards
- Technology stack conventions
- Security requirements
- Testing standards
- Documentation requirements

**Example .github/copilot-instructions.md:**

```markdown
# Project: Customer Management System

## Tech Stack

- Backend: Python 3.11 with FastAPI
- Frontend: React 18 with TypeScript
- Database: PostgreSQL 15
- Cache: Redis
- Message Queue: RabbitMQ

## Architecture

- Clean Architecture (Domain-Driven Design)
- CQRS pattern for data operations
- Event-driven for async operations
- RESTful API with OpenAPI documentation

## Development Standards

- All code must be type-safe
- Write tests before code (TDD)
- Use dependency injection
- Follow SOLID principles
- Document public APIs

## Security

- Never commit secrets to repository
- Use environment variables for configuration
- Validate all inputs
- Use prepared statements for SQL
- Implement rate limiting on APIs

## Testing

- Minimum 80% code coverage
- Unit tests for business logic
- Integration tests for APIs
- E2E tests for critical flows
```

### Workspace-Level Configuration

**Location:** `.vscode/settings.json` in workspace root

**What to Configure:**

- Team editor settings
- Linting rules
- Formatting preferences
- Debug configurations
- Task definitions

**Example .vscode/settings.json:**

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

### Configuration Priority

Configuration is applied in this order (later overrides earlier):

1. **Default Settings** (VS Code defaults)
2. **User Settings** (your personal preferences)
3. **Workspace Settings** (team preferences)
4. **Folder Settings** (specific folder in multi-root workspace)

### Best Practices

#### For Personal Use

- Configure user-level settings for your coding style
- Keep API keys and tokens in environment variables
- Set up personal MCP servers in user settings

#### For Teams

- Document all project-level configurations
- Version control `.github/` and `.vscode/` folders
- Use `.gitignore` for sensitive workspace settings
- Create onboarding documentation for new team members

#### For Organizations

- Create organization-wide instruction templates
- Set up company MCP servers
- Document security and compliance requirements
- Provide training on Copilot customization

---

## Complete Setup Example

Let's set up a complete Python project with all customizations:

### 1. Create Project Structure

```bash
mkdir my-python-project
cd my-python-project
mkdir -p .github/instructions .github/prompts .github/agents
mkdir -p .vscode
```

### 2. Create Project Instructions

**.github/copilot-instructions.md:**

```markdown
# My Python Project

A Flask REST API with PostgreSQL database.

## Stack

- Python 3.11
- Flask 3.0
- PostgreSQL 15
- SQLAlchemy ORM
- pytest for testing

## Standards

- Follow PEP 8
- Use type hints
- Write docstrings (Google style)
- 90% test coverage required
```

### 3. Create Language-Specific Instructions

**.github/instructions/python.instructions.md:**

```markdown
---
description: Python coding standards
applyTo: "**/*.py"
---

# Python Standards

## Code Style

- Follow PEP 8
- Use Black for formatting
- Use isort for imports
- Maximum line length: 88

## Type Hints

- Use type hints for all functions
- Import from typing module
- Use Optional for nullable types

## Testing

- Use pytest
- Name tests as test\_\*.py
- Aim for 90%+ coverage
```

### 4. Create Prompts

**.github/prompts/create-api-endpoint.prompt.md:**

```markdown
Create a Flask API endpoint with:

- Input validation using Pydantic
- Database operations using SQLAlchemy
- Error handling
- Unit tests with pytest
- OpenAPI documentation
```

### 5. Configure Workspace

**.vscode/settings.json:**

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false
}
```

### 6. Add MCP Servers

**.vscode/settings.json:**

```json
{
  "mcp.servers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://mcp-server.microsoft.com/learn"
    }
  }
}
```

### 7. Commit Configuration

```bash
git add .github/ .vscode/
git commit -m "Add Copilot customization"
git push
```

Now your team has consistent Copilot behavior across the project!

---

## Troubleshooting

### Common Issues

**1. Instructions Not Working**

- Ensure files are in `.github/` folder
- Check YAML frontmatter syntax
- Verify `applyTo` glob patterns
- Restart VS Code

**2. Prompts Not Appearing**

- Check file extension is `.prompt.md`
- Ensure files are in `.github/prompts/`
- Refresh Copilot (reload window)

**3. MCP Server Not Connecting**

- Verify configuration syntax
- Check network connectivity
- Ensure authentication is set up
- View MCP logs in Output panel

**4. Agent Mode Not Available**

- Update VS Code and Copilot extension
- Check if feature is enabled in your plan
- Verify you're signed in to GitHub

### Getting Help

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/copilot/overview)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [GitHub Community Discussions](https://github.com/orgs/community/discussions/categories/copilot)

---

## Additional Resources

- [Official GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [VS Code Copilot Documentation](https://code.visualstudio.com/docs/copilot/overview)
- [Microsoft Learn - Copilot Courses](https://learn.microsoft.com/en-us/training/paths/copilot/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/specification)
- [Azure MCP Server](https://github.com/Azure/azure-mcp)
- [Awesome Copilot Resources](https://github.com/github/awesome-copilot)
