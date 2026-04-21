# Creating Claude Skills

A comprehensive guide to building Claude skills—reusable, focused modules that extend Claude's capabilities.

## What is a Skill?

A skill is a self-contained, focused module that teaches Claude how to accomplish a specific task. Skills are:
- **Focused**: Do one thing well
- **Reusable**: Can be used across different projects
- **Documented**: Include clear examples and usage patterns
- **Concise**: Keep code under 500 lines

## Core Requirements

Every skill MUST include:

### 1. `name`
- Short, kebab-case identifier
- Examples: `code-review`, `image-generator`, `data-analyzer`
- Used when loading or referencing the skill

### 2. `description`
- Concise explanation of what the skill does
- Should describe the expertise or capability
- Example: "Analyzes code for bugs, performance, and security issues"

## Optional Fields

Skills MAY include:

### `allowed-tools`
Specify which tools your skill can access:
```yaml
allowed-tools:
  - bash
  - read
  - grep
  - github
```

### `model`
Specify a preferred Claude model:
```yaml
model: claude-opus-4-7
```

## Directory Structure

Organize your skill with this structure:

```
my-skill/
├── skill.md              # Metadata (name, description, etc.)
├── scripts/              # Executable code
│   ├── main.py
│   ├── helper.py
│   └── utils.py
├── references/           # Documentation
│   ├── README.md
│   ├── EXAMPLES.md
│   └── API_GUIDE.md
└── assets/               # Templates, data, icons
    ├── template.json
    └── sample_data.csv
```

### `scripts/`
- Python files with main logic
- Keep implementations focused and under 500 lines
- Use clear function and variable names
- Include docstrings for public functions

### `references/`
- Detailed documentation
- Usage examples
- Troubleshooting guides
- API specifications if applicable

### `assets/`
- JSON templates
- Sample data files
- Icons or images
- Configuration templates

## Skill Definition File

Create a `skill.md` file with your skill metadata:

```yaml
---
name: code-analyzer
description: |
  Analyzes Python code for:
  - Performance bottlenecks
  - Code quality issues
  - Security vulnerabilities
  - Best practice violations

allowed-tools:
  - read
  - bash
  - grep

model: claude-opus-4-7
---

# Code Analyzer Skill

Detailed documentation of your skill goes here.
```

## Example Skills

### Simple: Text Processor
- **Purpose**: Transform and clean text
- **Code**: ~100 lines
- **Tools**: None required

### Moderate: Git Helper
- **Purpose**: Analyze git history and suggest improvements
- **Code**: ~250 lines
- **Tools**: bash, grep

### Complex: Code Reviewer
- **Purpose**: Review code with detailed feedback
- **Code**: ~400 lines
- **Tools**: read, bash, grep, github

## Best Practices

### 1. Single Responsibility
Each skill should solve ONE problem well. Don't try to do too much.

**Good:**
- `markdown-to-html` - converts markdown to HTML
- `performance-profiler` - analyzes code performance

**Bad:**
- `all-in-one-tool` - does everything
- `generic-helper` - unclear purpose

### 2. Clear Documentation
Include:
- What the skill does
- How to use it
- Example usage
- Common use cases
- Error handling and edge cases

### 3. Focused Dependencies
Only specify tools and models if truly necessary:
```yaml
# ✓ Good - specific and necessary
allowed-tools:
  - read
  - bash

# ✗ Avoid - overly broad
allowed-tools:
  - bash
  - read
  - write
  - edit
  - grep
  - glob
```

### 4. Testing & Examples
Provide working examples:
- Create example files in `examples/`
- Show common use cases
- Document edge cases
- Include sample output

### 5. Modularity
Design skills to be composable:
- Don't reinvent the wheel
- Reuse other skills when possible
- Keep interfaces clean and predictable

## Code Style Guide

### Python
```python
def analyze_performance(code_snippet: str) -> dict:
    """Analyze code for performance issues.
    
    Args:
        code_snippet: Python code to analyze
        
    Returns:
        Dictionary with issues and recommendations
    """
    issues = []
    # Implementation here
    return {"issues": issues}
```

### Naming Conventions
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private: prefix with `_`

### Comments
- Only comment the WHY, not the WHAT
- Code should be self-explanatory
- Use docstrings for public APIs

## Publishing Your Skill

1. **Organize**: Ensure proper directory structure
2. **Document**: Add comprehensive references/
3. **Test**: Verify with examples/
4. **Review**: Check code quality and clarity
5. **Tag**: Use semantic versioning (v1.0.0)
6. **Share**: Make available in your repository

## Common Patterns

### Pattern 1: File Processor
```
Input: File path
Process: Read, analyze, transform
Output: Modified content or report
```

### Pattern 2: Query Analyzer
```
Input: Query/request
Process: Parse, analyze, generate
Output: Results or recommendations
```

### Pattern 3: Integration
```
Input: External API call
Process: Format, integrate, transform
Output: Processed response
```

## Troubleshooting

### Issue: Skill exceeds 500 lines
**Solution**: Break into smaller skills or extract utilities

### Issue: Documentation unclear
**Solution**: Add examples to `references/EXAMPLES.md`

### Issue: Tool access denied
**Solution**: Add tools to `allowed-tools` in skill metadata

### Issue: Performance slow
**Solution**: Profile with time imports, optimize critical paths

## Resources

- [Claude Skills Infographic](../CLAUDE_SKILLS_INFOGRAPHIC.md)
- [Project Structure Guide](PROJECT_STRUCTURE.md)
- [Claude Code Documentation](https://github.com/anthropics/claude-code)

## Quick Checklist

Creating a new skill? Use this checklist:

- [ ] Chose a clear, descriptive name
- [ ] Wrote a concise description
- [ ] Created proper directory structure
- [ ] Added executable code to `scripts/`
- [ ] Documented in `references/`
- [ ] Included examples
- [ ] Kept code under 500 lines
- [ ] Specified needed tools/model
- [ ] Tested with examples
- [ ] Ready to publish
