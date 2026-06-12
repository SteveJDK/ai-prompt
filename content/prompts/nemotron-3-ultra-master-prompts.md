---
title: "Nemotron 3 Ultra Master Prompts (June 2026)"
date: 2026-06-12
draft: false
type: prompts
categories:
  - llm
tags: [nemotron-3, nvidia, 550B, mamba-moe, prompt-engineering, 2026]
description: "Optimized prompts for NVIDIA Nemotron 3 Ultra — the first open-weight 550B hybrid Mamba-MoE model. 55B active parameters, 1M context window, 89.1 MMLU. Datacenter-scale agentic reasoning."
model_compatibility:
  - "Nemotron 3 Ultra"
  - "NVIDIA Nemotron 3"
quality_score: 95
difficulty: "Advanced"
version: "1.0.0"
featured: true
model: "Nemotron-3-Ultra"
parameters:
  architecture: "550B hybrid Mamba-MoE (55B active)"
  context: "1,000,000 tokens"
  mmlu: "89.1"
  license: "Open weights (NVFP4 variant available)"
variations:
  - name: "Million-Token Analysis"
    prompt_text: |
      /* NEMOTRON 3 ULTRA: 1M Context Deep Analysis
         ARCHITECTURE: 550B Mamba-MoE, 55B active, 1M context */

      You have access to [DOCUMENT_SET] spanning approximately [N] tokens.
      Analyze the entire corpus and produce:

      1. Executive Summary (500 words): Key themes, contradictions, and insights
      2. Cross-Reference Map: How documents relate to each other (graph description)
      3. Temporal Analysis: How themes evolved across the document timeline
      4. Entity Extraction: All named entities with relationships
      5. Critical Evaluation: Flagged inconsistencies, gaps, and areas needing verification
      6. Actionable Recommendations: 5-10 concrete next steps

      Leverage the full 1M context window — consider all documents simultaneously.
      Output: Structured markdown with tables and cross-references.
  - name: "Agentic Multi-Step Reasoning"
    prompt_text: |
      /* NEMOTRON 3 ULTRA: Agentic Reasoning Chain
         STRENGTH: 55B active Mamba-MoE for complex multi-step tasks */

      GOAL: [COMPLEX_GOAL_DESCRIPTION]

      Execute the following reasoning chain:
      1. DECOMPOSE: Break the goal into atomic subtasks
      2. PLAN: Order subtasks with dependencies
      3. RESEARCH: For each subtask, identify what information is needed
      4. REASON: Step through each subtask, showing your work
      5. SYNTHESIZE: Combine results into a coherent solution
      6. VERIFY: Check the solution against the original goal
      7. ITERATE: If gaps found, return to step 3 for affected subtasks

      Constraints:
      - Show intermediate reasoning explicitly
      - Flag assumptions and uncertainty levels
      - Use the Mamba architecture's strength for long-range dependencies
  - name: "Enterprise Document Processing"
    prompt_text: |
      /* NEMOTRON 3 ULTRA: Enterprise Batch Processing
         USE CASE: Legal/Financial/Technical document analysis */

      Process the following document batch:
      [DOCUMENT_1]: [TYPE] — [PURPOSE]
      [DOCUMENT_2]: [TYPE] — [PURPOSE]
      ...

      For each document:
      - Extract: Key clauses, obligations, dates, parties
      - Flag: Non-standard terms, potential risks, contradictions
      - Cross-reference: Conflicting clauses across documents

      Then produce:
      - Risk Matrix: High/Medium/Low with specific clause references
      - Compliance Checklist: Requirements vs. fulfillment status
      - Negotiation Points: 5-10 items ranked by priority

      Use full 1M context — all documents processed simultaneously for cross-document analysis.
craft_checklist:
  - "Declare context utilization strategy for 1M-token tasks"
  - "Use explicit reasoning chain structure for agentic workflows"
  - "Leverage Mamba-MoE hybrid for long-range dependency tasks"
  - "Specify output structure (markdown, JSON, tables) upfront"
  - "Break complex goals into explicit subtask chains"
