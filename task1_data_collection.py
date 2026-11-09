import os
import sys

import pandas as pd
import requests

API_KEY = os.getenv("NEWSAPI_KEY")
URL = "https://newsapi.org/v2/top-headlines"

def fetch_data():
    if not API_KEY:
        sys.exit("NEWSAPI_KEY is not set. Export it before running this script.")

    response = requests.get(
        URL,
        params={"country": "in", "pageSize": 100},
        headers={"X-Api-Key": API_KEY},
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()

    articles = data.get("articles", [])

    records = []
    for article in articles:
        records.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "author": article.get("author"),
            "published_at": article.get("publishedAt"),
            "description": article.get("description"),
            "content": article.get("content")
        })

    df = pd.DataFrame(records)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_data.csv", index=False)

    print(" Data fetched and saved to data/raw_data.csv")

if __name__ == "__main__":
    fetch_data()
