# SVG Infographics Guide

Complete guide to creating professional vector infographics using SVG (Scalable Vector Graphics) with Claude.

## What is SVG?

**SVG** (Scalable Vector Graphics) is an XML-based format for creating 2D graphics that can scale infinitely without losing quality.

### Key Advantages

✅ **Scalable** — Resize from 10px to 10000px without quality loss
✅ **Small File Size** — Text-based format compresses well
✅ **Editable** — Can be modified with code or visual tools
✅ **Interactive** — Can add animation, interactivity with CSS/JavaScript
✅ **Accessible** — Text-based, searchable, SEO-friendly
✅ **Free** — Open standard, no licensing costs
✅ **Universal** — Works in all modern browsers

## Basic SVG Structure

### Minimal SVG Document

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <!-- Content goes here -->
</svg>
```

### Core Attributes

- **xmlns** — XML namespace (required)
- **width/height** — Display size in pixels
- **viewBox** — "minX minY width height" coordinate system
- **preserveAspectRatio** — How to scale content

### Coordinate System

```
(0,0) -----> X increases right
  |
  |
  v Y increases down
```

## Common SVG Elements

### Shapes

```xml
<!-- Rectangle -->
<rect x="10" y="10" width="100" height="50" fill="blue"/>

<!-- Circle -->
<circle cx="100" cy="100" r="50" fill="red"/>

<!-- Ellipse -->
<ellipse cx="100" cy="100" rx="80" ry="50" fill="green"/>

<!-- Line -->
<line x1="0" y1="0" x2="100" y2="100" stroke="black" stroke-width="2"/>

<!-- Polygon -->
<polygon points="100,10 40,198 190,78" fill="purple"/>

<!-- Path -->
<path d="M 10 10 L 90 90 Q 90 10 10 10 Z" fill="orange"/>
```

### Text

```xml
<text x="50" y="50" font-size="20" fill="black">Hello SVG</text>

<text x="50" y="50" font-size="20" text-anchor="middle" fill="black">
  Centered Text
</text>
```

### Groups

```xml
<g id="my-group" fill="blue" opacity="0.8">
  <circle cx="50" cy="50" r="30"/>
  <rect x="10" y="10" width="80" height="80"/>
</g>
```

## Styling SVG

### Fill and Stroke

```xml
<!-- Solid colors -->
<rect fill="red" stroke="black" stroke-width="2"/>

<!-- Named colors -->
<circle fill="lightblue" stroke="darkblue"/>

<!-- Hex colors -->
<rect fill="#FF5733" stroke="#333333"/>

<!-- No fill -->
<circle fill="none" stroke="black" stroke-width="2"/>

<!-- Transparency -->
<rect fill="red" opacity="0.5"/>
```

### Color Values

- **Named**: `red`, `blue`, `lightgreen`, `darkviolet`
- **Hex**: `#FF0000`, `#00FF00`, `#0000FF`
- **RGB**: `rgb(255, 0, 0)`, `rgb(0, 255, 0)`
- **RGBA**: `rgba(255, 0, 0, 0.5)`

### Text Styling

```xml
<text font-family="Arial, sans-serif" 
      font-size="24" 
      font-weight="bold" 
      fill="black">
  Styled Text
</text>

<text font-style="italic" 
      font-variant="small-caps" 
      fill="navy">
  Fancy Text
</text>
```

## Creating Infographics

### 1. Simple Timeline

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="100" viewBox="0 0 400 100">
  <!-- Timeline line -->
  <line x1="20" y1="50" x2="380" y2="50" stroke="black" stroke-width="2"/>
  
  <!-- Points -->
  <circle cx="50" cy="50" r="8" fill="blue"/>
  <circle cx="150" cy="50" r="8" fill="blue"/>
  <circle cx="250" cy="50" r="8" fill="blue"/>
  <circle cx="350" cy="50" r="8" fill="blue"/>
  
  <!-- Labels -->
  <text x="50" y="80" text-anchor="middle" font-size="12">2020</text>
  <text x="150" y="80" text-anchor="middle" font-size="12">2021</text>
  <text x="250" y="80" text-anchor="middle" font-size="12">2022</text>
  <text x="350" y="80" text-anchor="middle" font-size="12">2023</text>
