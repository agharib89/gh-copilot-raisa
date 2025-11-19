---
description: 'Security best practices for Python development'
applyTo: '**/*.py'
---

# Security Best Practices

## Input Validation

- Validate and sanitize all user inputs.
- Use type hints and validation libraries like `pydantic` for data validation.
- Never trust user-supplied data without validation.
- Implement input length limits and format validation.

## Sensitive Data Handling

- Never hardcode secrets, API keys, or passwords in source code.
- Use environment variables for sensitive configuration.
- Consider using secret management services (e.g., AWS Secrets Manager, Azure Key Vault).
- Ensure sensitive data is not logged or exposed in error messages.

## Authentication and Authorization

- Use established authentication libraries and frameworks.
- Implement proper session management with secure session tokens.
- Use strong password hashing algorithms (e.g., bcrypt, Argon2).
- Never store passwords in plain text.
- Implement proper authorization checks before accessing resources.

## SQL Injection Prevention

- Always use parameterized queries or ORM methods.
- Never concatenate user input directly into SQL queries.
- Use prepared statements for database operations.
- Validate and sanitize all database inputs.

## Dependency Security

- Regularly update dependencies to patch security vulnerabilities.
- Use `pip-audit` or `safety` to check for known vulnerabilities.
- Pin dependency versions in `requirements.txt`.
- Review third-party libraries before adding them to the project.

## Code Injection Prevention

- Avoid using `eval()`, `exec()`, or `compile()` with user input.
- Sanitize inputs when using subprocess or shell commands.
- Use safe alternatives like `ast.literal_eval()` for evaluating literals.
- Be cautious with dynamic imports and reflection.

## File Operations

- Validate file paths to prevent directory traversal attacks.
- Implement proper file upload restrictions (size, type, content).
- Use secure file permissions.
- Avoid executing uploaded files or untrusted code.

## Cryptography

- Use established cryptographic libraries (e.g., `cryptography`, `PyNaCl`).
- Never implement custom cryptographic algorithms.
- Use secure random number generators (`secrets` module).
- Follow current best practices for encryption key management.

## Error Handling

- Avoid exposing sensitive information in error messages.
- Log errors appropriately without revealing system details.
- Use generic error messages for user-facing errors.
- Implement proper exception handling to prevent information leakage.

## API Security

- Implement rate limiting to prevent abuse.
- Use HTTPS for all network communications.
- Validate and sanitize API request data.
- Implement proper CORS policies.
- Use authentication tokens with appropriate expiration.

## Logging and Monitoring

- Log security-relevant events (authentication, authorization failures).
- Never log sensitive data (passwords, tokens, PII).
- Implement log rotation and secure log storage.
- Monitor for suspicious activity and potential security breaches.

## Best Practices

- Follow the principle of least privilege.
- Keep security libraries and frameworks up-to-date.
- Conduct regular security code reviews.
- Use static analysis tools to detect security issues.
- Implement defense in depth with multiple security layers.
