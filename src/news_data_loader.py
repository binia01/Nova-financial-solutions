import pandas as pd

def load_news_data(file_path: str) -> pd.DataFrame:
    """
    Loads the analyst ratings dataset from a CSV file and performs initial cleaning.

    Args:
        file_path (str): The path to the raw CSV data file.

    Returns:
        pd.DataFrame: A DataFrame with the 'date' column converted to datetime objects
                      and invalid date rows removed.
    """
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)

    # Convert date column, coercing errors to NaT (Not a Time)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows where the date could not be parsed
    df.dropna(subset=['date'], inplace=True)
    
    print("Data loaded and initial date cleaning complete.")
    return df