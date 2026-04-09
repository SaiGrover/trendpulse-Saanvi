import pandas as pd

def perform_eda():
    df = pd.read_csv("data/cleaned_data.csv")

    print("\n📌 DATA OVERVIEW")
    print(df.head())

    print("\n📌 DATA INFO")
    print(df.info())

    print("\n📌 NULL VALUES")
    print(df.isnull().sum())

    print("\n📌 TOP 10 NEWS SOURCES")
    print(df['source'].value_counts().head(10))

    print("\n📌 ARTICLES PER DAY")
    print(df['date'].value_counts().sort_index())

    print("\n📌 PEAK PUBLISHING HOURS")
    print(df['hour'].value_counts().sort_index())

    print("\n📌 TITLE LENGTH STATS")
    print(df['title_length'].describe())

    print("\n📌 CONTENT LENGTH STATS")
    print(df['content_length'].describe())

    print("\n📌 ARTICLES PER SOURCE (MEAN LENGTHS)")
    grouped = df.groupby('source').agg({
        'title_length': 'mean',
        'content_length': 'mean'
    }).sort_values(by='content_length', ascending=False)

    print(grouped.head(10))

if __name__ == "__main__":
    perform_eda()
