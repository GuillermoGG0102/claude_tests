# 🎨 How to Create Claude Skills — Infographic Guide

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                     🛠️  HOW TO CREATE CLAUDE SKILLS 🛠️                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝


┌──────────────────────────────────────────────────────────────────────────────┐
│                          📏 SIZE CONSTRAINT                                   │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                          ┌─────────────────┐                                │
│                          │  < 500 LINES  │                                  │
│                          └─────────────────┘                                │
│                                                                              │
│                    Keep your skill code concise and focused                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────┐
│              ⭐ MANDATORY FIELDS (Required in Every Skill)                    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  name:                                                                  │ │
│  │  └─→ Name of the skill (concise identifier)                            │ │
│  │      Example: "code-review", "image-generator", "api-debugger"        │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  description:                                                           │ │
│  │  └─→ What the skill does (its expertise knowledge)                     │ │
│  │      Example: "Reviews code for bugs, performance, and best practices" │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────┐
│            💡 OPTIONAL FIELDS (Customize as Needed)                          │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  allowed-tools:  [OPTIONAL]                                            │ │
│  │  └─→ What tools your skill can use                                    │ │
│  │      Example: ["bash", "read", "grep", "github"]                     │ │
│  │                                                                        │ │
│  │  ℹ️  Scope what integrations your skill needs                        │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  model:  [OPTIONAL]                                                    │ │
│  │  └─→ What model should be used for this skill                         │ │
│  │      Example: "claude-opus-4-7", "claude-sonnet-4-6"                 │ │
│  │                                                                        │ │
│  │  ℹ️  Specify if your skill requires specific model capabilities      │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────┐
│              📁 RECOMMENDED DIRECTORY STRUCTURE                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  my-skill/                                                                  │
│  │                                                                          │
│  ├── 📄 skill.md                    ← Skill definition with metadata       │
│  │                                                                          │
│  ├── 📂 scripts/                    ← Executable code                      │
│  │   ├── main.py                                                          │
│  │   ├── helper.py                                                        │
│  │   └── utils.py                                                         │
│  │                                                                          │
│  ├── 📂 references/                 ← Additional documentation             │
│  │   ├── API_GUIDE.md                                                     │
│  │   ├── EXAMPLES.md                                                      │
│  │   └── TROUBLESHOOTING.md                                               │
│  │                                                                          │
│  └── 📂 assets/                     ← Images, templates, data files       │
│      ├── icon.png                                                         │
│      ├── template.json                                                    │
│      └── sample_data.csv                                                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────┐
│                    ✅ SKILL DEFINITION EXAMPLE                               │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ---                                                                        │
│  name: code-review                                                          │
│  description: Analyzes code for bugs, performance issues, and best          │
│  practices, providing detailed feedback and suggestions                     │
│                                                                              │
│  allowed-tools:                                                             │
│    - bash                                                                   │
│    - read                                                                   │
│    - grep                                                                   │
│                                                                              │
│  model: claude-opus-4-7                                                     │
│  ---                                                                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────┐
│                         💭 BEST PRACTICES                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ✓ Keep skill focused on ONE primary task                                  │
│  ✓ Write clear, descriptive names and descriptions                         │
│  ✓ Only specify tools and models if truly necessary                        │
│  ✓ Organize code logically within scripts/ directory                       │
│  ✓ Document usage with examples in references/                             │
│  ✓ Stay under 500 lines of code                                            │
│  ✓ Make skills reusable and composable                                     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

```

---

## Quick Start Checklist

- [ ] Define your skill name and description
- [ ] Create skill.md with metadata
- [ ] Add executable code to scripts/
- [ ] Add documentation to references/
- [ ] Include assets if needed
- [ ] Keep code under 500 lines
- [ ] Test skill functionality
- [ ] Deploy and verify

---

**Created**: April 21, 2026  
**Purpose**: Visual guide for creating Claude skills
