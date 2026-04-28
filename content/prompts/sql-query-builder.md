---
title: "SQL Query Builder"
date: 2026-04-18T18:00:00
draft: false
type: prompts
categories:
  - data-analysis
tags: [sql, queries, database]
description: "Generate complex SQL queries with explanations and optimization tips."
model: "All Models"
difficulty: "Beginner"
prompt_text: |
  You are a SQL expert. Write optimized queries for:

  **Database:** [PostgreSQL/MySQL/SQL Server/SQLite]
  **Schema:**
  [DESCRIBE TABLES WITH COLUMNS AND RELATIONSHIPS]

  **Questions:**
  [LIST WHAT YOU NEED TO QUERY]

  For each query provide:
  1. **The SQL Query** - Formatted and commented
  2. **Explanation** - What each part does
  3. **Performance Tips** - Indexes needed, optimization suggestions
  4. **Edge Cases** - What could go wrong and how to handle it

  Use modern SQL features (CTEs, window functions) where appropriate.
tips:
  - Provide your table schemas
  - Specify your SQL dialect
---
