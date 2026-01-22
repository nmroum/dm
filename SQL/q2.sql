--For each language, compute a 7-day rolling average of articles published per day

WITH
-- Find overall min/max publish dates to build a full calendar.
dates_list AS (
  SELECT
    CAST(MIN(published_at) AS DATE) AS min_date,
    CAST(MAX(published_at) AS DATE) AS max_date
  FROM articles
),
-- Generate a contiguous list of dates between min and max.
calendar AS (
  SELECT
    generate_series(min_date, max_date, INTERVAL '1 day')::DATE AS published_date
  FROM dates_list
),
-- Identify all languages present in the dataset.
languages AS (
  SELECT DISTINCT language
  FROM articles
),
-- Count articles per language per day.
daily_counts AS (
  SELECT
    a.language,
    CAST(a.published_at AS DATE) AS published_date,
    COUNT(*) AS articles_per_day
  FROM articles AS a
  GROUP BY a.language, CAST(a.published_at AS DATE)
),
-- Create a complete language-by-date grid.
languages_calendar AS (
  SELECT
    l.language,
    d.published_date
  FROM languages AS l
  CROSS JOIN calendar AS d
),
-- Fill missing daily counts with zeros.
filled AS (
  SELECT
    c.language,
    c.published_date,
    COALESCE(dc.articles_per_day, 0) AS articles_per_day
  FROM languages_calendar AS c
  LEFT JOIN daily_counts AS dc
    ON dc.language = c.language
   AND dc.published_date = c.published_date
)
SELECT
  language,
  published_date,
  articles_per_day,
  AVG(articles_per_day) OVER (
    PARTITION BY language
    ORDER BY published_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7d_avg
FROM filled
ORDER BY language, published_date;
