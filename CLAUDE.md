# CLAUDE.md — Project Rules & Guidelines

---

## 🎨 Brand Assets & Identity

**CRITICAL**: Always check the `assets/brand/` folder before designing any infographic or visual. Your brand identity for all infographics is TNK Project.

### Brand Asset Requirements
- **Logo**: Use TNK eye symbol (64px+ minimum size)
- **Colors**: Only use TNK palette — never use default/generic colors
  - Primary: Cyan Eléctrico `#00CCFF`
  - Secondary: Verde Neón `#00FFB3`
  - Tertiary: Violeta `#B77FFF`
  - Base: Dark Navy `#0f1419` or `#1a1f2e`
- **Typography**: Space Grotesque (headlines), Inter (body), JetBrains Mono (code)
- **Full Guide**: [assets/brand/BRAND_GUIDE.md](assets/brand/BRAND_GUIDE.md)

### Anti-Generic Guardrails
**Colors**: Never use default Tailwind palette (indigo, blue, etc.). Pick TNK brand colors or derive from them.

**Shadows**: Never use flat `shadow-md`. Always layer with color tinting:
```css
box-shadow: 0 0 20px rgba(0, 204, 255, 0.2), 0 8px 24px rgba(0, 0, 0, 0.2);
```

**Typography**: Never use the same font for headings and body.
- Headings: Space Grotesque with `-0.04em` tracking
- Body: Inter with `1.7` line-height
- Code: JetBrains Mono

**Gradients**: Layer multiple radial gradients. Add subtle SVG noise filter (0.03–0.08 opacity) for depth.

**Animations**: Only animate `transform` and `opacity`. Never use `transition-all`. Use spring easing: `cubic-bezier(0.34, 1.56, 0.64, 1)`

**Interactive States**: Every clickable element must have:
- Hover (scale + glow)
- Focus-visible (cyan border outline)
- Active (scale down + enhanced shadow)
- Disabled (50% opacity)

**Images**: Always add gradient overlay `linear-gradient(180deg, rgba(15, 20, 25, 0.4), rgba(0, 0, 0, 0.6))` + color treatment layer with `mix-blend-multiply`.

**Spacing**: Use intentional tokens, not random steps:
- xs: 4px | sm: 8px | md: 12px | lg: 16px | xl: 24px | 2xl: 32px | 3xl: 48px | 4xl: 64px

**Depth**: Surfaces must layer properly:
- Base: #0f1419 (background)
- Surface: #252d3d (cards)
- Elevated: With cyan/violeta glow
- Floating: Maximum elevation (modals, tooltips)

---

## Key Capabilities

This project supports creating professional infographics using **two approaches**:

### 🎨 SVG Infographics (Recommended - Free & Professional)
- **No API costs, no dependencies, no setup required**
- Creates scalable vector graphics that work everywhere
- Use Claude to generate SVG code, save with `scripts/svg_generator.py`
- Perfect for: flowcharts, timelines, diagrams, organizational charts, architectures

### 📸 Image Generation (Optional - API-based)
- Uses OpenRouter API (costs apply)
- For photos, illustrations, artwork
- For technical diagrams, use SVG instead

## Always Do First

When the user needs any kind of infographic or visual:
1. **Ask if they want professional vector graphics or photos/illustrations**
2. **Default to SVG** — it's free, scalable, and professional
3. **Only use image generation** if they specifically request photos, artwork, or illustrations


---

## Creating SVG Infographics (5 Minutes)

**Perfect for**: Flowcharts, timelines, diagrams, organization charts, process flows, architectures

### Step-by-Step

1. **Describe your infographic** (plain English is fine):
   ```
   "Create a flowchart showing user registration process with 4 steps.
    Use professional blue and green colors.
    Make it 500x400 pixels."
   ```

2. **I'll generate SVG code** - you copy it

3. **Save using helper script** - no setup needed:
   ```bash
   python scripts/svg_generator.py my_diagram.svg
   # Paste the SVG code I provided
   ```

4. **Open in browser** - done!
   ```bash
   open my_diagram.svg
   ```

### Common Infographic Types

**Flowchart**
```
"Create an SVG flowchart with:
- Start/End nodes (circles)
- Process boxes (rectangles)
- Decision diamond
- Connecting arrows
- Labels for each step"
```

**Timeline**
```
"Create a 5-milestone timeline showing project progress.
Alternate points above and below the timeline line.
Use blue primary color and include dates and descriptions."
```

**Organization Chart**
```
"Create an org chart with CEO at top,
3 directors below, 2 managers under each director.
Use boxes connected by lines. Professional style."
```

**System Architecture**
```
"Create a microservices architecture diagram showing:
- Client layer, API Gateway, 4 microservices, database
- Arrows showing data flow
- Labels for each component"
```

### Documentation & Examples

