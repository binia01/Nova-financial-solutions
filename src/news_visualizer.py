import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_headline_length_distribution(df: pd.DataFrame):
    """Plots the distribution of headline lengths."""
    plt.figure(figsize=(10, 4))
    sns.histplot(df['headline_length'], bins=50, kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.show()

def plot_sentiment_distribution(df: pd.DataFrame):
    """Plots the distribution of sentiment polarity."""
    plt.figure(figsize=(10, 4))
    sns.histplot(df['sentiment'], bins=50, kde=True)
    plt.title("Sentiment Polarity Distribution")
    plt.show()

def plot_top_publishers(df: pd.DataFrame, top_n: int = 10):
    """Plots the top N publishers by article count."""
    plt.figure(figsize=(12, 5))
    df['publisher'].value_counts().nlargest(top_n).plot(kind='bar')
    plt.title(f"Top {top_n} Publishers by Article Count")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_articles_over_time(df: pd.DataFrame):
    """Plots the number of articles published per day over time."""
    plt.figure(figsize=(14, 5))
    df.set_index('date')['headline'].resample('D').count().plot()
    plt.title("Articles Published Per Day")
    plt.ylabel("Number of Articles")
    plt.xlabel("Date")
    plt.tight_layout()
    plt.show()

def plot_articles_by_day_of_week(df: pd.DataFrame):
    """Plots a count of articles for each day of the week."""
    plt.figure(figsize=(10, 6))
    sns.countplot(x='day_of_week', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.title('Number of Articles per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_common_words(common_words_df: pd.DataFrame):
    """Plots a horizontal bar chart of the most common words."""
    plt.figure(figsize=(12, 8))
    sns.barplot(x='count', y='word', data=common_words_df)
    plt.title(f"Top {len(common_words_df)} Most Common Words in Headlines")
    plt.xlabel('Frequency')
    plt.ylabel('Word')
    plt.show()
