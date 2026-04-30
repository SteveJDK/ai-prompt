---
title: "Seedance 2.0 Video-to-Video & Motion Transfer (2026)"
date: 2026-04-29
draft: false
type: prompts
categories:
  - video-generation
tags: [seedance-2-0, bytedance, video-generation, motion-transfer, ai-video]
description: "Advanced prompts for Seedance 2.0 motion transfer, video editing, and style transformation. Includes before/after comparisons and JSON-style configurations."
model_compatibility:
  - "Seedance 2.0"
  - "Seedance 1.5"
quality_score: 95
difficulty: "Advanced"
version: "2.0.0"
featured: true
model: "Seedance-2.0"
variations:
  - name: "Motion Transfer"
    prompt_text: "Transfer the walking motion from the reference video to the target character. Preserve original lighting, background, and character clothing. Maintain temporal consistency across frames."
  - name: "Style Transfer"
    prompt_text: "Transform this video to anime style. Keep original motion, camera movement, and timing. Apply cel-shading, clean lineart, and vibrant colors consistent with Studio Ghibli aesthetic."
before_prompt: "Make this video look like anime style"
after_prompt: "Apply anime cel-shading style transformation to entire video. Preserve original motion vectors, camera pan speed, and timing. Use 24fps consistent frame style. Color palette: vibrant greens, warm sunset tones, clean lineart edges. No flickering or temporal artifacts."
craft_checklist:
  - "Canvas and frame rate before subject"
  - "Motion preservation constraints explicitly stated"
  - "Style anchors specific and bounded"
  - "Temporal consistency directives included"
prompt_text: |
  /* SEEDANCE-2.0 MOTION TRANSFER
     VERSION: 2.0.0 */

  **Source Video:** [REFERENCE_MOTION_CLIP]
  **Target:** [DESTINATION_CHARACTER/SCENE]
  **Operation:** [motion_transfer | style_transfer | video_edit]

  Motion Constraints:
  - Preserve original [speed/acceleration/trajectory]
  - Maintain temporal consistency at [FPS]fps
  - Keep original [lighting/camera/background] unchanged
  
  Style Directives (if style transfer):
  - Target style: [SPECIFIC_STYLE, e.g., "Studio Ghibli cel-shading"]
  - Color palette: [PRIMARY_COLORS]
  - Line art: [clean/sketch/watercolor]
  - Frame consistency: "no flickering, smooth transitions"

  Output Requirements:
  - Duration: [SECONDS]
  - Resolution: [WIDTH]x[HEIGHT]
  - Format: mp4, 24fps
  - Quality: "temporal smoothness, no artifacts"
tips:
  - "Seedance 2.0 requires explicit motion preservation constraints"
  - "Always specify frame rate and duration for consistent output"
  - "Style transfer works best when source and target have similar motion complexity"
  - "Use JSON-style config for complex multi-element video edits"
---
