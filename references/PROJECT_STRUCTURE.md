# Project Structure Guide

Detailed explanation of the recommended directory structure for Claude projects.

## Directory Tree

```
claude_tests/
│
├── .claude/                      # Claude Code configuration
│   └── settings.json             # Model, tools, paths, hooks
│
├── .git/                         # Git repository (hidden)
├── .gitignore                    # Git ignore patterns
│
├── scripts/                      # Executable code & utilities
│   ├── generate_image.py         # AI image generation
│   ├── helper_functions.py       # Reusable utilities
│   └── ...                       # More scripts as needed
│
├── references/                   # Documentation & guides
│   ├── SKILLS.md                 # How to create skills
│   ├── PROJECT_STRUCTURE.md      # This file
│   ├── API_GUIDE.md              # API documentation
│   ├── TROUBLESHOOTING.md        # Common issues & solutions
│   └── ...                       # More guides
│
├── assets/                       # Static files & data
│   ├── templates/                # JSON/YAML templates
│   │   ├── skill_template.md
│   │   └── config_template.json
│   ├── icons/                    # Icon files
│   │   └── skill_icon.svg
│   ├── sample_data/              # Example datasets
│   │   └── sample.csv
│   └── ...
│
├── examples/                     # Working examples
│   ├── hello-skill.md            # Example skill definition
│   ├── basic_usage.py            # Usage examples
│   └── ...                       # More examples
│
├── tests/                        # Test files
│   ├── test_scripts.py           # Unit tests
│   ├── test_integration.py       # Integration tests
│   └── ...
│
├── docs/                         # Extended documentation
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── DEPLOYMENT.md             # Deployment guide
│   └── ...
│
├── CLAUDE.md                     # Project instructions for Claude
├── README.md                     # Project overview & quick start
├── CLAUDE_SKILLS_INFOGRAPHIC.md  # Visual guide
└── .env.example                  # Environment variables template
```

## Directory Purposes

### `.claude/`
Claude Code configuration directory.

**Files:**
- `settings.json` - Main configuration
  - Model selection (e.g., `claude-opus-4-7`)
  - Tool permissions
  - Path exclusions
  - Hook definitions

**Guidelines:**
- Keep configuration minimal
- Don't commit sensitive data
- Use `.env` for secrets

---

### `scripts/`
**Purpose:** Executable Python scripts and utilities

**What goes here:**
- Standalone scripts
- Utility functions
- Helper libraries
- Main implementations

**Structure:**
```
scripts/
├── generate_image.py       # Main feature script
├── image_processor.py      # Supporting utilities
├── utils.py                # Reusable functions
└── config.py               # Configuration management
```

**Guidelines:**
- Keep each script focused
- Maximum ~500 lines per script
- Use clear naming
- Include docstrings
- Add error handling

**Example script template:**
```python
#!/usr/bin/env python3
"""
Script description and purpose.
"""

import sys
from typing import Optional

def main_function(arg1: str, arg2: Optional[str] = None) -> bool:
    """Description of function."""
    pass

if __name__ == "__main__":
    main_function(sys.argv[1])
```

---

### `references/`
**Purpose:** Documentation, guides, and how-tos

**What goes here:**
- Skill creation guides
- API documentation
- Setup instructions
- Troubleshooting
- Best practices

**Structure:**
```
references/
├── SKILLS.md               # How to create skills
├── PROJECT_STRUCTURE.md    # Structure explanation (this file)
├── API_GUIDE.md            # API reference
├── TROUBLESHOOTING.md      # Common issues
├── DEPLOYMENT.md           # Deployment guide
└── ARCHITECTURE.md         # System design
```

**Guidelines:**
- Use markdown (.md)
- Keep sections focused
- Include examples
- Add table of contents for long docs
- Link between documents

---

### `assets/`
**Purpose:** Static files, templates, and data

**Structure:**
```
assets/
├── templates/
│   ├── skill_template.md           # Skill boilerplate
│   ├── config_template.json        # Config template
│   └── readme_template.md
├── icons/
│   ├── skill_icon.svg
│   └── logo.png
├── sample_data/
│   ├── sample.csv
│   ├── example.json
│   └── dataset.txt
└── icons/
    └── ...
```

**Guidelines:**
- Organize by file type
- Use clear naming
- Document templates
- Include sample data for testing

---

### `examples/`
**Purpose:** Working examples and demonstrations

