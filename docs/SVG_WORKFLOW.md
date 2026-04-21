# SVG Infographic Workflow Guide

Complete step-by-step workflow for creating vector infographics with Claude and saving them as SVG files.

## Overview

```
1. Describe → 2. Generate → 3. Save → 4. View → 5. Edit (optional) → 6. Export (optional)
```

## Step 1: Describe Your Infographic

Write a detailed description of what you want to create. Include:

### Essential Details

- **Type**: What kind of infographic? (flowchart, timeline, diagram, chart, etc.)
- **Dimensions**: Size in pixels (e.g., 600x400)
- **Content**: What information should it show?
- **Colors**: Preferred color scheme or specific colors
- **Style**: Professional? Creative? Minimalist?

### Example Prompts

#### Flowchart Example
```
Create an SVG flowchart showing a user registration process.
Include:
- Start and end nodes (rounded rectangles with green/red)
- Decision diamond (is email valid?)
- Process boxes (blue rectangles)
- Arrows showing flow
- Labels for each step
- Dimensions: 500x600 pixels
- Color scheme: Professional blue (#0066CC), gray (#CCCCCC), green (#00AA00)
- Use sans-serif font, size 14-16 for labels
```

#### Timeline Example
```
Create a timeline SVG showing the evolution of web technologies.
Include:
- Vertical timeline line (center)
- 5 milestone points alternating left/right
- Year labels and technology names
- Small icons or markers for each point
- 2 colors: primary (#3498DB) and accent (#E74C3C)
- Dimensions: 400x600 pixels
- Professional corporate style
```

#### Architecture Diagram Example
```
Create a microservices architecture diagram in SVG.
Show:
- Client layer (browser icon area)
- API Gateway (center box)
- 4 microservices (blue boxes on right)
- Database (cylinder shape on far right)
- Arrows showing data flow
- Labels for each component
- Dimensions: 700x500 pixels
- Colors: Client=green, API=blue, Services=light blue, DB=orange
- Make it scalable and clean
```

## Step 2: Generate SVG with Claude

### Using Claude Code (Recommended)

1. **Open Claude Code** and navigate to your project
2. **Ask Claude** for SVG code with your description
3. **Example Request**:
   ```
   Generate SVG code for a timeline showing project milestones.
   Include 4 milestones with dates and descriptions.
   Use blue (#0066CC) as primary color.
   Make it 500x400 pixels with viewBox="0 0 500 400"
   ```

### Tips for Better Results

✅ **Be Specific**: "rounded blue rectangles" vs "boxes"
✅ **Mention Dimensions**: "600x400" helps Claude size elements correctly
✅ **Reference Style**: "minimalist", "professional", "playful"
✅ **Include Colors**: Specific hex codes get better results
✅ **Describe Layout**: "centered title, 3 columns below" helps structure
✅ **Request Groups**: Ask Claude to use `<g id="...">` for organization

## Step 3: Save SVG Code

### Method 1: Using SVG Generator Script (Recommended)

**Copy Claude's SVG code, then run:**

```bash
python scripts/svg_generator.py my_infographic.svg --validate
```

**Then paste the SVG code when prompted.**

### Method 2: Pipe from File

```bash
python scripts/svg_generator.py output.svg --validate < code.txt
```

### Method 3: Direct Echo

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg" ...>...</svg>' | \
  python scripts/svg_generator.py infographic.svg --validate
```

### Script Output

Successful save will show:
```
✅ SVG saved successfully!
   📁 File: /home/user/claude_tests/infographic.svg
   📊 Size: 12.34 KB (12345 bytes)
   🌐 Open in browser: file:///home/user/claude_tests/infographic.svg
```

## Step 4: View in Browser

### Opening the SVG

#### Option A: Direct Open
```bash
# macOS
open infographic.svg

# Linux
firefox infographic.svg
xdg-open infographic.svg

# Windows
# Double-click the .svg file
```

#### Option B: Local Server (for advanced features)
```bash
# Python 3
python -m http.server 8000

# Then visit: http://localhost:8000/infographic.svg
```

### Checking the Result

- [ ] SVG displays without errors
- [ ] All elements are visible
- [ ] Colors match expectations
- [ ] Text is readable
- [ ] Layout matches description
- [ ] No distortion or stretching

## Step 5: Edit (Optional)

### Using Inkscape (Free & Professional)

1. **Download**: https://inkscape.org
2. **Open**: `File → Open` → select your SVG
3. **Edit**:
   - Select elements with selection tool
   - Drag to move
   - Click properties to change colors, fonts
   - Right-click for context menu
4. **Save**: `File → Save As` → keep as SVG

### Using Figma (Free Tier)

1. **Go to**: https://figma.com
2. **Create Project** or open existing
3. **Import**: `File → Import file` → your SVG
4. **Edit**: Drag, resize, change colors
5. **Export**: Right-click → Download as SVG

### Using Online Editor

- **Boxy SVG**: https://boxy-svg.com (open SVG, edit visually)
- **Gravit Designer**: https://gravit.io (web-based)

### What Can You Edit?

- ✅ Colors and fills
- ✅ Text content and fonts
- ✅ Element sizes and positions
- ✅ Stroke widths
- ✅ Opacity and transparency
- ✅ Add new shapes or text
- ✅ Group and ungroup elements

## Step 6: Export (Optional)

### Export to PNG

**Best for**: Sharing, embedding in web pages, presentations

```bash
# Using Inkscape
inkscape infographic.svg -o infographic.png

