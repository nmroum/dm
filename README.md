# Src Mini Pipeline

This project implements a small ingestion and enrichment pipeline that:

- reads articles from a CSV file (pandas)
- detects topics via keyword matching
- writes outputs to Parquet

## Quick start

```bash
python pipeline.py
```

Outputs are written to `output/` by default.

## Run tests

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_readers.py
```

See [`explanations.md`](explanations.md) for assumptions and trade-offs.

