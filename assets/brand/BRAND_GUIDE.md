# TNK Project — Brand Identity Guide

## 🎯 Brand Mission
Impulsar el análisis digital y el diseño estratégico combinando datos, tecnología y estética moderna.

## Brand Values
- **Innovación**: Vanguardia en analítica y diseño web
- **Precisión**: Atención al detalle en cada métrica y pixel
- **Claridad**: Comunicar lo completo de forma accesible
- **Elegancia**: Estética limpia, oscura y funcional

---

## 🎨 Color Palette

### Primary Color
- **Cian Eléctrico** — `#00CCFF`
- Energy, technology, forward-thinking
- Use for: Primary CTAs, highlights, key data points

### Secondary Color
- **Verde Neón** — `#00FFB3`
- Growth, positive change, success
- Use for: Secondary CTAs, accent borders, positive indicators

### Tertiary Color
- **Violeta** — `#B77FFF`
- Creativity, innovation, premium feel
- Use for: Accent elements, special features, depth layers

### Neutral Colors
- **Base (Dark Navy)** — `#0F1419` / `#1a1f2e`
- Primary background for all interfaces
- **Surface (Slightly Lighter)** — `#252d3d`
- Cards, containers, elevated surfaces
- **Text (Light)** — `#e0e0e0` / `#ffffff`
- Primary text on dark backgrounds
- **Text (Muted)** — `#9ca3af` / `#808080`
- Secondary text, helper text, labels

### Accent (Optional)
- **Rosa Neón** — `#FF5289`
- Use sparingly for errors, urgent states, or premium accents

---

## 🔤 Typography

### Headlines — **Space Grotesque**
- Family: Space Grotesque (geometric, modern, bold)
- Tracking: `-0.04em` (tight letter spacing for impact)
- Weight: **800** (Ultra Bold) for main titles
- Weight: **700** (Bold) for secondary headings
- Line Height: `1.1` (tight, confident)
- Usage: H1 (56px), H2 (40px), H3 (28px), H4 (22px)

**Characteristics**: Geometric, futuristic, technical
**When to use**: All headlines, section titles, CTAs

### Body — **Inter**
- Family: Inter (clean, highly legible, modern sans-serif)
- Weight: **400** (Regular) for body text
- Weight: **500** (Medium) for emphasis
- Weight: **600** (Semi-Bold) for strong emphasis
- Line Height: `1.7` (generous, readable)
- Size: `14px` to `16px` for optimal readability
- Letter Spacing: `0` (default, never tight for body)

**Characteristics**: Clean, accessible, professional
**When to use**: Body text, descriptions, supporting content, UI labels

### Code — **JetBrains Mono**
- Family: JetBrains Mono (monospace, technical, clear)
- Weight: **400** (Regular)
- Size: `12px` to `14px`
- Line Height: `1.6`

**Characteristics**: Monospace, technical, precise
**When to use**: Code snippets, technical values, command lines, IDs

---

## 🎭 Logo Usage

**Primary Logo**: TNK eye symbol with gold outline
- Minimum size: 64px width
- Always maintain clear space (minimum 1/4 logo width on all sides)
- Never distort, rotate, or modify the shape
- Versions:
  - **Light background**: Black TNK with gold outline
  - **Dark background**: White TNK with gold outline
  - **Monochrome**: Black or white only (when color unavailable)

---

## 🌈 Gradients & Effects

### Primary Gradient
- **Cian to Verde**: `linear-gradient(135deg, #00CCFF, #00FFB3)`
- Use for: Hero sections, major CTAs, primary backgrounds

### Secondary Gradient
- **Violeta to Cian**: `linear-gradient(135deg, #B77FFF, #00CCFF)`
- Use for: Accent sections, premium features, depth layers

### Dark Base Gradient
- **Navy to Darker Navy**: `linear-gradient(180deg, #1a1f2e, #0f1419)`
- Use for: Background transitions, depth effects

### Shadow System (Layered & Color-Tinted)
- **Soft Glow** (for interactive elements):
  ```css
  box-shadow: 0 0 20px rgba(0, 204, 255, 0.2);
  ```
- **Elevated** (for cards):
  ```css
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.2),
    0 8px 24px rgba(0, 204, 255, 0.1);
  ```
- **Deep Shadow** (for floating elements):
  ```css
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    0 0 20px rgba(0, 204, 255, 0.15);
  ```

