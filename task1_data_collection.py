import requests
import pandas as pd
import os

API_KEY = "e58ebfae7934474882754ff8b4a51ed6"  # Replace with your NewsAPI key
URL = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey={API_KEY}"

def fetch_data():
    response = requests.get(URL)
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
