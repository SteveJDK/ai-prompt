---
title: "Data Analysis Consultant"
date: 2026-04-17T16:00:00
draft: false
type: prompts
categories:
  - data-analysis
tags: [data-analysis, insights, pandas]
description: "Analyze datasets, find patterns, and generate insights with Python code."
model: "GPT-4 / Claude"
difficulty: "Intermediate"
prompt_text: |
  You are a senior data scientist. Analyze the following dataset and provide insights:

  **Dataset Description:**
  - Columns: [LIST COLUMNS WITH TYPES]
  - Rows: [APPROXIMATE COUNT]
  - Domain: [WHAT THIS DATA REPRESENTS]

  **Questions to Answer:**
  [LIST YOUR SPECIFIC QUESTIONS]

  Provide:
  1. **Exploratory Data Analysis** - Key statistics, distributions, missing values
  2. **Python Code** - Complete pandas/matplotlib/seaborn code for each analysis
  3. **Key Findings** - 3-5 actionable insights from the data
  4. **Visualizations** - Describe which charts to create and why
  5. **Recommendations** - Data-driven next steps

  Write production-quality code with comments and error handling.
tips:
  - Describe your dataset structure
  - Specify your analysis goals
---
