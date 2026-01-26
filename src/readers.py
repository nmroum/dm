import json
from pathlib import Path

import pandas as pd


def read_articles(path: str):
    source_path = Path(path)
    print(f"Reading source from {source_path}")

    if not source_path.exists():
        raise Exception(f"Source file not found: {source_path}")

    suffix = source_path.suffix.lower()
    if suffix == ".csv":
        print("Reading CSV file")
        try:
            df = pd.read_csv(source_path) #validate article id, 
            if "article_id" not in df.columns:
                raise Exception("Article ID column not found in CSV file")
            if "content" not in df.columns:
                raise Exception("Content column not found in CSV file")
            return df
        except Exception as exc:
            raise Exception(f"Failed to read CSV file: {source_path}") from exc

def read_topics(path: str):
    source_path = Path(path)
    print(f"Reading source from {source_path}")

    if not source_path.exists():
        raise Exception(f"Source file not found: {source_path}")

    suffix = source_path.suffix.lower()

    if suffix == ".json":
        print("Reading JSON file")
        try:
            with open(source_path, "r", encoding="utf-8") as handle:
                topics = json.load(handle) #topic id and keyword
                # check json has keys topic id and keywords, validate all elements
                for element in topics:
                    if "topic_id" not in element.keys():
                        raise Exception("Topic ID key not found in JSON file")
                    if "keywords" not in element.keys():
                        raise Exception("Keywords key not found in JSON file")
                return topics
        except Exception as exc:
            raise Exception(f"Failed to read JSON file: {source_path}") from exc

    raise Exception(f"Unsupported file type. Use .csv or .json. Got {source_path}")
