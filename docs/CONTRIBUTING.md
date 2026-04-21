# Contributing to Claude Tests & Skills

Thank you for your interest in contributing! This guide will help you get started.

## Code of Conduct

Be respectful and constructive. We aim to create an inclusive, welcoming environment.

## Getting Started

### Prerequisites
- Git installed
- Python 3.8 or higher
- Claude Code (optional but recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/GuillermoGG0102/claude_tests.git
cd claude_tests

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt
```

## Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation
- `refactor/` for code improvements

### 2. Make Changes
- Follow the project structure (see [PROJECT_STRUCTURE.md](../references/PROJECT_STRUCTURE.md))
- Keep changes focused and atomic
- Write clear commit messages

### 3. Write Tests
Add tests for new functionality:
```bash
# Run tests
python -m pytest tests/
```

### 4. Update Documentation
- Update README if needed
- Add docstrings to new functions
- Update references/ guides if relevant

### 5. Commit and Push
```bash
git add .
git commit -m "Clear, descriptive commit message"
git push origin feature/your-feature-name
```

### 6. Create Pull Request
Open a PR with:
- Clear title
- Description of changes
- Reference to related issues
- Test results

## Creating a New Skill

See [SKILLS.md](../references/SKILLS.md) for detailed instructions.

Quick checklist:
- [ ] Skill has clear, descriptive name
- [ ] Skill has comprehensive description
- [ ] Code is under 500 lines
- [ ] Includes proper directory structure
- [ ] Documentation in references/
- [ ] Examples in examples/
- [ ] Tests in tests/

Example structure:
```
my-new-skill/
├── skill.md
├── scripts/
│   └── main.py
├── references/
│   └── README.md
└── assets/
    └── example.json
```

## Code Standards

### Python Style
- Follow PEP 8
- Use type hints
- Write docstrings for public functions
- Keep functions small and focused

Example:
```python
def process_text(content: str) -> dict:
    """Process text and return metrics.
    
    Args:
        content: Text to process
        
    Returns:
        Dictionary with analysis results
    """
    # Implementation
    return {}
```

### Naming Conventions
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_SNAKE_CASE` for constants
- Prefix private members with `_`

### Comments
- Comment the WHY, not the WHAT
- Code should be self-explanatory
- Keep comments brief

## Documentation Standards

### Markdown Style
- Use clear headers
- Include code examples
- Add table of contents for long docs
- Link between related documents

### File Organization
- One topic per file
- Clear, descriptive filenames
- Proper directory structure

## Testing

### Unit Tests
```python
import pytest
from scripts.my_module import my_function

def test_my_function():
    result = my_function("input")
    assert result == "expected"
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_scripts.py::test_my_function

# Run with coverage
pytest --cov=scripts tests/
```

### Test Requirements
- Test critical functionality
- Include edge cases
- Keep tests independent
- Use descriptive names

## Performance

### Guidelines
- Profile before optimizing
- Avoid premature optimization
- Document performance constraints
- Include performance tests for critical paths

### Benchmarking
```python
import time

start = time.time()
result = my_function()
duration = time.time() - start
print(f"Execution time: {duration:.3f}s")
```

## Security

### API Keys & Secrets
- Never commit .env files
- Use .env.example as template
- Document required credentials
- Use environment variables

### Dependency Management
- Keep dependencies minimal
- Review new dependencies
- Update regularly
- Check for security issues

```bash
# Check for security issues
pip install safety
safety check
```

## Commit Messages

Use clear, descriptive messages:

**Good:**
```
Add image generation skill with FLUX.2 support

- Implement image generation API integration
- Add support for editing existing images
- Include examples and documentation
```

**Bad:**
```
fix stuff
update things
changes
```

### Format
```
[Type] Brief description (50 chars max)

Longer explanation if needed (wrap at 72 chars).
Include reasoning and important details.

- Bullet points for multiple changes
- Reference issues if applicable: Fixes #123
```

## Pull Request Guidelines

### Title
- Clear and descriptive
- Under 70 characters
- Start with type: `feat:`, `fix:`, `docs:`, etc.

### Description
```markdown
## Description
Brief overview of changes

## Type
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Performance improvement
- [ ] Refactoring

## Testing
How was this tested?

## Related Issues
Fixes #123
Related to #456

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Follows code style
```

## Review Process

### What We Look For
- Code quality and style
- Test coverage
- Documentation
- Performance impact
- Security implications

### Common Feedback
- Missing tests
- Unclear variable names
- Missing documentation
- Style inconsistencies
- Edge cases not handled

### Responding to Feedback
- Thank reviewers for suggestions
- Ask clarifying questions
- Make requested changes
- Explain any disagreements
- Push updates (don't force)

## Staying Updated

### Keeping Your Fork Current
```bash
# Add upstream remote
git remote add upstream https://github.com/GuillermoGG0102/claude_tests.git

# Fetch updates
git fetch upstream

# Rebase your branch
git rebase upstream/main
```

### Following Updates
- Watch the repository
- Subscribe to releases
- Check issues for discussions
- Read commit messages

## Questions & Support

### Getting Help
- Read existing documentation
- Search closed issues
- Ask in discussions
- Contact maintainers

### Reporting Issues
1. Check if issue already exists
2. Include reproduction steps
3. Provide error messages
4. Describe expected behavior
5. Include environment info

## Recognition

Contributors are recognized:
- In README.md
- In release notes
- In commit messages
- In discussions

## Thank You!

Your contributions make this project better. We appreciate your time and effort!

---

For more information:
- [Project Structure](../references/PROJECT_STRUCTURE.md)
- [Skills Guide](../references/SKILLS.md)
- [CLAUDE.md](../CLAUDE.md)
- [README](../README.md)
