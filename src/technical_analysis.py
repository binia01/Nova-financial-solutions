import pandas as pd
import talib

def _calculate_for_group(group: pd.DataFrame) -> pd.DataFrame:
    """
    Apply technical indicators to a single ticker's data.
    """
    group = group.copy()  # avoid SettingWithCopy issues

    # Simple Moving Averages
    group['SMA_20'] = talib.SMA(group['Close'], timeperiod=20)
    group['SMA_50'] = talib.SMA(group['Close'], timeperiod=50)

    # Relative Strength Index (RSI)
    group['RSI_14'] = talib.RSI(group['Close'], timeperiod=14)

    # MACD and components
    macd, macdsignal, macdhist = talib.MACD(
        group['Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    group['MACD'] = macd
    group['MACD_signal'] = macdsignal
    group['MACD_hist'] = macdhist
    
    return group


def add_technical_indicators(stock_df: pd.DataFrame) -> pd.DataFrame:
    """
    Add common technical indicators to OHLCV stock data grouped by ticker.
    """
    print("Calculating technical indicators...")

    # Define the lambda function
    def calculate_and_reattach_ticker(group):
        ticker = group['Ticker'].iloc[0]  # Get the ticker name for this group
        # Drop the ticker column for calculation
        indicators_df = _calculate_for_group(group.drop(columns=['Ticker']))
        # Re-attach the ticker column to the result
        indicators_df['Ticker'] = ticker
        return indicators_df
    
    df = (
        stock_df
        .groupby('Ticker', group_keys=False)
        .apply(calculate_and_reattach_ticker)
    )


    # Drop NaNs created from lookback windows
    df = df.dropna()

    print("Technical indicators added successfully.")
    return df

def add_daily_returns(stock_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the daily percentage change in the 'Close' price.

    Args:
        stock_df (pd.DataFrame): DataFrame with stock data, including a 'Ticker' column.

    Returns:
        pd.DataFrame: The DataFrame with an added 'daily_return' column.
    """
    print("Calculating daily stock returns...")
    # Calculate percentage change on the 'Close' price for each stock group
    stock_df['daily_return'] = stock_df.groupby('Ticker')['Close'].pct_change()
    
    # It's also useful to calculate the next day's return for predictive analysis
    stock_df['next_day_return'] = stock_df.groupby('Ticker')['daily_return'].shift(-1)
    
    # Drop rows with NaN values created by pct_change() and shift()
    stock_df.dropna(subset=['daily_return', 'next_day_return'], inplace=True)
    
    return stock_df