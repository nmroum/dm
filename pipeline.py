from src.enrichment import build_article_topics
from src.readers import read_articles, read_topics


def run_pipeline(articles_path, topics_path, output_dir):
    articles = read_articles(articles_path)
    topics = read_topics(topics_path)
    article_topics = build_article_topics(articles, topics)

    output_dir = str(output_dir).rstrip("/")
    articles.to_parquet(f"{output_dir}/articles.parquet", index=False)
    article_topics.to_parquet(f"{output_dir}/article_topics.parquet", index=False)

    #articles.to_csv(f"{output_dir}/articles.csv", index=False)
    #article_topics.to_csv(f"{output_dir}/article_topics.csv", index=False)

    return articles, article_topics


if __name__ == "__main__":
    run_pipeline(
        articles_path="articles.csv",
        topics_path="topics.json",
        output_dir="output",
    )
