import pandas as pd
import os

def load_and_prepare_data(file_path) -> pd.DataFrame:
    """
    Loads, extracts, and prepares stock data from a file.

    This function handles the entire data ingestion pipeline:
    1. Consolidates them into a single pandas DataFrame.
    2. Cleans the data by ensuring correct data types and handling missing values.
    2. Sorts the data by Ticker and Date, which is essential for time-series analysis.

    Args:
        file_path (str): file path for the files.

    Returns:
        pd.DataFrame: A cleaned, prepared, and indexed DataFrame ready for analysis.
    """
     

    # Load all CSVs into a single DataFrame
    all_data = []
    for filename in os.listdir(file_path):
        if filename.endswith('.csv'):
            # The ticker is usually in the filename
            ticker = filename.split('.')[0]
            df = pd.read_csv(os.path.join(file_path, filename))
            df['Ticker'] = ticker # Add a ticker column
            all_data.append(df)

    # Concatenate all data into one DataFrame
    stock_data = pd.concat(all_data, ignore_index=True)

    # Data cleaning
    # Convert 'Date' column to datetime objects
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # Ensure data types are correct (Open, High, Low, Close, Volume should be numeric)
    for col in ['Open', "High", 'Low', 'Close', 'Volume']:
        stock_data[col] = pd.to_numeric(stock_data[col], errors='coerce')

    # Sort the data (crucial for time-series calculations)
    stock_data.sort_values(by=['Ticker', 'Date'], inplace=True)

    # Set the Date as the index (useful for many financial analyses)
    stock_data.set_index('Date', inplace=True)

    # Drop ant rows with missing values
    stock_data.dropna(inplace=True)

    print("Data loaded and prepared successfully!")
    print(f"Loaded data for {stock_data['Ticker'].nunique()} stocks.")
    return stock_data
    