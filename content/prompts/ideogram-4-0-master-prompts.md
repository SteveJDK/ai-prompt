---
title: "Ideogram 4.0 Master Prompts (June 2026)"
date: 2026-06-12
draft: false
type: prompts
categories:
  - image-generation
tags: [ideogram-4, open-weight, text-to-image, prompt-engineering, ai-art, 2026]
description: "Optimized prompts for Ideogram 4.0 — the #2 image generation model with first-ever open weights. JSON-structured prompts with bounding boxes, color palettes, and precision text layouts. Excels at posters, UI mockups, and text-rich designs."
model_compatibility:
  - "Ideogram 4.0"
  - "Ideogram 4"
quality_score: 96
difficulty: "Advanced"
version: "1.0.0"
featured: true
model: "Ideogram-4.0"
parameters:
  size: "2048x2048"
  quality: "high"
  architecture: "9.3B DiT flow-matching"
variations:
  - name: "JSON Bounding Box"
    prompt_text: "/* IDEOGRAM-4 CONFIG: Event Poster\n   ARCHITECTURE: 9.3B DiT Flow-Matching */\n{\n  \"canvas\": { \"ratio\": \"2:3\", \"resolution\": \"2K\" },\n  \"layout\": {\n    \"header\": { \"bbox\": [0.05, 0.02, 0.95, 0.15], \"text\": \"TECH SUMMIT 2026\", \"font\": \"sans-serif bold\", \"size\": \"large\" },\n    \"body\": { \"bbox\": [0.05, 0.20, 0.95, 0.60], \"content\": \"futuristic cityscape with data streams\" },\n    \"footer\": { \"bbox\": [0.05, 0.85, 0.95, 0.98], \"text\": \"June 20-22 | San Francisco\", \"font\": \"monospace\", \"size\": \"small\" }\n  },\n  \"palette\": [\"#0a0a2e\", \"#00d4ff\", \"#ff6b35\", \"#ffffff\"],\n  \"style\": \"neon-noir tech conference aesthetic\",\n  \"render_goals\": [\"crisp typography\", \"high contrast\", \"no text artifacts\"]\n}"
  - name: "UI Mockup"
    prompt_text: "/* IDEOGRAM-4 CONFIG: App UI Mockup\n   STRENGTH: Text-rich layouts, labelled diagrams */\n{\n  \"canvas\": { \"ratio\": \"9:19.5\", \"resolution\": \"2K\" },\n  \"layout\": {\n    \"status_bar\": { \"bbox\": [0, 0, 1, 0.04], \"elements\": [\"9:41\", \"wifi\", \"battery\"] },\n    \"header\": { \"bbox\": [0, 0.05, 1, 0.12], \"text\": \"Dashboard\", \"font\": \"system sans-serif bold\" },\n    \"card_1\": { \"bbox\": [0.05, 0.15, 0.95, 0.30], \"bg\": \"#ffffff\", \"shadow\": true, \"content\": \"Revenue: $12,450\\n↑ 12% vs last month\" },\n    \"card_2\": { \"bbox\": [0.05, 0.33, 0.95, 0.48], \"bg\": \"#f8f9fa\", \"content\": \"Active Users: 2,847\\n● Online: 342\" },\n    \"tab_bar\": { \"bbox\": [0, 0.93, 1, 1], \"items\": [\"Home\", \"Analytics\", \"Settings\", \"Profile\"] }\n  },\n  \"palette\": [\"#ffffff\", \"#f8f9fa\", \"#4f46e5\", \"#111827\"],\n  \"style\": \"clean iOS design system, rounded corners, subtle shadows\"\n}"
  - name: "Product with Labels"
    prompt_text: "/* IDEOGRAM-4 CONFIG: Labelled Product Diagram\n   STRENGTH: Text + visual precision */\n{\n  \"canvas\": { \"ratio\": \"16:9\", \"resolution\": \"2K\" },\n  \"subject\": { \"type\": \"mechanical keyboard exploded view\", \"angle\": \"45° isometric\" },\n  \"annotations\": [\n    { \"bbox\": [0.15, 0.20, 0.30, 0.25], \"label\": \"PBT Keycaps\", \"connector\": \"line\" },\n    { \"bbox\": [0.40, 0.35, 0.55, 0.40], \"label\": \"Cherry MX Switches\", \"connector\": \"line\" },\n    { \"bbox\": [0.35, 0.55, 0.60, 0.60], \"label\": \"Aluminum Plate\", \"connector\": \"line\" },\n    { \"bbox\": [0.50, 0.70, 0.70, 0.75], \"label\": \"Hot-Swap PCB\", \"connector\": \"line\" }\n  ],\n  \"palette\": [\"#e8e8e8\", \"#333333\", \"#00bcd4\"],\n  \"lighting\": \"diffuse studio lighting, soft shadows\",\n  \"render_goals\": [\"clean lines\", \"readable labels\", \"professional diagram\"]\n}"
