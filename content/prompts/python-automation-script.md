---
title: "Python Automation Script"
date: 2026-04-20T22:00:00
draft: false
type: prompts
categories:
  - automation
tags: [python, automation, scripting]
description: "Generate Python scripts to automate repetitive tasks and workflows."
model: "All Models"
difficulty: "Intermediate"
prompt_text: |
  You are a Python automation expert. Write a script to automate:

  **Task Description:** [DESCRIBE WHAT NEEDS TO BE AUTOMATED]
  **Input:** [WHAT DATA/FILES IT STARTS WITH]
  **Output:** [WHAT RESULT IS EXPECTED]
  **Frequency:** [ONCE/DAILY/WEEKLY/CONTINUOUS]

  Provide:
  1. **Complete Script** - Production-ready with error handling
  2. **Requirements** - pip install commands for dependencies
  3. **Setup Instructions** - How to configure and run
  4. **Scheduling** - Cron or systemd timer configuration
  5. **Logging** - Built-in logging with levels and rotation
  6. **Edge Cases** - How the script handles failures and missing data

  Follow best practices: type hints, docstrings, try/except blocks, and configuration via environment variables.
tips:
  - Describe the manual process step by step
  - Specify any dependencies
---
