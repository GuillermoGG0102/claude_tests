# Claude Tests & Skills Project

A structured repository for developing, testing, and documenting Claude skills and integrations.

## 📁 Project Structure

```
.
├── .claude/              # Claude configuration
│   └── settings.json     # Claude Code settings
├── scripts/              # Executable code and utilities
│   ├── generate_image.py # AI image generation script
│   └── ...
├── references/           # Documentation and guides
│   ├── SKILLS.md         # Guide to creating skills
│   ├── PROJECT_STRUCTURE.md
│   └── ...
├── assets/               # Images, templates, data files
│   ├── templates/
│   ├── icons/
│   └── ...
├── examples/             # Example implementations
│   └── hello-skill.md    # Example skill definition
├── tests/                # Test files
├── docs/                 # Additional documentation
├── CLAUDE.md             # Project instructions for Claude
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites
- Claude Code installed
- Python 3.8+ (for scripts)
- OpenRouter API key (for image generation)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/GuillermoGG0102/claude_tests.git
   cd claude_tests
   ```

2. **Configure environment** (if using image generation)
   ```bash
   cp .env.example .env
   # Add your OpenRouter API key to .env
   ```

3. **Install dependencies** (if needed)
   ```bash
   pip install -r requirements.txt  # if it exists
   ```

## 📚 Key Directories

### `scripts/`
Executable Python scripts and utilities. Keep implementations under 500 lines where possible.

Example:
```bash
python scripts/generate_image.py "A beautiful sunset"
```

### `references/`
Documentation, guides, and how-tos. Includes:
- Skill creation guides
- API documentation
- Setup instructions
- Troubleshooting guides

### `assets/`
Static files including:
- Icons and images
- JSON templates
- Sample data
- Configuration templates

### `examples/`
Working examples of skills and implementations

### `tests/`
Unit tests and integration tests for validating code

### `docs/`
Additional documentation beyond references

## 🛠️ Creating a Skill

See [references/SKILLS.md](references/SKILLS.md) for detailed instructions on creating Claude skills.

Quick checklist:
- [ ] Define `name` and `description`
- [ ] Create skill directory with `scripts/`, `references/`, `assets/` subdirs
- [ ] Keep code under 500 lines
- [ ] Add documentation in `references/`
- [ ] Include examples in `examples/`

## 🤖 Using Claude Code

This project is optimized for Claude Code. Key files:
- **CLAUDE.md** — Project instructions and rules
- **.claude/settings.json** — Claude Code configuration

Claude will automatically follow instructions in `CLAUDE.md` when working on this project.

## 📖 Documentation

- [CLAUDE.md](CLAUDE.md) — Project rules and instructions
- [references/SKILLS.md](references/SKILLS.md) — How to create skills
- [references/PROJECT_STRUCTURE.md](references/PROJECT_STRUCTURE.md) — Detailed structure guide
- [CLAUDE_SKILLS_INFOGRAPHIC.md](CLAUDE_SKILLS_INFOGRAPHIC.md) — Visual guide

## 🔧 Configuration

### Claude Code Settings

Configuration is managed in `.claude/settings.json`. Common settings:
- Model selection
- Tool permissions
- Hook configurations
- Path exclusions

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

When contributing:
1. Follow the project structure
2. Keep skills under 500 lines
3. Add documentation to `references/`
4. Include examples in `examples/`
5. Update this README if adding new directories

## 📞 Support

For questions about Claude Code, visit: https://github.com/anthropics/claude-code/issues
