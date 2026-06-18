---
title: "GPT-5.5 & GPT-5.5 Pro Master Prompts (June 2026)"
date: 2026-06-18
draft: false
type: prompts
categories:
  - trending
  - text-generation
tags: [gpt-5-5, openai, prompt-engineering, ai-model, 2026, reasoning, multimodality]
description: "Optimized prompts for OpenAI GPT-5.5 and GPT-5.5 Pro — native multimodality (text, vision, audio, speech), structured output, reasoning models, and function calling. Updated June 2026 for latest API capabilities."
model_compatibility:
  - "GPT-5.5"
  - "GPT-5.5 Pro"
  - "GPT-5.5 Instant"
  - "GPT-5.3"
quality_score: 96
difficulty: "Advanced"
version: "1.0.0"
featured: true
model: "GPT-5.5"
parameters:
  max_tokens: 128000
  temperature: 0.7
  reasoning_effort: "high"
variations:
  - name: "Structured Output Pipeline"
    prompt_text: |
      Generate a [DOMAIN] analysis following this exact JSON schema:
      {
        "summary": "string (max 200 chars)",
        "findings": [{"id": "string", "severity": "critical|high|medium|low", "detail": "string"}],
        "recommendations": [{"action": "string", "impact": "high|medium|low", "effort": "1-10"}],
        "confidence": 0.0-1.0
      }
      Use reasoning mode for complex analysis. Include confidence estimates for all claims.
  - name: "Multimodal Creative Brief"
    prompt_text: |
      You receive: [IMAGE_BRIEF], [AUDIO_BRIEF], [TEXT_SPEC]
      Synthesize all inputs into a unified creative direction document:
      1. Visual: extract key elements from image, describe palette/mood
      2. Audio: capture tone, pacing, emotional cues
      3. Text: identify constraints, requirements, style guide
      4. Fusion: combine into a coherent creative brief with 3 concept directions
      Use vision + audio natively — no external tools needed.
  - name: "Codex Agent Workflow"
    prompt_text: |
      Task: [COMPLEX_DEVOPS_TASK]
      
      Use the Agents SDK pattern:
      1. PLAN: break task into subtasks with dependency graph
      2. EXECUTE: for each subtask, run in sandbox and capture output
      3. VERIFY: validate each subtask output against spec
      4. INTEGRATE: compose verified outputs into final result
      
      Use function calling for tool execution. 
      Use structured output for inter-agent communication.
      On failure: retry with adjusted approach, max 3 attempts per subtask.
before_prompt: "Write a blog post about AI trends in 2026."
after_prompt: |
  As GPT-5.5, write a technical blog post about AI trends in Q2 2026:
  
  STRUCTURE:
  1. Executive summary (3 bullets, max 150 chars each)
  2. Market landscape (key players, model releases, pricing shifts)
  3. Technical deep-dive (2-3 breakthroughs with concrete metrics)
  4. Developer impact (API changes, tooling evolution, migration guides)
  5. Predictions (Q3-Q4 2026, with confidence levels)
  
  FORMAT: Markdown with mermaid diagrams for architecture flows.
  TONE: Technical but accessible. Assume senior engineer audience.
  SOURCES: Cite official announcements and benchmark data.
craft_checklist:
  - "Use structured output (JSON mode) for any data that will be parsed downstream"
  - "Enable reasoning mode (reasoning_effort=high) for multi-step analysis"
  - "Leverage native multimodality — pass images/audio directly, not as descriptions"
  - "Define function/tool schemas explicitly for agent workflows"
  - "Set response_format to json_schema for guaranteed valid outputs"
