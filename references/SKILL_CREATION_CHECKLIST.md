# Claude Skill Creation Checklist

**Complete guide for building effective, maintainable Claude skills**

---

## 📋 Phase 1: DEFINE (Planning)

### Purpose & Scope
- [ ] **Clear purpose statement** — What is the single, core goal?
- [ ] **Scope boundaries** — What it DOES and what it DOESN'T do
- [ ] **Real-world examples** — 3+ concrete use cases
- [ ] **Target audience** — Who will use this skill?
- [ ] **Success criteria** — How to measure if it works well

### Documentation Foundation
- [ ] **Name** — Descriptive, unique, kebab-case (e.g., "code-reviewer", "text-analyzer")
- [ ] **Description** — Clear summary of functionality (2-3 sentences)
- [ ] **Features list** — What capabilities does it have?
- [ ] **Limitations documented** — Edge cases, unsupported scenarios
- [ ] **Integration points** — How it works with other skills

### Example Scenarios
- [ ] **Happy path** — Standard successful use case
- [ ] **Edge cases** — What happens with unusual input?
- [ ] **Error scenarios** — How to handle failures gracefully
- [ ] **Performance expectations** — Speed, size, complexity

---

## 📁 Phase 2: ORGANIZE (Structure)

### Directory Structure
```
skill-name/
├── skill.md                    # Metadata & documentation
├── scripts/
│   ├── main.py                 # Primary implementation
│   └── utils.py                # Helper functions (if needed)
├── references/
│   ├── README.md               # Detailed usage guide
│   ├── EXAMPLES.md             # More examples
│   └── LIMITATIONS.md          # Known constraints
├── assets/
│   └── sample_data.txt         # Test data
└── tests/
    └── test_skill.py           # Test cases
```

**Checklist:**
- [ ] `skill.md` exists with metadata
- [ ] Code in `scripts/` directory
- [ ] Documentation in `references/`
- [ ] Test data in `assets/`
- [ ] Tests in `tests/` (optional but recommended)

### Tool Selection
- [ ] **Minimum privilege principle** — Only tools absolutely needed
- [ ] **Security rationale** — Why each tool is required
- [ ] **No over-permissioning** — Avoid "just in case" tools
- [ ] **Tool alternatives considered** — Best tool for the job?

**Common tool combinations:**
- **Read-only analysis**: `read`, `grep` only
- **Code review**: `read`, `grep`, tools NOT needed
- **File generation**: `write`, `read` (rarely both)
- **Search/research**: `grep`, `search` (be specific)

Avoid: Using all tools. Use only what's necessary.

---

## ⚙️ Phase 3: IMPLEMENT (Coding)

### Code Quality
- [ ] **Under 500 lines** — Keep focused and maintainable
- [ ] **Single responsibility** — One primary purpose
- [ ] **No dependencies** — Use stdlib only (or minimal)
- [ ] **Clear naming** — Self-documenting code
- [ ] **Comments sparse** — Only for "why", not "what"

### Model Selection
| Aspect | Sonnet | Opus |
|--------|--------|------|
| **Speed** | ⚡⚡⚡ Fast | ⚡⚡ Slower |
| **Cost** | $ | $$$ |
| **Complex reasoning** | ✓ Good | ✓✓ Better |
| **Default choice** | YES | For complex logic |

- [ ] **Model justified** — Why Sonnet vs Opus?
- [ ] **Context window considered** — Is 200K enough?
- [ ] **Cost implications** — Performance/cost tradeoff
- [ ] **Version pinned** — Specific model version used

### Error Handling
- [ ] **Input validation** — Check for null, empty, wrong type
- [ ] **Graceful failures** — Don't crash on bad input
- [ ] **Error messages** — Helpful, actionable feedback
- [ ] **Fallback behaviors** — Default handling
- [ ] **Logging** — Track issues for debugging

**Example error cases:**
```python
# Bad: Crashes on empty input
result = analyze(text)

# Good: Handles empty input
if not text or len(text.strip()) == 0:
    return {"status": "error", "message": "Empty input provided"}
```

### Performance Characteristics
- [ ] **Speed target** — Expected latency (e.g., "< 2 seconds")
- [ ] **Memory usage** — Expected usage (e.g., "< 50MB")
- [ ] **Input limits** — Max size handled (e.g., "files < 1MB")
- [ ] **Scalability** — How it handles growth
- [ ] **Bottlenecks identified** — Known limitations

### Edge Cases & Limitations
- [ ] **Very short input** — What's the minimum?
- [ ] **Very long input** — What's the maximum?
- [ ] **Special characters** — Unicode, emojis, etc.
- [ ] **Language support** — English only? Or multi-language?
- [ ] **Domain limitations** — Specific to certain types of data?
- [ ] **Concurrency** — Single-threaded vs parallel safe?

---

## ✅ Phase 4: TEST & ITERATE (Validation)

### Testing
- [ ] **Happy path test** — Basic functionality works
- [ ] **Edge case tests** — Boundary conditions
- [ ] **Error case tests** — Invalid inputs handled
- [ ] **Performance tests** — Meets speed targets
- [ ] **Integration tests** — Works with other skills

**Test structure:**
```python
def test_happy_path():
    """Normal use case should work."""
    result = skill(valid_input)
    assert result is not None

def test_empty_input():
    """Empty input should be handled."""
    result = skill("")
    assert result.get("error") is not None

def test_performance():
    """Should complete in reasonable time."""
    start = time.time()
    skill(input)
    elapsed = time.time() - start
    assert elapsed < 2.0  # 2 second limit
```