**What goes here:**
- Example skill definitions
- Usage demonstrations
- Test cases
- Working code samples

**Structure:**
```
examples/
├── hello-skill.md          # Simple skill example
├── advanced-skill.md       # Complex skill example
├── usage_tutorial.py       # Usage walkthrough
└── ...
```

**Guidelines:**
- Each example should be complete and runnable
- Include comments explaining key parts
- Show multiple use cases
- Keep examples small and focused

---

### `tests/`
**Purpose:** Automated tests for code quality

**Structure:**
```
tests/
├── test_scripts.py         # Unit tests
├── test_integration.py     # Integration tests
├── test_edge_cases.py      # Edge case tests
├── fixtures/               # Test data
└── ...
```

**Guidelines:**
- Test critical functionality
- Include edge cases
- Use clear test names
- Keep tests independent
- Run before committing

**Example test:**
```python
import pytest
from scripts.generate_image import process_image

def test_process_image_valid_input():
    result = process_image("test.png")
    assert result is not None
```

---

### `docs/`
**Purpose:** Extended documentation

**What goes here:**
- Contribution guidelines
- Deployment instructions
- Architecture decisions
- Advanced topics

**Structure:**
```
docs/
├── CONTRIBUTING.md         # How to contribute
├── DEPLOYMENT.md           # How to deploy
├── ARCHITECTURE.md         # System design
├── SECURITY.md             # Security guidelines
└── ...
```

---

## Root Level Files

### `CLAUDE.md`
Project instructions that Claude will follow automatically.

**Contains:**
- Project rules and guidelines
- Required skills to invoke first
- Coding standards
- Important constraints

### `README.md`
Main project documentation.

**Contains:**
- Project overview
- Quick start guide
- Installation instructions
- Key concepts
- Links to detailed docs

### `.gitignore`
Specifies files Git should ignore.

**Common patterns:**
- Environment files (.env)
- Python artifacts (__pycache__, .pyc)
- Build directories (build/, dist/)
- IDE files (.vscode, .idea)

### `.env.example`
Template for environment variables.

```env
OPENROUTER_API_KEY=your_key_here
DEBUG=false
LOG_LEVEL=info
```

---

## File Organization Best Practices

### 1. Naming Conventions
- Use kebab-case for directories: `my-feature/`
- Use snake_case for Python files: `my_script.py`
- Use UPPER_SNAKE_CASE for constants: `MAX_RETRIES`
- Use PascalCase for classes: `MyClass`

### 2. Documentation
- Every directory should have README or index
- Every script should have docstrings
- Complex logic needs comments explaining WHY
- Include examples in documentation

### 3. Modularity
- Keep concerns separated
- One file = one responsibility
- Share common code via `utils.py` or dedicated modules
- Import what you need, not everything

### 4. Scalability
- Plan ahead for growth
- Use meaningful folder names
- Create subdirectories for related files
- Document new directories

---

## Adding New Skills

When creating a new skill:

1. **Create skill directory** under `skills/` or `scripts/`
2. **Add structure:**
   ```
   my-skill/
   ├── skill.md
   ├── scripts/
   ├── references/
   └── assets/
   ```
3. **Document** in `references/SKILLS.md`
4. **Add example** in `examples/`
5. **Test** thoroughly
6. **Update** README if public-facing

---

## Maintenance

### Regular Tasks
- Review and archive old projects
- Update documentation
- Clean up unused files
- Update dependencies

### Directory Health Checklist
- [ ] All directories have clear purpose
- [ ] Documentation is current
- [ ] No orphaned files
- [ ] Naming consistent
- [ ] Structure matches README
- [ ] Examples are working
- [ ] Tests passing

---

## Migration Guide

If converting existing project:

1. Create new directories
2. Move files appropriately
3. Update imports and paths
4. Update documentation
5. Test everything works
6. Commit migration

---

## Quick Reference

| Directory | Purpose | Stores |
|-----------|---------|--------|
| `.claude/` | Configuration | settings.json |
| `scripts/` | Executable code | Python files |
| `references/` | Documentation | Markdown guides |
| `assets/` | Static files | Templates, data, icons |
| `examples/` | Working samples | Demo code |
| `tests/` | Quality assurance | Test files |
| `docs/` | Extended docs | Guides, architecture |

---

See also:
- [SKILLS.md](SKILLS.md) - How to create skills
- [CLAUDE.md](../CLAUDE.md) - Project rules
- [README.md](../README.md) - Project overview