### Texture & Depth
- Add subtle SVG noise filter for depth in gradients
- Opacity: `0.03–0.08` (very subtle, not obvious)
- Use `mix-blend-mode: multiply` for color treatment overlays
- Layer multiple radial gradients for complex backgrounds

---

## ✨ Visual Principles

### 1. Color Blocking
Never use generic color palettes. Always use TNK primary colors:
- Cyan (#00CCFF) for primary actions
- Verde (#00FFB3) for secondary/success states
- Violeta (#B77FFF) for tertiary/premium features

### 2. Shadows
- Never use flat `shadow-md`
- Always layer shadows with color tinting:
  - Base shadow (dark, low opacity)
  - Colored glow (cyan or violeta, even lower opacity)

### 3. Typography Pairing
- **Headlines**: Space Grotesque (geometric, bold, -0.04em tracking)
- **Body**: Inter (clean, 1.7 line-height)
- **Code**: JetBrains Mono
- Never use same font for headlines and body

### 4. Spacing Tokens
Use consistent, intentional spacing:
- **xs**: 4px
- **sm**: 8px
- **md**: 12px
- **lg**: 16px
- **xl**: 24px
- **2xl**: 32px
- **3xl**: 48px
- **4xl**: 64px

### 5. Depth Layering
Surfaces must have defined layering:
- **Base**: Dark Navy (#0f1419)
- **Surface**: Slightly lighter (#252d3d) — cards, containers
- **Elevated**: With cyan/violeta glow — floating elements, modals
- **Floating**: Maximum elevation — tooltips, dropdowns, popovers

### 6. Interactive States
Every clickable element must have:
- **Default**: Standard state
- **Hover**: Slight scale (1.02–1.05) + glow effect
- **Focus Visible**: Cyan border outline (2–3px)
- **Active**: Scale down (0.98) + enhanced shadow
- **Disabled**: 50% opacity + no interactivity

### 7. Images & Photo Treatment
When using images:
- Add gradient overlay: `linear-gradient(180deg, rgba(15, 20, 25, 0.4), rgba(0, 0, 0, 0.6))`
- Apply color treatment with `mix-blend-mode: multiply` + cyan/violeta tint
- Maintain contrast ratio ≥ 4.5:1 for text over images
- Never use images without treatment — always add depth layer

### 8. Animations
- Only animate: `transform` and `opacity`
- Never use: `transition-all`
- Easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` (spring-style)
- Duration: 200–300ms for micro-interactions, 400–600ms for larger movements
- Avoid: Rapid, jarring transitions

---

## 🎬 Component Styles

### Buttons
- **Primary**: Cyan background, black text, hover glow
- **Secondary**: Verde background, dark navy text
- **Tertiary**: Violeta outline, transparent background
- **Disabled**: 50% opacity, no hover effects

### Cards
- Background: Surface color (#252d3d)
- Border: 1px cyan/violeta (optional)
- Shadow: Layered with cyan tint
- Spacing: 24px padding (xl token)
- Radius: 8–12px (not fully rounded)

### Input Fields
- Background: Dark base (#1a1f2e)
- Border: 1px #404854 (default), cyan on focus
- Text: Light color (#e0e0e0)
- Placeholder: Muted text (#808080)
- Focus: Cyan glow, 2px outline

### Badges & Tags
- Background: Gradient (Cyan to Verde)
- Text: Dark navy (contrast)
- Padding: 6px 12px (md token)
- Radius: 20px (pill-shaped)
- Size: Small (12px text)

---

## 📐 Layout Grid

- **Desktop**: 12-column grid, 16px gutters
- **Tablet**: 8-column grid, 12px gutters
- **Mobile**: 4-column grid, 8px gutters
- **Base spacing unit**: 4px (all padding/margin multiples of 4)

---

## ✅ Quick Checklist for All Designs

- [ ] Using TNK color palette (not generic colors)
- [ ] Headlines in Space Grotesque with -0.04em tracking
- [ ] Body text in Inter with 1.7 line-height
- [ ] Layered, color-tinted shadows (never flat)
- [ ] Every interactive element has hover/focus/active states
- [ ] Consistent spacing tokens (4px base unit)
- [ ] Proper depth layering (base → surface → elevated → floating)
- [ ] Images have gradient overlay + color treatment
- [ ] Dark navy background (#0f1419 or #1a1f2e)
- [ ] Animations use transform + opacity only
- [ ] Text contrast ratio ≥ 4.5:1 (WCAG AA)
- [ ] Logo used correctly with clear space
