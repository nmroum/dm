import pandas as pd


def build_article_topics(articles: pd.DataFrame, topics: list[dict]) -> pd.DataFrame:
    print(f"Building article topics for {len(articles)} articles and {len(topics)} topics")
    if not topics:
        return pd.DataFrame(columns=["article_id", "topic_id"])

    matches: list[dict] = []
    for _, row in articles.iterrows():
        content_text = str(row.get("content") or "").lower()
        for topic in topics:
            if any(
                str(keyword).strip().lower() in content_text
                for keyword in topic.get("keywords", [])
            ):
                matches.append(
                    {"article_id": row.get("article_id"), "topic_id": topic.get("topic_id")}
                )

    if not matches:
        return pd.DataFrame(columns=["article_id", "topic_id"])

    combined = pd.DataFrame(matches).drop_duplicates()
    return combined.sort_values(["article_id", "topic_id"]).reset_index(drop=True)
