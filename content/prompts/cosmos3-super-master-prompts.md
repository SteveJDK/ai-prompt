---
title: "Cosmos3-Super Master Prompts (June 2026)"
date: 2026-06-12
draft: false
type: prompts
categories:
  - video-generation
  - multimodal
tags: [cosmos-3, nvidia, physical-ai, video-generation, world-model, 2026]
description: "Optimized prompts for NVIDIA Cosmos3-Super — a 64B physical-AI omnimodel that couples action trajectories with video+audio generation. World-model architecture for physics-aware content creation."
model_compatibility:
  - "Cosmos3-Super"
  - "NVIDIA Cosmos 3"
quality_score: 93
difficulty: "Advanced"
version: "1.0.0"
featured: true
model: "Cosmos3-Super"
parameters:
  architecture: "64B omnimodel (32B reasoner + 32B generator)"
  output: "Video + Audio + Action Trajectories"
  license: "OpenMDW 1.1"
variations:
  - name: "Physics-Aware Scene"
    prompt_text: |
      /* COSMOS3-SUPER CONFIG: Physical World Simulation
         ARCHITECTURE: 32B Reasoner → 32B Generator */

      SCENE: [SCENE_DESCRIPTION]
      PHYSICS:
        - Gravity: [EARTH | MOON | ZERO-G | CUSTOM 9.8 m/s²]
        - Materials: [GLASS (refractive), STEEL (reflective), CLOTH (deformable), WATER (fluid)]
        - Lighting: [SUN (directional), STUDIO (three-point), NEON (volumetric)]
        - Camera: [STATIC | DOLLY_LEFT | ORBIT | HANDHELD] at [DISTANCE]
      ACTION:
        - Object "[OBJECT_NAME]": [FALL | SLIDE | BOUNCE | SHATTER | DEFORM]
        - Duration: [N] seconds at 24fps
        - Initial state: [POSITION], [VELOCITY], [ROTATION]
      AUDIO:
        - Type: [PHYSICS_BASED | AMBIENT | MUSIC | DIALOGUE]
        - Spatial: [STEREO | SURROUND_5.1 | BINAURAL]
      RENDER: photorealistic, global illumination, motion blur at 0.5 shutter
  - name: "Action-Conditioned Generation"
    prompt_text: |
      /* COSMOS3-SUPER: Action-to-Video
         STRENGTH: Couples actions with generated visuals */

      TRAJECTORY: [ACTION_SEQUENCE]
        t=0.0: [INITIAL_STATE]
        t=1.0: [ACTION_1] → [EXPECTED_OUTCOME_1]
        t=2.0: [ACTION_2] → [EXPECTED_OUTCOME_2]
        t=3.0: [ACTION_3] → [EXPECTED_OUTCOME_3]
      
      ENVIRONMENT: [INDOOR | OUTDOOR | ABSTRACT | PHYSICS_SIM]
      AGENT: [ROBOT_ARM | HUMANOID | VEHICLE | DRONE | CUSTOM]
      CONSTRAINTS:
        - Collision detection: ON
        - Material physics: [REALISTIC | SIMPLIFIED]
        - Temporal consistency: HIGH
      OUTPUT: 24fps video with synchronized audio track
  - name: "Cinematic World-Building"
    prompt_text: |
      /* COSMOS3-SUPER: Cinematic World Model */

      WORLD: "[WORLD_NAME]" — [BRIEF_DESCRIPTION]
      ATMOSPHERE: [TIME_OF_DAY], [WEATHER], [SEASON]
      
      CAMERA PATH:
        Start: wide establishing shot, [DURATION]s
        → Push in to medium shot of [SUBJECT], [DURATION]s
        → Track right following [MOVING_ELEMENT], [DURATION]s
        → Pull back to wide, [DURATION]s
      
      AUDIO DESIGN:
        - Ambience: [WIND | RAIN | CROWD | SILENCE | CUSTOM]
        - Foley: [FOOTSTEPS | MECHANICAL | NATURE | CUSTOM]
        - Music: [ORCHESTRAL | ELECTRONIC | AMBIENT | NONE]
      
      PHYSICS NOTES: [WIND_STRENGTH], [PARTICLE_EFFECTS], [CLOTH_SIMULATION]
      RENDER STYLE: [PHOTOREAL | STYLIZED | CINEMATIC | ANIME]
