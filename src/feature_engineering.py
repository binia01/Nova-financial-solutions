import pandas as pd
from textblob import TextBlob
import swifter


def add_sentiment_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates and adds a sentiment polarity score for each headline using TextBlob.

    Args:
        df (pd.DataFrame): The input DataFrame with a 'headline' column.

    Returns:
        pd.DataFrame: The DataFrame with an added 'sentiment' column.
    """
    print("Calculating sentiment scores...")
    # Ensure headlines are strings before applying TextBlob
    headlines = df['headline'].fillna('').astype(str)
    df['sentiment'] = headlines.swifter.apply(lambda text: TextBlob(text).sentiment.polarity)
    return df

def add_headline_length(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates and adds the character length of each headline.

    Args:
        df (pd.DataFrame): The input DataFrame with a 'headline' column.

    Returns:
        pd.DataFrame: The DataFrame with an added 'headline_length' column.
    """
    df['headline_length'] = df['headline'].fillna('').apply(len)
    return df

def add_day_of_week(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts and adds the day of the week from the 'date' column.

    Args:
        df (pd.DataFrame): The input DataFrame with a datetime 'date' column.

    Returns:
        pd.DataFrame: The DataFrame with an added 'day_of_week' column.
    """
    df['day_of_week'] = df['date'].dt.day_name()
    return df