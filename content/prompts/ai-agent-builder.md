---
title: "AI Agent Builder"
date: 2026-04-22T00:00:00
draft: false
type: prompts
categories:
  - automation
tags: [ai-agents, workflow, autonomous]
description: "Design autonomous AI agents with tools, memory, and decision-making capabilities."
model: "GPT-4 / Claude"
difficulty: "Advanced"
prompt_text: |
  You are an AI agent architect. Design an autonomous agent for:

  **Goal:** [WHAT THE AGENT SHOULD ACCOMPLISH]
  **Environment:** [WHERE IT OPERATES - WEB/API/DATABASE/CLI]
  **Tools Available:** [LIST APIS, DATABASES, SERVICES]
  **Constraints:** [TIME LIMITS, RATE LIMITS, BUDGET, SAFETY RULES]

  Provide:
  1. **Agent Architecture** - Role, capabilities, and decision flow
  2. **System Prompt** - The complete system prompt for the LLM
  3. **Tool Definitions** - Each tool with description, parameters, and when to use
  4. **Memory Strategy** - What to remember between iterations (short-term vs long-term)
  5. **Guardrails** - Safety rules, rate limit handling, and error recovery
  6. **Evaluation** - How to measure if the agent is succeeding

  Include a state machine diagram in text format showing the agent decision flow.
tips:
  - Define the agent goal clearly
  - Specify which tools/APIs it needs
---
