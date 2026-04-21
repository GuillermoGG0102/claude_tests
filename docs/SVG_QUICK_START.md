# SVG Quick Start Guide

**Get started creating vector infographics in 5 minutes.**

## TL;DR

1. **Ask Claude** for SVG code
2. **Copy the code** Claude generates
3. **Run**: `python scripts/svg_generator.py output.svg`
4. **Paste** the SVG code
5. **Open**: The `.svg` file in your browser

That's it! You now have a professional vector infographic.

---

## The 5-Minute Workflow

### 1. Ask Claude (30 seconds)

Talk to Claude in plain English:

```
Create an SVG flowchart showing a simple decision process:
- Start (green)
- Decision diamond (yellow)  
- Action 1 (blue)
- Action 2 (blue)
- End (red)
Connect with arrows.
Make it 400x500 pixels.
Professional style.
```

### 2. Claude Generates SVG (1 minute)

Claude will provide SVG code that looks like:
```xml
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="500" viewBox="0 0 400 500">
  <!-- Your infographic code here -->
</svg>
```

### 3. Copy the Code (10 seconds)

Select and copy Claude's entire SVG code block (from `<svg` to `</svg>`).

### 4. Save with Script (10 seconds)

```bash
python scripts/svg_generator.py my_flowchart.svg
```

When prompted, paste the SVG code and press Ctrl+D (or Cmd+D on Mac).

### 5. View in Browser (10 seconds)

```bash
open my_flowchart.svg
```

**Done!** Your infographic appears in the browser.

---

## Common Requests

### Simple Timeline
```
Create a 5-year timeline showing milestones.
Include: 2020, 2021, 2022, 2023, 2024
Show points on a horizontal line.
Add brief labels below each point.
Use blue and gray colors.
Make it 600x150 pixels.
```

### Organization Chart
```
Create an organization chart showing:
- CEO at top
- 3 directors below
- 2 managers under each director
Use boxes connected by lines.
Professional corporate style.
Make it 600x400 pixels.
```

### Process Flow
```
Show a data processing pipeline:
Input → Validation → Processing → Storage → Output
Use boxes and arrows.
Make it 700x200 pixels.
Professional technical style.
```

### Comparison Diagram
```
Create a 2-column comparison of Option A vs Option B.
List 5 features in each column.
Use checkmarks for pros, X marks for cons.
Make it 500x400 pixels.
```

---

## Editing Your SVG

### Change Colors

1. Open `.svg` file in text editor
2. Find the color value (e.g., `fill="blue"`)
3. Replace with new color
   - `fill="red"` for red
   - `fill="#0066CC"` for custom blue
   - `fill="rgb(100, 150, 200)"` for RGB
4. Save and refresh browser

### Change Text

1. Find `<text>` tag in SVG code
2. Change the text between the tags
3. Save and refresh

### Change Size

Option A: Use browser zoom (Ctrl/Cmd + or -)

Option B: Edit SVG attributes
```xml
<!-- Change this -->
<svg width="400" height="300" ...>

<!-- To this for 2x larger -->
<svg width="800" height="600" ...>
```

### Undo Bad Changes

1. Delete your modified `.svg` file
2. Ask Claude to regenerate
3. Save again

---

## Free Editing Tools

### Just Want to View?
- Any web browser
- Just open the `.svg` file

### Want to Edit Visually?
- **Inkscape** (free, professional)
  - Download: https://inkscape.org
  - Open SVG → Edit visually → Save

- **Figma** (free tier)
  - Go to https://figma.com
  - Import SVG → Edit → Export

### Want to Edit Code?
- Any text editor (VS Code, Sublime, etc.)
- Edit SVG XML directly
- Save and refresh browser

---

## Troubleshooting

**SVG won't save**
→ Make sure you copied the ENTIRE SVG code including `<svg>` and `</svg>`

**SVG appears blank**
→ Open browser Developer Tools (F12), check Console for errors

**Colors don't show**
→ Make sure SVG has `fill="color"` attributes

**Text too small**
→ Ask Claude to increase `font-size` or edit manually in text editor

**Want to redo it**
→ Delete the file, ask Claude again, save again

---

## Next Time

Once you're comfortable, check out:
- [SVG_WORKFLOW.md](SVG_WORKFLOW.md) - Full detailed workflow
- [SVG_INFOGRAPHICS.md](../references/SVG_INFOGRAPHICS.md) - Technical reference
- `/examples/` - Working examples you can learn from
- `/assets/svg-templates/` - Templates to build from

---

## That's It!

You now know how to:
- ✅ Ask Claude for SVG infographics
- ✅ Save SVG code to files
- ✅ View SVG in your browser
- ✅ Make basic edits
- ✅ Use free editing tools

**Happy diagramming!** 🎨
