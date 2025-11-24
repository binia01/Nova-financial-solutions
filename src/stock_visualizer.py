import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_technical_analysis(df:pd.DataFrame, ticker: str):
    """
    Generates a 3-panel plot for a given stock showing price, RSI, and MACD.

    Args:
        df (pd.DataFrame): The DataFrame containing stock data and indicators.
        ticker (str): The ticker symbol of the stock to plot.
    """

    if ticker not in df['Ticker'].unique():
        print(f"Error: Ticker '{ticker}' not found in the DataFrame.")
        return
    
    ticker_df = df[df['Ticker'] == ticker].copy()

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15,12), sharex=True,
                                        gridspec_kw={'height_ratios': [3,1,1]})
    
    # Panel 1: Price and Moving Averages

    ax1.plot(ticker_df.index, ticker_df['Close'], label='Close Price', color='blue')
    ax1.plot(ticker_df.index, ticker_df['SMA_20'], label='20-Day SMA', color='orange', linestyle='--')
    ax1.plot(ticker_df.index, ticker_df['SMA_50'], label='50-Day SMA', color='red', linestyle='--')
    ax1.set_ylabel('Price (USD)')
    ax1.set_title(f'Technical Analysis for {ticker}')
    ax1.legend()
    ax1.grid(True)

    # Panel 2: RSI
    ax2.plot(ticker_df.index, ticker_df['RSI_14'], label='RSI (14)', color='purple')
    ax2.axhline(70, linestyle='--', color='red', alpha=0.5)
    ax2.axhline(30, linestyle='--', color='green', alpha=0.5)
    ax2.set_ylabel('RSI')
    ax2.legend()
    ax2.grid(True)

    # Panel 3: MACD
    ax3.bar(ticker_df.index, ticker_df['MACD_hist'], label='MACD Histogram', color='gray', alpha=0.7)
    ax3.plot(ticker_df.index, ticker_df['MACD'], label='MACD', color='green')
    ax3.plot(ticker_df.index, ticker_df['MACD_signal'], label='Signal Line', color='red', linestyle='--')
    ax3.set_ylabel('MACD')
    ax3.legend()
    ax3.grid(True)

    # Formatting and display
    plt.xlabel('Date')
    plt.tight_layout()
    plt.show()