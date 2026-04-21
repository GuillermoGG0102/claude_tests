#!/usr/bin/env python3
"""
Create a professional PNG infographic for LinkedIn sharing.
Dependencies: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

# Dimensions optimized for LinkedIn (600px wide)
WIDTH = 600
HEIGHT = 1200
BG_COLOR = (255, 255, 255)  # White
PRIMARY_COLOR = (102, 126, 234)  # Blue (#667eea)
SECONDARY_COLOR = (118, 75, 162)  # Purple (#764ba2)
ACCENT_COLOR = (245, 87, 108)  # Pink (#f5576c)
TEXT_DARK = (51, 51, 51)  # Dark gray
TEXT_LIGHT = (102, 102, 102)  # Light gray

# Create image
img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# Create gradient header (blue to purple)
for y in range(100):
    ratio = y / 100
    r = int(102 + (118 - 102) * ratio)
    g = int(126 + (75 - 126) * ratio)
    b = int(234 + (162 - 234) * ratio)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

# Header
y_pos = 30
# Emoji as text (using Unicode)
draw.text((WIDTH // 2 - 20, y_pos), "🛠️", fill=(255, 255, 255), anchor="lm")
y_pos += 50

# Title
draw.text((WIDTH // 2, y_pos), "How to Create", fill=(255, 255, 255), anchor="mm")
y_pos += 35
draw.text((WIDTH // 2, y_pos), "Claude Skills", fill=(255, 255, 255), anchor="mm")
y_pos += 25
draw.text((WIDTH // 2, y_pos), "A Step-by-Step Guide", fill=(255, 255, 255), anchor="mm", font=None)

y_pos += 60

# Size badge
badge_y = y_pos
badge_height = 50
# Draw rounded rectangle for badge (approximation)
draw.rectangle(
    [(WIDTH // 2 - 100, badge_y), (WIDTH // 2 + 100, badge_y + badge_height)],
    fill=PRIMARY_COLOR,
    outline=None
)
draw.text((WIDTH // 2, badge_y + 25), "< 500 LINES", fill=(255, 255, 255), anchor="mm")
y_pos += badge_height + 20

# Subtitle
draw.text((WIDTH // 2, y_pos), "Keep your skill focused and maintainable",
          fill=TEXT_LIGHT, anchor="mm")
y_pos += 50

# Separator
draw.line([(30, y_pos), (WIDTH - 30, y_pos)], fill=(240, 240, 240), width=2)
y_pos += 40

# Step 1
draw.ellipse([(40, y_pos - 15), (60, y_pos + 5)], fill=PRIMARY_COLOR)
draw.text((50, y_pos - 5), "1", fill=(255, 255, 255), anchor="mm")
draw.text((75, y_pos - 15), "Define Your Skill 📝", fill=TEXT_DARK, anchor="lm")
y_pos += 35
draw.text((75, y_pos), "name: Concise identifier", fill=TEXT_DARK, anchor="lm")
y_pos += 22
draw.text((75, y_pos), '"code-review", "api-debugger"', fill=TEXT_LIGHT, anchor="lm")
y_pos += 30
draw.text((75, y_pos), "description: What it does", fill=TEXT_DARK, anchor="lm")
y_pos += 22
draw.text((75, y_pos), '"Analyzes code for bugs"', fill=TEXT_LIGHT, anchor="lm")
y_pos += 50

# Step 2
draw.ellipse([(40, y_pos - 15), (60, y_pos + 5)], fill=SECONDARY_COLOR)
draw.text((50, y_pos - 5), "2", fill=(255, 255, 255), anchor="mm")
draw.text((75, y_pos - 15), "Organize Files 📁", fill=TEXT_DARK, anchor="lm")
y_pos += 35
draw.text((75, y_pos), "📄 skill.md - Metadata", fill=TEXT_DARK, anchor="lm")
y_pos += 22
draw.text((75, y_pos), "🐍 scripts/ - Your code", fill=TEXT_DARK, anchor="lm")
y_pos += 22
draw.text((75, y_pos), "📖 references/ - Docs", fill=TEXT_DARK, anchor="lm")
y_pos += 22
draw.text((75, y_pos), "🎨 assets/ - Data & icons", fill=TEXT_DARK, anchor="lm")
y_pos += 50

# Step 3
draw.ellipse([(40, y_pos - 15), (60, y_pos + 5)], fill=SECONDARY_COLOR)
draw.text((50, y_pos - 5), "3", fill=(255, 255, 255), anchor="mm")
draw.text((75, y_pos - 15), "Customize (Optional) ⚙️", fill=TEXT_DARK, anchor="lm")
y_pos += 35
draw.text((75, y_pos), "allowed-tools: What it can access", fill=TEXT_DARK, anchor="lm")
y_pos += 22
draw.text((75, y_pos), "model: Which Claude to use", fill=TEXT_DARK, anchor="lm")
y_pos += 60

# Best Practices Section
draw.text((WIDTH // 2, y_pos), "✅ Best Practices", fill=TEXT_DARK, anchor="mm")
y_pos += 40

practices = [
    ("🎯", "One Primary Task"),
    ("📝", "Clear Names"),
    ("🔧", "Only Needed Tools"),
    ("📚", "Document Well"),
]

practices_y = y_pos
for i, (emoji, text) in enumerate(practices):
    x = 50 if i % 2 == 0 else WIDTH // 2 + 50
    y = practices_y + (i // 2) * 40
    draw.text((x, y), f"{emoji} {text}", fill=TEXT_DARK, anchor="lm")

y_pos += 100

# CTA Section
cta_y = y_pos
# Draw CTA background
draw.rectangle([(30, cta_y), (WIDTH - 30, cta_y + 80)],
               fill=PRIMARY_COLOR, outline=None)
draw.text((WIDTH // 2, cta_y + 20), "🚀 Ready to Build?",
          fill=(255, 255, 255), anchor="mm")
draw.text((WIDTH // 2, cta_y + 50), "Start with your skill definition today",
          fill=(255, 255, 255), anchor="mm")

y_pos += 100

# Footer
draw.text((WIDTH // 2, y_pos), "Claude Skills Guide",
          fill=PRIMARY_COLOR, anchor="mm")

# Save
img.save('examples/claude-skills-infographic.png')
print("✅ Infographic saved: examples/claude-skills-infographic.png")
print("📊 Size: 600x1200px (LinkedIn optimized)")
print("📤 Ready to upload to LinkedIn!")
