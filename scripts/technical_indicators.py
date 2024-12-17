import talib

def add_technical_indicators(data):
    """
    Adds Moving Averages, RSI, and MACD to stock price data.
    Args:
        data (DataFrame): Stock price data with 'Close' prices.
    Returns:
        DataFrame: Data with additional columns for indicators.
    """
    # Moving Averages
    data['SMA_10'] = talib.SMA(data['Close'], timeperiod=10)  # 10-day Simple Moving Average
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)  # 50-day Simple Moving Average

    # Relative Strength Index (RSI)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

    # Moving Average Convergence Divergence (MACD)
    data['MACD'], data['MACD_signal'], _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    print("Technical indicators calculated:")
    print(data[['SMA_10', 'SMA_50', 'RSI', 'MACD']].head())
    return data