# Using online converter
# https://convertio.co/svg-png/
```

**Quality Settings**:
- DPI: 96 (web), 300 (print)
- Background: transparent or white

### Export to PDF

**Best for**: Printing, high-quality archive

```bash
# Using Inkscape
inkscape infographic.svg -o infographic.pdf

# Or print to PDF from browser
# Open SVG in browser → Print → Save as PDF
```

### Export to Other Formats

| Format | Best For | Tool |
|--------|----------|------|
| PNG | Web, presentations | Inkscape, online |
| PDF | Printing, documents | Inkscape, browser |
| JPG | Email, small file | Online converter |
| TIFF | Professional printing | Inkscape |
| WebP | Modern web | Online converter |

## Complete Workflow Example

### 1. Request
```
I need an infographic showing the project structure of a Claude skills repository.
Include sections for: scripts/, references/, examples/, assets/, tests/, docs/.
Each section should be a box with title and brief description.
Use professional colors: primary blue #0066CC, secondary gray #CCCCCC.
Dimensions: 700x400 pixels.
Arrange in 2 rows of 3 boxes with connecting lines to a central "Project" node.
```

### 2. Claude Generates
Claude writes SVG code with proper structure, groups, and styling.

### 3. Save
```bash
python scripts/svg_generator.py project_structure.svg --validate
# Paste SVG code
```

### 4. View
```bash
open project_structure.svg
# SVG opens in browser, looks good!
```

### 5. Edit (Optional)
- Open in Inkscape
- Change colors to match brand
- Update labels
- Adjust spacing
- Save as SVG

### 6. Export (Optional)
```bash
inkscape project_structure.svg -o project_structure.png
# PNG is ready for presentations
```

## Workflow Shortcuts

### Quick Save & View
```bash
# Save and immediately open in browser
python scripts/svg_generator.py out.svg && open out.svg
```

### Batch Processing
```bash
# Create multiple infographics
for i in 1 2 3; do
  python scripts/svg_generator.py infographic_$i.svg
done
```

### Validation Only
```bash
# Check if SVG is valid without saving
python scripts/svg_generator.py output.svg --validate < draft.svg
```

## Troubleshooting

### SVG Won't Save

**Error**: "SVG content is empty"
- **Solution**: Make sure you copied the complete SVG code including `<svg>` and `</svg>` tags

**Error**: "Permission denied"
- **Solution**: Check directory permissions, try saving to different location

### SVG Won't Display

**Problem**: Opens as text file instead of image
- **Solution**: Ensure file has `.svg` extension

**Problem**: Shows as blank in browser
- **Solution**: 
  - Check browser console for errors
  - Verify SVG has viewBox or width/height
  - Ensure fill colors are set

### Colors Appear Wrong

**Problem**: Colors don't match expectation
- **Solution**: 
  - Edit in Inkscape and change colors directly
  - Ask Claude to regenerate with specific hex codes
  - Use color picker tool to find exact colors

### Text is Too Small/Large

**Problem**: Text doesn't fit or is hard to read
- **Solution**:
  - Edit font-size in SVG code
  - Or open in Inkscape and adjust with text tool
  - Ask Claude to regenerate with specific font-size

## Best Practices

### During Creation
- ✅ Describe clearly with dimensions
- ✅ Request specific colors (hex codes)
- ✅ Ask for clean, organized structure
- ✅ Request meaningful IDs and groups
- ✅ Mention accessibility needs

### After Generation
- ✅ Validate SVG before saving
- ✅ View in browser immediately
- ✅ Test responsiveness
- ✅ Keep SVG file in version control
- ✅ Document the generation prompt

### For Reuse
- ✅ Save SVG with descriptive filename
- ✅ Add to examples/ or assets/
- ✅ Document what the infographic shows
- ✅ Keep source prompt for regeneration
- ✅ Version your infographics

## Files to Organize

### Project Structure
```
examples/
├── skill-creation.svg        # How to create skills
├── project-structure.svg     # Directory tree
├── workflow.svg              # Process flow
└── timeline.svg              # Timeline example

assets/svg-templates/
├── infographic-template.svg  # Reusable template
├── flowchart-template.svg    # Flow template
├── timeline-template.svg     # Timeline template
└── chart-template.svg        # Chart template
```

### Naming Convention
- Use descriptive names: `user-flow.svg`, not `diagram1.svg`
- Use lowercase with hyphens: `my-infographic.svg`
- Include content type: `*-timeline.svg`, `*-flowchart.svg`

## Performance Tips

### File Size
- Remove unnecessary decimal places
- Use shorthand notation in paths
- Consolidate similar styling
- Remove comments before finalizing

### Rendering
- Test with large viewBox dimensions
- Simplify complex paths
- Limit number of elements
- Use symbols for repeated elements

## Next Steps

- **Learn More**: See [SVG_INFOGRAPHICS.md](../references/SVG_INFOGRAPHICS.md) for technical details
- **Quick Start**: See [SVG_QUICK_START.md](SVG_QUICK_START.md) for fast onboarding
- **Examples**: Check `/examples/` for working SVG samples
- **Templates**: Use `/assets/svg-templates/` for starting points

---

**Pro Tip**: Save your SVG generation prompts! If you need to regenerate or modify an infographic later, you'll have the original description ready.
