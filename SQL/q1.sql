--For each topic, return the top 3 sources by article count

WITH topic_source_counts AS (
  SELECT
    at.topic_id,
    a.source,
    COUNT(*) AS article_count
  FROM article_topics AS at
  JOIN articles AS a
    ON a.article_id = at.article_id
  GROUP BY at.topic_id, a.source
),
ranked AS (
  SELECT
    topic_id,
    source,
    article_count,
    ROW_NUMBER() OVER (
      PARTITION BY topic_id
      ORDER BY article_count DESC, source
    ) AS rn
  FROM topic_source_counts
)
SELECT
  topic_id,
  source,
  article_count
FROM ranked
WHERE rn <= 3
ORDER BY topic_id, article_count DESC, source;