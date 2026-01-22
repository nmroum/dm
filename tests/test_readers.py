import json

import pandas as pd

from src.readers import read_source


def test_read_articles_csv(tmp_path):
    df = pd.DataFrame(
        {
            "article_id": ["a1"],
            "source": ["source"],
            "language": ["en"],
            "published_at": ["2024-01-01T00:00:00Z"],
            "content": ["Hello world"],
        }
    )
    path = tmp_path / "articles.csv"
    df.to_csv(path, index=False)

    result = read_source(str(path))

    assert len(result) == 1
    assert set(result.columns) == set(df.columns)


def test_read_topics_json(tmp_path):
    payload = [{"topic_id": "ai", "keywords": ["AI", "gpt"]}]
    path = tmp_path / "topics.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    topics = read_source(str(path))

    assert len(topics) == 1
    assert topics[0]["topic_id"] == "ai"
