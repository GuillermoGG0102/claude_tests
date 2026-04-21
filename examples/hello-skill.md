---
name: text-analyzer
description: |
  Analyzes text for various characteristics including:
  - Word count and reading time
  - Sentiment analysis
  - Readability metrics
  - Common patterns and statistics

allowed-tools:
  - read
  - grep

model: claude-sonnet-4-6
---

# Text Analyzer Skill

A simple, focused skill that demonstrates Claude skill structure and conventions.

## Purpose

This skill teaches Claude how to deeply analyze text content and provide meaningful insights about readability, sentiment, and content characteristics.

## Features

### Word & Readability Analysis
- Total word count
- Unique word count
- Average word length
- Estimated reading time
- Flesch-Kincaid grade level

### Sentiment & Tone
- Overall sentiment (positive/negative/neutral)
- Emotional tone
- Emphasis patterns
- Formality level

### Content Patterns
- Most common words
- Key phrases
- Topic clustering
- Length distribution

## Usage

### Basic Analysis
```
Analyze this text for readability and sentiment:
"The quick brown fox jumps over the lazy dog. This is a sample text..."
```

### File Analysis
```
Read the file at references/sample.txt and provide full analysis
```

### Comparative Analysis
```
Compare the readability of these two texts:
Text A: ...
Text B: ...
```

## Implementation

The skill is implemented in `scripts/text_analyzer.py` (~150 lines):

```python
def analyze_text(text: str) -> dict:
    """Analyze text and return metrics."""
    
def calculate_readability(text: str) -> float:
    """Calculate Flesch-Kincaid score."""
    
def analyze_sentiment(text: str) -> str:
    """Determine sentiment (positive/neutral/negative)."""
    
def find_patterns(text: str) -> dict:
    """Find common words and phrases."""
```

## Examples

### Example 1: Blog Post Analysis
**Input:** Blog post about machine learning
**Output:**
- Reading time: 5 minutes
- Grade level: 12 (college)
- Sentiment: Informative, positive
- Key phrases: "machine learning", "neural networks", "data science"

### Example 2: Email Analysis
**Input:** Professional email
**Output:**
- Reading time: 1 minute
- Grade level: 8
- Sentiment: Neutral, professional
- Common words: Thank you, please, regards

### Example 3: Comparative Analysis
**Input:** Two product descriptions
**Output:**
- Text A is more formal and technical
- Text B is more casual and persuasive
- Text A targets experts, Text B targets general audience

## How to Use This Skill

1. **Invoke the skill** when you need text analysis
2. **Provide text** as input (directly or via file)
3. **Get detailed analysis** with metrics and insights
4. **Ask follow-up questions** for deeper understanding

## Common Use Cases

- **Readability optimization**: Ensure content is at right reading level
- **Tone matching**: Adjust writing to match brand voice
- **Quality assessment**: Evaluate content before publishing
- **Comparative analysis**: Compare different versions or authors
- **Accessibility**: Ensure content is accessible to target audience

## Limitations & Edge Cases

- Very short texts (<50 words) may have skewed metrics
- Sentiment analysis works best for English
- Grade level estimates are approximate
- Specialized jargon may not be recognized

## Integration with Other Skills

This skill pairs well with:
- **Writing Assistant**: For improving based on analysis
- **Grammar Checker**: For language quality
- **SEO Analyzer**: For content optimization
- **Translator**: For multi-language content

## Performance Characteristics

- Analysis time: <1 second for typical text
- Handles texts up to 100,000 words
- Memory efficient: ~1MB per analysis

## Future Enhancements

- [ ] Multi-language support
- [ ] Topic modeling
- [ ] Audience detection
- [ ] Style matching
- [ ] Plagiarism detection

## Code Structure

```
text-analyzer/
├── skill.md                    # This file
├── scripts/
│   ├── text_analyzer.py        # Main implementation
│   └── utils.py                # Helper functions
├── references/
│   ├── README.md               # Detailed guide
│   └── EXAMPLES.md             # More examples
└── assets/
    └── sample_texts.txt        # Test data
```

## Testing

Example test cases:
```python
def test_word_count():
    text = "Hello world"
    assert count_words(text) == 2

def test_sentiment():
    text = "I love this!"
    assert analyze_sentiment(text) == "positive"
```

## Related Documentation

- [SKILLS.md](../references/SKILLS.md) - How to create skills
- [PROJECT_STRUCTURE.md](../references/PROJECT_STRUCTURE.md) - Project organization
- [CLAUDE_SKILLS_INFOGRAPHIC.md](../CLAUDE_SKILLS_INFOGRAPHIC.md) - Visual guide

## Quick Checklist

This skill demonstrates:
- ✓ Clear name and description
- ✓ Focused functionality (text analysis only)
- ✓ Proper directory structure
- ✓ Documented features and examples
- ✓ Code under 500 lines
- ✓ Multiple use cases
- ✓ Edge case handling
- ✓ Integration possibilities

---

**Last Updated:** 2026-04-21
**Status:** Example/Template
**License:** MIT
