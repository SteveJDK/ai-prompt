---
title: "Gemma 4 Master Prompts (June 2026)"
date: 2026-06-12
draft: false
type: prompts
categories:
  - llm
  - multimodal
tags: [gemma-4, google, multimodal, any-to-any, prompt-engineering, 2026]
description: "Optimized prompts for Google Gemma 4 12B — the encoder-free any-to-any multimodal model. Handles text, image, audio, and video with 256K context. Apache 2.0 open weights. Laptop-class deployment."
model_compatibility:
  - "Gemma 4"
  - "Gemma 4 12B"
quality_score: 94
difficulty: "Intermediate"
version: "1.0.0"
featured: true
model: "Gemma-4"
parameters:
  context: "256K tokens"
  languages: "140+"
  architecture: "12B encoder-free any-to-any"
variations:
  - name: "Multimodal Analysis"
    prompt_text: |
      /* GEMMA-4 MULTIMODAL ANALYSIS
         CAPABILITY: Any-to-any (text/image/audio/video) */
      
      You are analyzing [CONTENT_TYPE]. Provide a structured breakdown:

      1. Visual Elements (if image/video): Describe layout, colors, subjects, text content
      2. Audio Elements (if audio): Transcribe speech, identify speakers, note tone/emotion
      3. Text Elements: Extract key information, summarize, identify entities
      4. Cross-Modal Insights: How do the different modalities interact or contradict?
      5. Actionable Summary: 3-5 bullet points of key takeaways

      Output format: Markdown with clear section headers. Be thorough but concise.
  - name: "Multilingual Translation"
    prompt_text: |
      /* GEMMA-4 140+ LANGUAGE TRANSLATION
         STRENGTH: Native multilingual support */

      Translate the following content from [SOURCE_LANG] to [TARGET_LANG].
      Preserve: formatting, tone, cultural nuances, technical terminology.
      If the content contains mixed modalities, process each separately:

      Text: "[TEXT_CONTENT]"
      Context notes: [ADDITIONAL_CONTEXT]

      Output: Clean translated text only. Add translator notes for culturally-specific terms.
  - name: "Agentic Coding Assistant"
    prompt_text: |
      /* GEMMA-4 CODING ASSISTANT
         STRENGTH: 256K context, code understanding */

      Role: Senior software engineer. Analyze the codebase context below and:
      1. Identify the architecture pattern being used
      2. Flag any potential issues (security, performance, maintainability)
      3. Suggest 3 improvements with code examples
      4. If a specific task is requested, implement it with clear comments

      Context window utilization: The full 256K is available — provide comprehensive code context.
      Output: Structured markdown with code blocks, file paths, and line references.
craft_checklist:
  - "Declare modality type at prompt start for routing"
  - "Use structured output format requests (markdown, JSON)"
  - "Leverage full 256K context by including comprehensive reference material"
  - "Specify output language explicitly for multilingual tasks"
  - "Break complex multimodal tasks into sequential analysis steps"
prompt_text: |
  /* GEMMA-4 MASTER PROMPT
     VERSION: 1.0.0
     CAPABILITIES: Any-to-Any Multimodal, 256K Context, 140+ Languages
     ARCHITECTURE: 12B Encoder-Free, Apache 2.0 */

  **Task Type:** [analysis | translation | generation | coding | creative]
  **Input Modality:** [text | image | audio | video | mixed]
  **Output Format:** [markdown | JSON | code | plain text]
  **Language:** [TARGET_LANGUAGE] (Gemma 4 supports 140+ natively)

  **Context (use the full 256K):**
    [DETAILED_CONTEXT — include reference docs, examples, specifications]

  **Instructions:**
    1. [STEP_1 — modality-specific analysis]
    2. [STEP_2 — processing]
    3. [STEP_3 — output formatting]

  **Constraints:**
    - [CONSTRAINT_1]
    - [CONSTRAINT_2]

  Key Gemma 4 capabilities:
  - Encoder-free design: no separate vision/audio encoders — unified processing
  - 256K context window: provide extensive reference material
  - 140+ languages: specify target language explicitly
  - Apache 2.0: fully open for commercial use
tips:
  - "Gemma 4's any-to-any design means you can mix image, audio, and text in a single prompt"
  - "Always specify output language — 140+ supported, but defaults to input language"
  - "256K context is generous — include reference docs and examples directly in the prompt"
  - "For coding tasks, provide full file context rather than snippets — the model excels at large-context understanding"
  - "Apache 2.0 license means no usage restrictions for commercial deployment"
---

## Gemma 4 Prompt Guide

**Gemma 4 12B** (released June 2026) is Google's **encoder-free any-to-any multimodal model** — a single unified architecture that processes text, images, audio, and video without separate modality-specific encoders. It ships with **Apache 2.0 open weights**, making it the most deployable multimodal open model available.

### Key Capabilities

| Feature | Specification |
|---------|--------------|
| Architecture | 12B encoder-free any-to-any |
| Context Window | 256,000 tokens |
| Languages | 140+ natively supported |
| Modalities | Text, image, audio, video |
| License | Apache 2.0 (fully open) |
| Deployment | Laptop-class (ONNX + MLX ready) |

### Prompting Strategy

1. **Declare modalities upfront** — Tell Gemma 4 what types of input you're providing
2. **Use the full context** — 256K tokens lets you include entire documents, codebases, or transcripts
3. **Specify output format** — Gemma 4 responds well to structured output format directives
4. **Explicit language selection** — For multilingual tasks, name the target language explicitly
5. **Sequential analysis for mixed content** — Break complex multi-modal tasks into ordered steps

### Deployment
Weights available via Hugging Face. QAT (Quantization-Aware Training) enables INT4/FP8 deployment on consumer hardware. ONNX and MLX ports available for Apple Silicon.