</svg>
```

### 2. Simple Flowchart

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="250" viewBox="0 0 300 250">
  <!-- Start -->
  <rect x="100" y="10" width="100" height="40" fill="green" stroke="black" stroke-width="2"/>
  <text x="150" y="35" text-anchor="middle" fill="white" font-weight="bold">Start</text>
  
  <!-- Arrow -->
  <line x1="150" y1="50" x2="150" y2="70" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- Process -->
  <rect x="100" y="70" width="100" height="40" fill="blue" stroke="black" stroke-width="2"/>
  <text x="150" y="95" text-anchor="middle" fill="white" font-weight="bold">Process</text>
  
  <!-- Arrow -->
  <line x1="150" y1="110" x2="150" y2="130" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- End -->
  <rect x="100" y="130" width="100" height="40" fill="red" stroke="black" stroke-width="2"/>
  <text x="150" y="155" text-anchor="middle" fill="white" font-weight="bold">End</text>
</svg>
```

### 3. Simple Bar Chart

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200">
  <!-- Y-axis -->
  <line x1="40" y1="20" x2="40" y2="160" stroke="black" stroke-width="2"/>
  
  <!-- X-axis -->
  <line x1="40" y1="160" x2="280" y2="160" stroke="black" stroke-width="2"/>
  
  <!-- Bars -->
  <rect x="60" y="100" width="40" height="60" fill="steelblue"/>
  <rect x="120" y="80" width="40" height="80" fill="steelblue"/>
  <rect x="180" y="60" width="40" height="100" fill="steelblue"/>
  <rect x="240" y="40" width="40" height="120" fill="steelblue"/>
  
  <!-- Labels -->
  <text x="80" y="180" text-anchor="middle" font-size="12">Q1</text>
  <text x="140" y="180" text-anchor="middle" font-size="12">Q2</text>
  <text x="200" y="180" text-anchor="middle" font-size="12">Q3</text>
  <text x="260" y="180" text-anchor="middle" font-size="12">Q4</text>
</svg>
```

## Using Claude to Generate SVG

### Example Prompt

```
Generate an SVG infographic showing the architecture of a microservices system.
Include:
- Service boxes with rounded corners
- Connection arrows between services
- Different colors for different types of services
- Labels for each component
- Professional styling with good typography

Make it approximately 500x400 pixels with viewBox="0 0 500 400"
```

### Tips for Getting Good SVG Output

1. **Be Specific** — Describe layout, colors, and dimensions
2. **Request Structure** — Ask for groups, IDs, and clear organization
3. **Include Dimensions** — Specify viewBox size
4. **Reference Patterns** — "Use a clean, minimalist style" or "professional business look"
5. **Define Colors** — Be specific: "use blue #0066CC, gray #CCCCCC"
6. **Mention Elements** — Request specific shapes: "rounded rectangles", "curved arrows"

## Editing SVG Infographics

### Free Tools

#### **Inkscape** (Recommended - Professional)
- Download: https://inkscape.org
- Open-source, free
- Full vector editing capabilities
- Learning curve: Moderate
- Best for: Complex infographics, professional designs

#### **Figma** (Best for Collaboration)
- Web-based: https://figma.com
- Free tier available
- Collaborative editing
- Learning curve: Easy
- Best for: Team projects, sharing designs

#### **SVG Online Editor**
- Boxy SVG: https://boxy-svg.com
- SVG Edit: https://svgedit.netlify.app
- Simple, web-based
- Learning curve: Very easy
- Best for: Quick edits, learning

### Basic Editing Workflow

1. **Open** SVG file in Inkscape or web editor
2. **Select** elements to modify
3. **Change** properties (colors, size, position, text)
4. **Save** as SVG (maintains format)
5. **Export** as PNG/PDF if needed

## Exporting SVG

### Save as PNG/PDF

#### Using Inkscape
```bash
inkscape input.svg -o output.png
inkscape input.svg -o output.pdf
```

#### Using Online Converters
- CloudConvert: https://cloudconvert.com
- Online-Convert: https://online-convert.com
- AnyConv: https://anyconv.com

### Quality Settings

- **PNG** — Best for web, supports transparency
- **PDF** — Best for printing, maintains vector quality
- **JPG** — Smaller file size, no transparency

## Best Practices

### Organization
- ✅ Use meaningful IDs and group names
- ✅ Group related elements together
- ✅ Comment complex sections
- ✅ Define reusable elements in `<defs>`
- ❌ Avoid deeply nested groups

### Performance
- ✅ Keep path definitions clean
- ✅ Use shapes instead of paths when possible
- ✅ Minimize decimal precision
- ✅ Remove unnecessary whitespace
- ❌ Don't create extremely large coordinate values

### Design
- ✅ Use consistent color palette
- ✅ Maintain consistent stroke widths
- ✅ Use aligned text (avoid misalignment)
- ✅ Provide adequate spacing
- ✅ Test on different screen sizes
- ❌ Don't mix too many fonts
- ❌ Avoid overly bright colors

### Accessibility
- ✅ Add descriptive titles: `<title>My Diagram</title>`
- ✅ Add descriptions: `<desc>A system architecture diagram</desc>`
- ✅ Use semantic structure
- ✅ Ensure sufficient color contrast
- ❌ Don't rely on color alone to convey information

## Common Patterns

### Reusable Symbols

```xml
<defs>
  <!-- Define once, use multiple times -->
  <symbol id="arrow" viewBox="0 0 10 10">
    <polygon points="5,0 10,10 0,10" fill="black"/>
  </symbol>
