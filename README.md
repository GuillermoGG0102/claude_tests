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

### Quick Start: Create SVG Infographics (Free!)

1. **Clone the repository**
   ```bash
   git clone https://github.com/GuillermoGG0102/claude_tests.git
   cd claude_tests
   ```

2. **Ask Claude for SVG code**
   ```
   "Create an SVG flowchart showing a simple process with 3 steps.
    Use professional colors and make it 500x400 pixels."
   ```

3. **Save with SVG generator** (no dependencies needed!)
   ```bash
   python scripts/svg_generator.py my_infographic.svg
   # Paste Claude's SVG code when prompted
   ```

4. **Open in browser**
   ```bash
   open my_infographic.svg
   ```

✅ That's it! No API keys, no costs, completely free vector graphics.

See [docs/SVG_QUICK_START.md](docs/SVG_QUICK_START.md) for more examples.

## 📚 Key Directories

### `scripts/`
Executable Python scripts and utilities. Keep implementations under 500 lines where possible.

Examples:
```bash
python scripts/svg_generator.py my_infographic.svg    # Save SVG code to files
```

### `references/`
Documentation, guides, and how-tos. Includes:
- Skill creation guides
- SVG infographic guides
- API documentation
- Setup instructions
- Troubleshooting guides

### `assets/`
Static files including:
- SVG templates for quick creation
- Icons and images
- JSON templates
- Sample data
- Configuration templates

### `examples/`
Working examples of skills and infographics:
- SVG infographic samples
- Skill implementations
- Project structure diagrams

### `tests/`
Unit tests and integration tests for validating code
- Test suite for SVG generator

### `docs/`
Additional documentation:
- SVG workflow guide
- SVG quick start guide
- Contributing guidelines

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

### Skills Development
- [CLAUDE.md](CLAUDE.md) — Project rules and instructions
- [references/SKILLS.md](references/SKILLS.md) — How to create Claude skills
- [references/PROJECT_STRUCTURE.md](references/PROJECT_STRUCTURE.md) — Detailed structure guide
- [CLAUDE_SKILLS_INFOGRAPHIC.md](CLAUDE_SKILLS_INFOGRAPHIC.md) — Visual guide to creating skills

### SVG Infographics (Free, No APIs)
- [references/SVG_INFOGRAPHICS.md](references/SVG_INFOGRAPHICS.md) — Comprehensive SVG technical guide
- [docs/SVG_WORKFLOW.md](docs/SVG_WORKFLOW.md) — Complete step-by-step workflow
- [docs/SVG_QUICK_START.md](docs/SVG_QUICK_START.md) — 5-minute quick start guide
- [examples/](examples/) — Working SVG examples (project-structure, workflow, timeline)

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
