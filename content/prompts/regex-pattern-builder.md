---
title: "Regex Pattern Builder"
date: 2026-05-02T20:00:00
draft: false
type: prompts
categories:
  - coding
tags: [regex, pattern-matching, text-processing]
description: "Build and explain complex regular expressions for text matching and extraction."
model: "All Models"
difficulty: "Intermediate"
prompt_text: |
  You are a regex expert. Build a regular expression for:

  **What to Match:** [DESCRIBE THE PATTERN YOU NEED]
  **Example Inputs:**
  - Should match: [EXAMPLES]
  - Should NOT match: [EXAMPLES]

  Provide:
  1. **The Regex Pattern** - Complete, tested pattern
  2. **Explanation** - What each part does, component by component
  3. **Test Cases** - 10 test strings showing match/no-match results
  4. **Language-Specific Notes** - Any differences for Python, JavaScript, etc.
  5. **Performance** - Efficiency considerations and potential backtracking issues
  6. **Simpler Alternative** - If there is a non-regex solution that is cleaner

  Make the pattern as readable as possible with comments and named groups.
tips:
  - Describe what you want to match
  - Provide example input strings
---
