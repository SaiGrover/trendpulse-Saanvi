import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw_data.csv")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df['author'].fillna("Unknown", inplace=True)
    df['description'].fillna("", inplace=True)
    df['content'].fillna("", inplace=True)

    # Convert to datetime
    df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')

    # Drop invalid dates
    df = df[df['published_at'].notna()]

    # Feature Engineering
    df['title_length'] = df['title'].apply(lambda x: len(str(x)))
    df['content_length'] = df['content'].apply(lambda x: len(str(x)))

    df['date'] = df['published_at'].dt.date
    df['hour'] = df['published_at'].dt.hour

    df.to_csv("data/cleaned_data.csv", index=False)

    print("Cleaned data saved to data/cleaned_data.csv")

if __name__ == "__main__":
    clean_data()
