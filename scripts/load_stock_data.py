import yfinance as yf
import talib
import pandas as pd

def load_stock_data(ticker, start_date, end_date):
    """
    Fetches stock price data from Yahoo Finance.
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        start_date (str): Start date for data in 'YYYY-MM-DD' format.
        end_date (str): End date for data in 'YYYY-MM-DD' format.
    Returns:
        DataFrame: Stock price data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    print("Data loaded successfully:")
    print(data.head())
    return data

def save_data_to_csv(data, filename):
    data.to_csv(filename, index=True)
    print(f"Data saved to {filename}")
