import json
from pathlib import Path

import pandas as pd


def read_source(path: str):
    source_path = Path(path)
    print(f"Reading source from {source_path}")

    if not source_path.exists():
        raise Exception(f"Source file not found: {source_path}")

    suffix = source_path.suffix.lower()
    if suffix == ".csv":
        print("Reading CSV file")
        try:
            return pd.read_csv(source_path)
        except Exception as exc:
            raise Exception(f"Failed to read CSV file: {source_path}") from exc

    if suffix == ".json":
        print("Reading JSON file")
        try:
            with open(source_path, "r", encoding="utf-8") as handle:
                return json.load(handle)
        except Exception as exc:
            raise Exception(f"Failed to read JSON file: {source_path}") from exc

    raise Exception(f"Unsupported file type. Use .csv or .json. Got {source_path}")
