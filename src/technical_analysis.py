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
