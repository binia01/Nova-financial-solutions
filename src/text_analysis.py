import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords

def get_common_words(df: pd.DataFrame, top_n: int = 20) -> pd.DataFrame:
    """
    Finds the most common words in the headlines after removing stopwords.

    Args:
        df (pd.DataFrame): The DataFrame containing a 'headline' column.
        top_n (int): The number of top words to return.

    Returns:
        pd.DataFrame: A DataFrame with 'word' and 'count' of the most common words.
    """
    print(f"Finding top {top_n} common words...")
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))

    all_headlines = ' '.join(df['headline'].str.lower().fillna(''))
    words = all_headlines.split()
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

    word_counts = Counter(filtered_words)
    common_words = word_counts.most_common(top_n)

    return pd.DataFrame(common_words, columns=['word', 'count'])