prompt_text: |
  /* GPT-5.5 MASTER PROMPT
     VERSION: 1.0.0
     CAPABILITIES: Native Multimodality, Structured Output, Reasoning, Function Calling, Agents SDK */

  **Model Configuration:**
  ┌─────────────────────────────────────────────┐
  │ model: gpt-5.5 | gpt-5.5-pro | gpt-5.5-instant│
  │ reasoning_effort: low | medium | high        │
  │ response_format: text | json_schema          │
  │ modalities: [text, vision, audio, speech]    │
  │ tools: [custom_functions, code_interpreter]  │
  └─────────────────────────────────────────────┘

  **Prompt Architecture:**
  ┌─ SYSTEM ─────────────────────────────────────┐
  │ Role: [EXPERTISE + CONSTRAINTS]              │
  │ Output: [FORMAT_SPEC]                        │
  │ Rules: [SAFETY + QUALITY_BOUNDARIES]          │
  └──────────────────────────────────────────────┘
  ┌─ CONTEXT ────────────────────────────────────┐
  │ Background: [DOMAIN_KNOWLEDGE]               │
  │ Input Data: [TEXT | IMAGE | AUDIO | SPEECH]  │
  │ Constraints: [HARD_REQUIREMENTS]             │
  └──────────────────────────────────────────────┘
  ┌─ INSTRUCTION ────────────────────────────────┐
  │ 1. [STEP_ONE] — purpose + expected output    │
  │ 2. [STEP_TWO] — dependencies on step 1       │
  │ 3. [STEP_N] — final integration              │
  └──────────────────────────────────────────────┘

  **Reasoning Mode Selection:**
  - LOW: Simple classification, formatting, translation
  - MEDIUM: Code review, content writing, data analysis
  - HIGH: Architecture design, multi-step research, debugging complex systems

  **Multimodal Input Pattern:**
  ```
  [IMAGE: screenshot of dashboard]
  Describe the metrics shown and identify anomalies.
  
  [AUDIO: customer_call.mp3]
  Extract action items and sentiment shifts.
  
  [TEXT: product spec]
  Given the above, generate a prioritized roadmap.
  ```

  **Function Calling Pattern:**
  Define tools with clear JSON schemas. GPT-5.5 will chain calls intelligently.
  For agent workflows, use the Agents SDK pattern: plan → execute → verify → integrate.

  **Output Quality Gates:**
  - Structured outputs: validate against schema before returning
  - Code: include error handling and edge cases
  - Research: cite sources, flag uncertainty
  - Creative: provide 3+ variations with trade-off notes
tips:
  - "Use reasoning_effort=high for any task requiring more than surface-level analysis"
  - "Native multimodality means images/audio go directly in the prompt — no preprocessing needed"
  - "Structured output with json_schema guarantees valid JSON — use for pipelines"
  - "GPT-5.5 Pro has deeper reasoning and lower hallucination for critical applications"
  - "Function calling chains are smarter in 5.5 — define tools once, let the model orchestrate"
  - "For Agents SDK: start with a simple agent, add tools incrementally, test sandbox behavior"
  - "GPT-5.5 on Amazon Bedrock (June 2026): use for enterprise deployments with AWS integration"
---

## GPT-5.5 & GPT-5.5 Pro — Complete Prompt Guide

OpenAI's GPT-5.5 series represents a major leap in native multimodality, structured reasoning, and agentic capabilities. Available on the OpenAI API and **Amazon Bedrock** (as of June 2026).

### Model Family

| Model | Best For | Key Feature |
|---|---|---|
| **GPT-5.5** | General purpose, coding, writing | Balanced performance/cost |
| **GPT-5.5 Pro** | Research, architecture, critical apps | Deeper reasoning, lower hallucination |
| **GPT-5.5 Instant** | High-throughput, chat | Fastest, most affordable |
| **GPT-5.5-Cyber** | Enterprise security | Locked-down, private deployment |

### What's New vs GPT-5

1. **Native multimodality** — images, audio, and speech are first-class inputs. No separate vision/audio models.
2. **Reasoning effort control** — dial reasoning depth per request (`low`/`medium`/`high`).
3. **Structured output** — `json_schema` response format guarantees valid JSON output.
4. **Agents SDK** — first-class agent orchestration with sandbox execution.
5. **Amazon Bedrock GA** — enterprise deployment with AWS integration.

### Prompting Best Practices

1. **Lead with output format.** GPT-5.5 respects structure more than any previous OpenAI model — use it.
2. **Reasoning for complex tasks.** Set `reasoning_effort=high` for multi-step problems. The model will "think" before answering.
3. **Multimodal by default.** Don't describe images — include them. GPT-5.5 processes them natively.
4. **Function calling is production-grade.** Define tools with JSON schemas and let the model chain them.
5. **Structured output for pipelines.** Use `response_format: json_schema` when the output feeds another system.
