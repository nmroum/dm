import pandas as pd

from src.enrichment import build_article_topics


def test_build_article_topics_matches_keywords():
    articles = pd.DataFrame(
        {
            "article_id": ["a1", "a2"],
            "source": ["source", "source"],
            "language": ["en", "en"],
            "published_at": ["2026-01-01T00:00:00Z", "2026-01-02T00:00:00Z"],
            "content": ["OpenAI releases a new GPT model.", "nothing relevant."],
        }
    )
    topics = [{"topic_id": "ai", "keywords": ["ai", "gpt"]}]

    article_topics = build_article_topics(articles, topics)

    assert article_topics.to_dict(orient="records") == [
        {"article_id": "a1", "topic_id": "ai"}
    ]
