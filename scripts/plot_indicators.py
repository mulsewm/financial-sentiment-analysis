import matplotlib.pyplot as plt

def plot_stock_with_indicators(data, ticker):
    """
    Plots stock price along with technical indicators.
    Args:
        data (DataFrame): Stock price data with indicators.
        ticker (str): Stock ticker symbol.
    """
    plt.figure(figsize=(12, 8))

    # Plot Close Price and Moving Averages
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.plot(data.index, data['SMA_10'], label='SMA 10', color='orange')
    plt.plot(data.index, data['SMA_50'], label='SMA 50', color='green')

    # Plot RSI
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--')  # Overbought
    plt.axhline(30, color='green', linestyle='--')  # Oversold
    plt.title(f'{ticker} - Relative Strength Index (RSI)')
    plt.legend()
    plt.show()

    # Plot MACD
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, data['MACD'], label='MACD', color='blue')
    plt.plot(data.index, data['MACD_signal'], label='MACD Signal', color='red')
    plt.title(f'{ticker} - MACD')
    plt.legend()
    plt.show()
