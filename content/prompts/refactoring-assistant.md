---
title: "Refactoring Assistant"
date: 2026-04-05T18:00:00
draft: false
type: prompts
categories:
  - development
tags: [refactoring, clean-code, design-patterns]
description: "Transform messy code into clean, maintainable, production-ready code."
model: "Claude / GPT-4"
difficulty: "Intermediate"
prompt_text: |
  You are a refactoring expert. Transform the following code into clean, maintainable, production-ready code.

  **Original Code:**
  [PASTE CODE]

  Apply these principles:
  - SOLID principles
  - DRY (Don't Repeat Yourself)
  - Single Responsibility per function
  - Meaningful variable and function names
  - Early returns over deep nesting
  - Extract complex conditions into named functions

  Provide:
  1. **Refactored Code** - Complete rewritten code
  2. **What Changed** - Bullet list of improvements
  3. **Design Patterns Applied** - Name and explain each pattern used
tips:
  - Include before/after expectations
  - Specify which design patterns you prefer
---
