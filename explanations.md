# Explanations

## How to run
- Using Poetry:
  - `poetry install`
  - `poetry run python pipeline.py`
- Using system Python:
  - `pip install pandas pyarrow`
  - `python pipeline.py`
- Inputs are `articles.csv` and `topics.json` in the repo root; outputs land in `output/`.
- To change paths, update the arguments in `pipeline.py` or call `run_pipeline(...)`.

## Assumptions made
- `articles.csv` has at least `article_id` and `content` columns; other columns are preserved.
- `topics.json` is a list of objects with `topic_id` and `keywords` (list of strings).
- Missing or null `content` is treated as an empty string.
- Keyword matches are case-insensitive substring checks.
- An article can match multiple topics; duplicates are removed per `article_id`/`topic_id`.

## Trade-offs and design decisions
- Simple substring matching is easy to reason about but can create false positives.
- The implementation uses Python loops over rows and topics for clarity, not speed.
- The pipeline reads only CSV/JSON to keep the interface minimal.
- Outputs are Parquet for efficient storage.

## What I would improve with more time
- Use a more robust solution for the pipeline like Airflow
- Do some schema validation with clearer error messages.
- Add more source types to the reader
- Add structured logging and more tests for more cases.