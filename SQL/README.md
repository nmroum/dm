When to choose a view, materialized view, or pre-computed table

View:
- Use when you need a reusable query, always fresh data, and minimal storage.
- Example: a view that joins `articles` to `article_topics` for analysts, or a
  view that exposes daily article counts by language.

Materialized view:
- Use when the query is expensive and read-heavy, and slightly stale data is OK.
- Example: a materialized view that aggregates top topics per day for a
  dashboard, refreshed hourly.

Pre-computed table:
- Use when you need full control of refresh logic, versioning, and downstream
  dependencies (often built by ETL/ELT), or when multiple systems depend on the
  result.
- Example: a daily fact table of article metrics (counts, rolling averages,
  zero-filled dates) updated by a nightly job, or an NLP-enriched article table
  stored for auditability and repeatable ML features.

To summarize: views stay live, materialized views trade freshness for speed, and
pre-computed tables give you full control.