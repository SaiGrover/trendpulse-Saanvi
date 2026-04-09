import pandas as pd
import matplotlib.pyplot as plt

def visualize():
    df = pd.read_csv("data/cleaned_data.csv")

    # Top sources
    plt.figure()
    df['source'].value_counts().head(10).plot(kind='bar')
    plt.title("Top News Sources")
    plt.xlabel("Source")
    plt.ylabel("Article Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/top_sources.png")

    # Articles per hour
    plt.figure()
    df['hour'].value_counts().sort_index().plot(kind='line', marker='o')
    plt.title("Publishing Trend by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.savefig("data/hourly_trend.png")

    # Title length distribution
    plt.figure()
    df['title_length'].plot(kind='hist', bins=20)
    plt.title("Title Length Distribution")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("data/title_length_dist.png")

    print("Visualizations saved in data/ folder")

if __name__ == "__main__":
    visualize()
