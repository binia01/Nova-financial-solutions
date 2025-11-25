import pandas as pd
from textblob import TextBlob
import swifter

def add_sentiment_score(news_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates and adds a sentiment polarity score for each news headline.

    Args:
        news_df (pd.DataFrame): DataFrame containing news data with a 'headline' column.

    Returns:
        pd.DataFrame: The DataFrame with an added 'sentiment' column.
    """
    print("Calculating sentiment scores for news headlines...")
    # Ensure headlines are strings before analysis
    headlines = news_df['headline'].fillna('').astype(str)
    # Use swifter to speed up the apply operation
    news_df['sentiment'] = headlines.swifter.apply(
        lambda text: TextBlob(text).sentiment.polarity
    )
    return news_df

def prepare_daily_sentiment(news_df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares and aggregates news sentiment data for merging with stock data.

    This function performs two key steps:
    1. Normalizes the 'date' column to remove the time component, aligning it by day.
    2. Groups by 'stock' (ticker) and 'Date', calculating the mean daily sentiment.

    Args:
        news_df (pd.DataFrame): DataFrame with news data, including 'date', 'stock',
                                and a calculated 'sentiment' column.

    Returns:
        pd.DataFrame: A DataFrame indexed by ('Date', 'Ticker') with the mean daily sentiment.
    """
    print("Aggregating daily sentiment scores...")
    df = news_df.copy()
    # Normalize the date to just the date part (removes time)
    df['Date'] = pd.to_datetime(df['date']).dt.date
    df['Date'] = pd.to_datetime(df['Date']) # Convert back to datetime objects for merging
    
    # Group by stock and date, then calculate the average sentiment for that day
    daily_sentiment = df.groupby(['stock', 'Date'])['sentiment'].mean()
    daily_sentiment.rename_axis(['Ticker', 'Date'], inplace=True)
    
    return daily_sentiment.to_frame() # Convert Series to DataFrame

def merge_sentiment_with_stock_data(stock_df: pd.DataFrame, sentiment_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the daily stock data with the aggregated daily sentiment data.

    Args:
        stock_df (pd.DataFrame): DataFrame with stock OHLCV data, indexed by 'Date'.
        sentiment_df (pd.DataFrame): DataFrame with mean daily sentiment, indexed by ('Date', 'Ticker').

    Returns:
        pd.DataFrame: A combined DataFrame with stock and sentiment data.
    """
    print("Merging sentiment data with stock data...")
    
    # Ensure the stock DataFrame has Ticker as a column for merging
    if 'Ticker' not in stock_df.columns:
        stock_df = stock_df.reset_index()

    # The sentiment data has a MultiIndex ('Date', 'Ticker'). Resetting it prepares for merge.
    sentiment_df = sentiment_df.reset_index()

    # Merge on both Date and Ticker
    combined_df = pd.merge(stock_df, sentiment_df, on=['Date', 'Ticker'], how='left')

    # Forward-fill sentiment scores to apply a day's sentiment to subsequent non-news days
    combined_df['sentiment'] = combined_df.groupby('Ticker')['sentiment'].ffill()

    # Drop any initial rows that have no sentiment data to forward-fill from
    combined_df.dropna(subset=['sentiment'], inplace=True)
    
    return combined_df