before_prompt: "Make an image of a keyboard with labels."
after_prompt: "Isometric exploded view of a mechanical keyboard at 45°. PBT Keycaps (top layer, labelled). Cherry MX Switches (middle layer, labelled). Aluminum Plate (lower layer, labelled). Hot-Swap PCB (bottom layer, labelled). Diffuse studio lighting, soft shadows. Clean diagram aesthetic, high readability."
craft_checklist:
  - "JSON structured with bounding boxes for precise layout control"
  - "Color palette defined as hex array for brand consistency"
  - "Text regions enclosed in bbox coordinates with font specifications"
  - "Canvas ratio declared FIRST for stable composition"
  - "Render goals as explicit directives, not vague adjectives"
prompt_text: |
  /* IDEOGRAM-4.0 MASTER PROMPT
     VERSION: 1.0.0
     CAPABILITIES: Text-Rich Layouts, Bounding Box Control, Open Weights DiT
     STRENGTHS: Posters, UI Mockups, Labelled Diagrams, Typography */

  **Canvas:** [ASPECT_RATIO] at [RESOLUTION] (e.g., "2:3 at 2K", "16:9 at 2K")
  **Layout Type:** [poster | UI mockup | diagram | product shot | illustration]
  **Structured Regions (JSON style):**
    - Each region: { "bbox": [x1, y1, x2, y2], "content": "...", "font/style": "..." }
    - Bounding boxes powerful for text placement — Ideogram 4's core strength
  **Color Palette:** [PRIMARY], [SECONDARY], [ACCENT], [BACKGROUND]
    - Use hex codes (#RRGGBB) for brand consistency
  **Lighting:** [TYPE] [DIRECTION] [MOOD]
  **Material/Texture:** [SURFACE_DETAILS]
  **Quality Directives:** "no text artifacts, clean lines, professional grade"

  Key Ideogram 4.0 differentiators:
  - Bounding-box syntax for pixel-precise text placement
  - Native 2K resolution — always specify "2K" for best quality
  - Excels at combining text + visuals (posters, UI, diagrams)
  - Flow-matching DiT architecture — different prompt style than diffusion
tips:
  - "Ideogram 4.0's killer feature is bounding-box text placement — use bbox coordinates for posters and UI mockups"
  - "Always define hex color palette explicitly — Ideogram 4 respects brand color specifications"
  - "Canvas ratio FIRST prevents layout drift — prioritize over subject description"
  - "For text-heavy designs, each text block needs its own bbox region with font/size hints"
  - "Use '2K' resolution directive for maximum quality output"
---

## Ideogram 4.0 Optimization Guide

Ideogram 4.0 (June 2026) is a **9.3B parameter Diffusion Transformer (DiT)** trained from scratch with flow-matching — and it ships **open weights** for the first time. It ranks **#2 overall** on image generation leaderboards, behind only GPT Image 2.0, and is the **#1 open-weight model** on Design Arena and LMArena.

### Key Strengths
- **Text-Rich Layouts**: Posters, UI mockups, labelled diagrams — text renders clean without garbled characters
- **Bounding Box Control**: JSON-style `bbox` coordinates for pixel-precise element placement
- **Color Palette Adherence**: Explicit hex color arrays produce consistent brand outputs
- **2K Native Resolution**: Trained at 2048×2048 — always specify "2K" for optimal quality

### Prompt Structure
Ideogram 4.0 responds best to **JSON-structured prompts** with explicit spatial coordinates. Unlike diffusion models that benefit from verbose natural language, Ideogram's DiT architecture prefers structured parameterization:

1. **Canvas first** — Always declare aspect ratio and resolution before any content
2. **Bounding boxes** — Use `[x1, y1, x2, y2]` coordinates (0-1 normalized) for precise placement
3. **Hex palettes** — Define colors as `#RRGGBB` arrays for brand-accurate output
4. **Render goals** — Replace vague adjectives ("beautiful", "nice") with concrete directives

### License Note
Weights are available on Hugging Face under a non-commercial agreement. Apache 2.0 for code; commercial path available via Ideogram directly.