prompt_text: |
  /* NEMOTRON 3 ULTRA MASTER PROMPT
     VERSION: 1.0.0
     CAPABILITIES: 550B Mamba-MoE, 55B Active, 1M Context, 89.1 MMLU
     ARCHITECTURE: Hybrid Mamba–Transformer Mixture-of-Experts */

  **Task:** [ANALYSIS | REASONING | GENERATION | AGENTIC]
  **Context Size:** [ESTIMATED_TOKENS] tokens (max 1,000,000)
  **Reasoning Depth:** [SHALLOW | MODERATE | DEEP | EXHAUSTIVE]

  **Instructions:**
    1. [PHASE_1 — Decomposition/Setup]
    2. [PHASE_2 — Core Processing]
    3. [PHASE_3 — Synthesis/Verification]
    4. [PHASE_4 — Output Formatting]

  **Output Format:** [MARKDOWN | JSON | TABLE | CODE]
  **Quality Requirements:**
    - [REQUIREMENT_1]
    - [REQUIREMENT_2]

  Nemotron 3 Ultra architecture notes:
  - Mamba backbone excels at ultra-long sequences (use full 1M context!)
  - MoE with 55B active parameters — substantial reasoning depth per token
  - Hybrid design: Mamba for long-range + Transformer experts for focused reasoning
  - NVFP4 variant: ~5× throughput on Blackwell hardware

  Strategy: Front-load complex tasks with explicit reasoning chains.
  The Mamba architecture processes linearly — structure your prompt to match.
tips:
  - "Nemotron 3 Ultra's 1M context window is the largest among open models — provide complete document sets, not summaries"
  - "Use explicit multi-step reasoning chains — the 55B active MoE excels at structured decomposition"
  - "Mamba backbone means the model processes sequentially — front-load the most important context"
  - "For enterprise document analysis, cross-reference clauses across all documents simultaneously"
  - "NVFP4 variant on Blackwell hardware delivers ~5× throughput for production deployment"
---

## Nemotron 3 Ultra Prompt Guide

**NVIDIA Nemotron 3 Ultra** (released June 2026) is the first open-weight **550 billion parameter hybrid Mamba–Mixture-of-Experts model** — a groundbreaking architecture combining Mamba's linear-time sequence processing with Transformer-based expert modules.

### Architecture

```
Input → [Mamba Backbone] → [MoE Router] → [Expert 1..N] → Output
         ↑ Linear time        ↑ 55B active        ↑ Sparse activation
         1M context OK        out of 550B total     ~10% active params
```

### Key Specifications

| Metric | Value |
|--------|-------|
| Total Parameters | 550B |
| Active Parameters | 55B (~10%) |
| Context Window | 1,000,000 tokens |
| MMLU Score | 89.1 |
| Architecture | Hybrid Mamba–Transformer MoE |
| License | Open weights (NVFP4 variant on Hugging Face) |

### Prompting Strategy

Nemotron 3 Ultra's unique Mamba-MoE architecture requires different prompting than pure Transformer models:

1. **Front-load critical context** — Mamba processes sequentially; early tokens have more influence
2. **Use explicit reasoning chains** — The 55B active MoE excels at structured multi-step decomposition
3. **Leverage the full 1M context** — Include entire document sets, codebases, or transcripts
4. **Structured output formats** — Request tables, JSON, or markdown with explicit section headers
5. **Agentic workflows** — Decompose complex goals into `t=1..N` reasoning steps

### Performance Characteristics
- **Strengths**: Ultra-long context tasks, multi-document analysis, agentic reasoning, structured decomposition
- **Trade-off**: Mamba backbone means sequential processing (not parallel like pure Transformers)
- **Deployment**: NVFP4 quantization variant achieves ~5× throughput on NVIDIA Blackwell hardware
