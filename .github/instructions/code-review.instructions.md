---
description: 'Code review standards and GitHub review guidelines'
applyTo: '**/*.py'
---

# Code Review Standards

## Review Objectives

- Ensure code correctness and functionality.
- Verify adherence to coding standards and best practices.
- Identify potential bugs, security issues, and performance problems.
- Assess code readability and maintainability.
- Share knowledge and promote team learning.

## What to Review

### Code Quality

- Does the code follow Python PEP 8 style guidelines?
- Are variable and function names descriptive and consistent?
- Is the code DRY (Don't Repeat Yourself)?
- Are there any code smells or anti-patterns?

### Functionality

- Does the code do what it's supposed to do?
- Are edge cases handled appropriately?
- Is error handling comprehensive and appropriate?
- Are there any logical errors or potential bugs?

### Testing

- Are there adequate test cases?
- Do tests cover both success and failure scenarios?
- Are tests clear and maintainable?
- Is test coverage acceptable?

### Security

- Are there any security vulnerabilities?
- Is user input properly validated and sanitized?
- Are sensitive data handled securely?
- Are dependencies up-to-date and secure?

### Performance

- Are there any obvious performance issues?
- Is the algorithm choice appropriate?
- Are resources managed efficiently?
- Could the code benefit from optimization?

### Documentation

- Are docstrings present and following conventions?
- Is complex logic adequately commented?
- Are API changes documented?
- Is the README updated if needed?

## Review Process

### For Reviewers

1. **Understand the Context**: Read the PR description and linked issues.
2. **Review Incrementally**: Don't try to review large PRs in one sitting.
3. **Be Constructive**: Provide specific, actionable feedback.
4. **Prioritize Issues**: Distinguish between critical issues and suggestions.
5. **Ask Questions**: If something is unclear, ask for clarification.
6. **Suggest Improvements**: Offer alternatives when pointing out problems.
7. **Acknowledge Good Work**: Recognize well-written code and good practices.

### For Authors

1. **Self-Review First**: Review your own code before requesting review.
2. **Keep PRs Small**: Smaller PRs are easier to review thoroughly.
3. **Provide Context**: Write clear PR descriptions explaining the changes.
4. **Respond Promptly**: Address review comments in a timely manner.
5. **Be Open to Feedback**: Consider suggestions objectively.
6. **Explain Decisions**: Clarify your reasoning when asked.
7. **Update Documentation**: Ensure docs reflect code changes.

## Review Comments

### Structure

- Be specific about what needs to change and why.
- Provide examples or suggestions when appropriate.
- Use clear, professional language.
- Categorize feedback (e.g., "Critical:", "Suggestion:", "Question:").

### Tone

- Be respectful and professional.
- Focus on the code, not the person.
- Assume good intent.
- Frame feedback constructively.

### Examples

**Good:**
- "Consider using a set instead of a list here for O(1) lookup time."
- "This function could benefit from a docstring explaining the parameters."
- "Critical: This SQL query is vulnerable to injection. Use parameterized queries."

**Avoid:**
- "This code is terrible."
- "Why would you do it this way?"
- "Obviously this is wrong."

## GitHub Review Best Practices

### PR Size

- Keep PRs focused on a single concern.
- Aim for PRs under 400 lines of code when possible.
- Break large features into multiple PRs.

### PR Description

- Explain what changes were made and why.
- Link to related issues or discussions.
- Include screenshots or examples for UI changes.
- Note any breaking changes or migration steps.

### Commit Messages

- Use clear, descriptive commit messages.
- Follow conventional commit format when applicable.
- Keep commits atomic and focused.

### Review Workflow

1. Read the PR description and understand the goal.
2. Review the test files first to understand expected behavior.
3. Review the main code changes.
4. Check for documentation updates.
5. Verify CI checks pass.
6. Approve or request changes with specific feedback.

## Checklist for Reviewers

- [ ] Code follows project style guidelines
- [ ] Changes are well-tested
- [ ] Documentation is updated
- [ ] No security vulnerabilities introduced
- [ ] Performance considerations addressed
- [ ] Error handling is appropriate
- [ ] Code is readable and maintainable
- [ ] No unnecessary complexity added
- [ ] Breaking changes are documented
- [ ] CI checks pass
