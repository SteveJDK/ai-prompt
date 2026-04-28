---
title: "Debug This Error"
date: 2026-04-02T12:00:00
draft: false
type: prompts
categories:
  - development
tags: [debugging, error-fixing, troubleshooting]
description: "Diagnose and fix errors with root cause analysis and step-by-step solutions."
model: "All Models"
difficulty: "Beginner"
prompt_text: |
  You are an expert debugger. Analyze the following error and provide:

  **Error:**
  [PASTE ERROR MESSAGE AND STACK TRACE]

  **Context:**
  - Language/Framework: [SPECIFY]
  - Environment: [SPECIFY OS, VERSIONS]
  - What I was trying to do: [DESCRIBE]

  Please provide:
  1. **Root Cause** - What exactly went wrong and why
  2. **Immediate Fix** - The exact code change needed
  3. **Prevention** - How to avoid this error in the future
  4. **Related Issues** - Similar errors to watch out for

  Start with the fix first, then explain the cause. Be concise.
tips:
  - Include the full error message and stack trace
  - Mention your environment and versions
---