- **Quick Start** (5 min): [docs/SVG_QUICK_START.md](docs/SVG_QUICK_START.md)
- **Full Workflow** (detailed): [docs/SVG_WORKFLOW.md](docs/SVG_WORKFLOW.md)
- **Technical Reference**: [references/SVG_INFOGRAPHICS.md](references/SVG_INFOGRAPHICS.md)
- **Working Examples**: `/examples/*.svg` (project-structure, workflow, timeline)
- **Templates**: `/assets/svg-templates/` (infographic, flowchart, timeline)

### Key Advantages

✅ **Zero Cost** - No API keys or subscriptions
✅ **No Dependencies** - Uses only Python stdlib
✅ **Professional Quality** - Scalable vectors, infinite zoom
✅ **Easy Editing** - Edit in free tools (Inkscape, Figma) or text editor
✅ **Portable** - Works in any browser, any device
✅ **Version Control** - Text-based, git-friendly

---

# Image Generation (Optional - API-based)
python scripts/generate_image.py "Add sunglasses to the person" --input portrait.png --model "black-forest-labs/flux.2-pro"
```

### Edit with custom output
```bash
python scripts/generate_image.py "Remove the text from the image" --input screenshot.png --output cleaned.png
```

### Multiple images
Run the script multiple times with different prompts or output paths:
```bash
python scripts/generate_image.py "Image 1 description" --output image1.png
python scripts/generate_image.py "Image 2 description" --output image2.png
```

## Script Parameters

- `prompt` (required): Text description of the image to generate, or editing instructions
- `--input` or `-i`: Input image path for editing (enables edit mode)
- `--model` or `-m`: OpenRouter model ID (default: google/gemini-3-pro-image-preview)
- `--output` or `-o`: Output file path (default: generated_image.png)
- `--api-key`: OpenRouter API key (overrides .env file)

## Example Use Cases

### For Scientific Documents
```bash
# Generate a conceptual illustration for a paper
python scripts/generate_image.py "Microscopic view of cancer cells being attacked by immunotherapy agents, scientific illustration style" --output figures/immunotherapy_concept.png

# Create a visual for a presentation
python scripts/generate_image.py "DNA double helix structure with highlighted mutation site, modern scientific visualization" --output slides/dna_mutation.png
```

### For Presentations and Posters
```bash
# Title slide background
python scripts/generate_image.py "Abstract blue and white background with subtle molecular patterns, professional presentation style" --output slides/background.png

# Poster hero image
python scripts/generate_image.py "Laboratory setting with modern equipment, photorealistic, well-lit" --output poster/hero.png
```

### For General Visual Content
```bash
# Website or documentation images
python scripts/generate_image.py "Professional team collaboration around a digital whiteboard, modern office" --output docs/team_collaboration.png

# Marketing materials
python scripts/generate_image.py "Futuristic AI brain concept with glowing neural networks" --output marketing/ai_concept.png
```

## Error Handling

The script provides clear error messages for:
- Missing API key (with setup instructions)
- API errors (with status codes)
- Unexpected response formats
- Missing dependencies (requests library)

If the script fails, read the error message and address the issue before retrying.

## Critical Prompt Requirements

**IMPORTANT: No Meta Instructions in Output**

When generating prompts for the AI image generation models, ensure the generated image does NOT contain any visible text showing:
- The prompt or instructions that were given to generate it
- System instructions or AI-related metadata
- Any "meta" text describing how the image was created
- Watermarks or labels indicating AI generation
- Layout descriptions (e.g., "left panel", "right panel", "center panel")
- Font specifications or typography instructions
- Color scheme descriptions or palette information

The image should only contain the requested visual content. Always include this instruction in your prompts: "Do not include any text showing the prompt, instructions, layout descriptions, font/color specifications, or metadata in the generated image."

## Notes

- Images are returned as base64-encoded data URLs and automatically saved as PNG files
- The script supports both `images` and `content` response formats from different OpenRouter models
- Generation time varies by model (typically 5-30 seconds)
- For image editing, the input image is encoded as base64 and sent to the model
- Supported input image formats: PNG, JPEG, GIF, WebP
- Check OpenRouter pricing for cost information: https://openrouter.ai/models

## Image Editing Tips

- Be specific about what changes you want (e.g., "change the sky to sunset colors" vs "edit the sky")
- Reference specific elements in the image when possible
- For best results, use clear and detailed editing instructions
- Both Gemini 3 Pro and FLUX.2 Pro support image editing through OpenRouter

## Integration with Other Skills

- **scientific-schematics**: Use for technical diagrams, flowcharts, circuits, pathways
- **generate-image**: Use for photos, illustrations, artwork, visual concepts
- **scientific-slides**: Combine with generate-image for visually rich presentations
- **latex-posters**: Use generate-image for poster visuals and hero images