</defs>

<!-- Use multiple times -->
<use href="#arrow" x="50" y="50" width="20" height="20"/>
<use href="#arrow" x="150" y="150" width="20" height="20"/>
```

### Gradient Fills

```xml
<defs>
  <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:blue;stop-opacity:1"/>
    <stop offset="100%" style="stop-color:lightblue;stop-opacity:1"/>
  </linearGradient>
</defs>

<rect width="200" height="200" fill="url(#gradient)"/>
```

## Troubleshooting

### SVG Not Displaying

**Problem**: SVG won't open in browser
**Solution**:
- Check file has `.svg` extension
- Verify it starts with `<svg` and ends with `</svg>`
- Check for XML syntax errors (mismatched quotes)
- Try opening in browser console for error messages

### Colors Not Showing

**Problem**: Elements appear invisible
**Solution**:
- Check `fill` attribute is set (default is black)
- Verify colors are valid (hex, rgb, or named)
- Check `opacity` isn't set to 0
- Ensure elements aren't behind white background

### File Size Too Large

**Problem**: SVG file is bigger than expected
**Solution**:
- Remove unnecessary decimal places in coordinates
- Use shorthand commands in paths
- Consolidate similar styling
- Remove comments and whitespace
- Use `<g>` groups for shared properties

## Resources

### Learning
- [MDN SVG Documentation](https://developer.mozilla.org/en-US/docs/Web/SVG)
- [SVG Specification](https://www.w3.org/TR/SVG2/)
- [A Practical Guide to SVG](https://www.w3schools.com/graphics/svg_intro.asp)

### Tools
- [Inkscape](https://inkscape.org) — Professional vector editor
- [Figma](https://figma.com) — Collaborative design
- [SVG Repo](https://www.svgrepo.com) — SVG icons and graphics

### Conversion
- [CloudConvert](https://cloudconvert.com) — Format conversion
- [SVGOMG](https://jakearchibald.github.io/svgomg/) — SVG optimization

## Quick Checklist

When creating SVG infographics:

- [ ] Define proper viewBox dimensions
- [ ] Use meaningful IDs and groups
- [ ] Choose appropriate colors
- [ ] Include text labels where needed
- [ ] Test in multiple browsers
- [ ] Validate SVG structure
- [ ] Document complex sections
- [ ] Optimize before deployment
- [ ] Test responsiveness
- [ ] Plan for accessibility

---

**Next Steps**: See [SVG_WORKFLOW.md](SVG_WORKFLOW.md) for end-to-end workflow guide, or [SVG_QUICK_START.md](../docs/SVG_QUICK_START.md) for quick onboarding.