- [ ] **Unit tests** exist (scripts/test_skill.py or similar)
- [ ] **Test cases documented** — What's being tested
- [ ] **Edge cases tested** — Not just happy path
- [ ] **Tests pass locally** — Before committing

### Documentation
- [ ] **Usage guide** — How to invoke the skill
- [ ] **Input format** — What data types/structure expected
- [ ] **Output format** — What result looks like
- [ ] **Examples** — 3+ concrete examples
- [ ] **Limitations section** — What doesn't work
- [ ] **Troubleshooting** — Common issues & fixes
- [ ] **Integration guide** — How it works with other skills

**Documentation files:**
- `skill.md` — Metadata + quick overview
- `references/README.md` — Detailed usage
- `references/EXAMPLES.md` — Multiple examples
- `references/LIMITATIONS.md` — Constraints & workarounds

### Output Format
- [ ] **Structured output** — Consistent JSON/dict structure
- [ ] **Schema defined** — Clear key names & types
- [ ] **Error responses** — Consistent error format
- [ ] **Validation** — Output matches expected structure
- [ ] **Parseable** — Easy for other skills to consume

**Good output format:**
```python
{
    "status": "success",  # Always include status
    "result": {...},      # Main result
    "metadata": {         # Additional info
        "processing_time_ms": 234,
        "model_used": "claude-sonnet"
    }
}
```

### Feedback & Iteration
- [ ] **User feedback collected** — How is skill actually used?
- [ ] **Common mistakes documented** — What users misunderstand?
- [ ] **Enhancement backlog** — Future improvements tracked
- [ ] **Version history** — Changes logged
- [ ] **Refinement cycle** — Plan for updates

---

## 🎯 Final Quality Check

### Before Release
- [ ] **Code passes linter** — No syntax errors
- [ ] **Tests all pass** — 100% pass rate
- [ ] **Documentation complete** — All sections filled
- [ ] **Examples work** — Tested and verified
- [ ] **No TODOs** — All planned work done
- [ ] **Performance acceptable** — Meets targets
- [ ] **Error handling robust** — Tested edge cases
- [ ] **Security reviewed** — Tool permissions appropriate

### Skill Maturity Levels

**🟢 Production Ready**
- Clear purpose, solid implementation
- Complete documentation with examples
- Tested, error handling robust
- Performance acceptable
- Ready for general use

**🟡 Beta**
- Functional but may need refinement
- Documentation present but incomplete
- Limited testing
- Feedback wanted from users

**🔴 Experimental**
- Works for basic cases
- Minimal documentation
- Limited testing
- Use with caution

---

## 📊 Quick Reference: Common Patterns

### Pattern 1: Data Analysis Skill
- **Tools needed**: `read`, `grep` (read-only)
- **Model**: Sonnet (fast, cost-effective)
- **Output**: Structured analysis results
- **Example**: Text analyzer, code reviewer

### Pattern 2: Code Generation Skill
- **Tools needed**: `write`, optionally `read`
- **Model**: Opus (complex logic needed)
- **Output**: Generated code with explanations
- **Example**: Boilerplate generator, refactorer

### Pattern 3: Search & Research Skill
- **Tools needed**: `grep`, optionally `search`
- **Model**: Sonnet
- **Output**: Findings with context
- **Example**: Codebase explorer, documentation searcher

### Pattern 4: Content Transformation
- **Tools needed**: `read`, `write`
- **Model**: Sonnet
- **Output**: Transformed content
- **Example**: Markdown formatter, code translator

---

## 🚀 Skill Launch Checklist

Before publishing your skill:

- [ ] **All tests pass** locally
- [ ] **Documentation reviewed** for clarity
- [ ] **Examples verified** to work
- [ ] **Performance benchmarked**
- [ ] **Edge cases documented**
- [ ] **Error messages user-friendly**
- [ ] **Integration points clarified**
- [ ] **Version number set**
- [ ] **Changelog documented**
- [ ] **README updated in main project**

---

## 📚 Skill Creation Template

Use this template to start a new skill:

```markdown
---
name: your-skill-name
description: |
  Brief description of what this skill does.
  
allowed-tools:
  - tool1
  - tool2

model: claude-sonnet-4-6
---

# Your Skill Name

[Your documentation here following this structure]

## Purpose
[Why this skill exists]

## Features
[What it can do]

## Usage
[How to use it]

## Implementation
[Code structure overview]

## Examples
[Concrete usage examples]

## Limitations
[What it doesn't do]

## Performance
[Speed, memory, limits]

## Testing
[How to test it]

## Integration
[How it works with other skills]
```

---

## ❓ FAQ

**Q: How long should a skill be?**
A: Under 500 lines. If longer, consider splitting into multiple skills.

**Q: Should I use all available tools?**
A: No. Use minimum required. More permissions = more security risk.

**Q: When to use Opus vs Sonnet?**
A: Default to Sonnet (fast, cheap). Use Opus only for complex reasoning.

**Q: How many examples do I need?**
A: At least 3. Show happy path, edge case, and real-world scenario.

**Q: What if my skill needs an external library?**
A: Avoid if possible. Keep dependencies minimal. Document why if needed.

**Q: How do I handle very large inputs?**
A: Document the limit. Return error if exceeded. Consider streaming for large data.

**Q: What's a good skill name?**
A: kebab-case, descriptive (not generic). Good: "code-reviewer", "text-analyzer". Bad: "tool1", "helper".

---

**Last Updated:** 2026-04-21  
**Version:** 1.0  
**Status:** Reference Guide