craft_checklist:
  - "Define physics parameters explicitly — Cosmos3-Super is a world model, not just a video generator"
  - "Action trajectories use keyframe-style syntax with timestamps"
  - "Camera behavior described as path with timing per shot"
  - "Audio generation coupled with visual action for synchronized output"
  - "Material properties affect physics simulation quality"
prompt_text: |
  /* COSMOS3-SUPER MASTER PROMPT
     VERSION: 1.0.0
     CAPABILITIES: Physical-AI Video Gen, Action-Conditioned, Audio Sync
     ARCHITECTURE: 64B Omnimodel (32B Reasoner + 32B Generator) */

  **Scene:** [SCENE_TYPE] — [DURATION]s at [FPS]fps
  **World Physics:**
    - Gravity: [VALUE] m/s²
    - Atmosphere: [DENSITY], [WIND], [TEMPERATURE]
    - Materials present: [GLASS, METAL, CLOTH, WATER, ORGANIC]
  **Camera:**
    - Path: [SHOT_1 → SHOT_2 → SHOT_3] with [TRANSITION_TYPE]
    - Lens: [FOCAL_LENGTH]mm, [APERTURE]
  **Action Trajectory (keyframed):**
    t=[START]: [INITIAL_STATE]
    t=[MID]: [INTERMEDIATE_ACTION]
    t=[END]: [FINAL_STATE]
  **Audio:**
    - Type: [PHYSICS_BASED | DESIGNED | MUSIC]
    - Sync: [ON_ACTION | CONTINUOUS | REACTIVE]
  **Quality:** [PHOTOREAL | STYLIZED], temporal consistency HIGH

  Cosmos3-Super differentiators:
  - Physical simulation, not just pixel prediction
  - Couples action → video → audio in one unified generation
  - World-model architecture understands object permanence and physics
  - OpenMDW 1.1 license on Hugging Face
tips:
  - "Cosmos3-Super is a world model — use physics parameters (gravity, material, collision) not just visual descriptions"
  - "Action trajectories use keyframe syntax with precise timestamps for predictable output"
  - "Camera path is described as a sequence of shots with durations — not free-text"
  - "Audio is generated synchronously with video — specify audio events at the same timestamps as visual actions"
  - "For best temporal consistency, keep action sequences under 30 seconds"
---

## Cosmos3-Super Prompt Guide

**NVIDIA Cosmos3-Super** (released June 2026) is a **64 billion parameter physical-AI omnimodel** — a world-model architecture that combines a 32B reasoning module with a 32B generation module. Unlike traditional video generators that predict pixels, Cosmos3-Super **simulates physics** and couples action trajectories with synchronized video and audio output.

### Architecture

```
Action Trajectory → [32B Reasoner] → Physical State → [32B Generator] → Video + Audio
                                    ↑
                              World Knowledge
```

### Prompting Strategy

Cosmos3-Super requires a fundamentally different prompting approach than diffusion-based video models (Sora, Runway, Kling):

1. **Define physics first** — Gravity, material properties, atmospheric conditions
2. **Keyframe actions** — Use `t=TIMESTAMP` syntax for action trajectories
3. **Camera as path** — Describe camera movement as timed shot sequences
4. **Audio sync** — Specify audio events at the same timestamps as visual actions
5. **World knowledge** — The 32B reasoner understands real-world physics; describe outcomes, not pixel-level details

### Comparison: Cosmos3 vs Traditional Video Gen

| Aspect | Cosmos3-Super | Traditional (Sora/Runway) |
|--------|--------------|---------------------------|
| Approach | Physics simulation | Pixel prediction |
| Actions | Keyframe trajectories | Descriptive text |
| Audio | Synchronized generation | Separate generation |
| Consistency | Temporal by design | Requires guidance |
| License | OpenMDW 1.1 (Hugging Face) | Proprietary |
