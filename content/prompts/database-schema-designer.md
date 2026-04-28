---
title: "Database Schema Designer"
date: 2026-04-04T16:00:00
draft: false
type: prompts
categories:
  - development
tags: [database, schema, sql]
description: "Generate normalized database schemas with proper relationships and indexes."
model: "All Models"
difficulty: "Intermediate"
prompt_text: |
  You are a database architect. Design an optimized database schema for:

  **Application:** [DESCRIBE YOUR APPLICATION]
  **Database Type:** [PostgreSQL/MySQL/MongoDB/Other]

  Provide:
  1. **Entity-Relationship Diagram** (in text/mermaid format)
  2. **Table Definitions** with columns, types, constraints, and primary/foreign keys
  3. **Indexes** - Which columns need indexes and why
  4. **Normalization Level** - Which normal form and justification
  5. **Migration SQL** - Complete CREATE TABLE statements

  Optimize for read-heavy workloads unless specified otherwise.
tips:
  - Specify your database type (PostgreSQL, MySQL, MongoDB)
  - List your main entities
---
