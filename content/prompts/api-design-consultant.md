---
title: "API Design Consultant"
date: 2026-04-03T14:00:00
draft: false
type: prompts
categories:
  - development
tags: [api-design, rest, architecture]
description: "Design RESTful APIs with proper endpoints, versioning, and documentation."
model: "Claude / GPT-4"
difficulty: "Intermediate"
prompt_text: |
  You are a senior API architect. Design a RESTful API for the following domain:

  **Domain:** [DESCRIBE YOUR APPLICATION DOMAIN]

  Please provide:
  1. **Resource Endpoints** - All CRUD operations with HTTP methods, paths, and request/response schemas
  2. **Authentication** - Recommended auth strategy (JWT, OAuth2, API keys)
  3. **Error Handling** - Standardized error response format with HTTP status codes
  4. **Pagination and Filtering** - How to handle large datasets
  5. **Versioning Strategy** - URL path vs header vs query param
  6. **Rate Limiting** - Recommended approach and headers

  Output as a clean API specification table. Include OpenAPI/Swagger annotations where relevant.
tips:
  - Specify your domain/model clearly
  - Mention if you need GraphQL instead of REST
---
