import matplotlib.pyplot as plt

def plot_stock_data(df, date_column, stock_value_column):
    """
    Plots stock data as a line chart.
    Args:
        df (DataFrame): The data to plot.
        date_column (str): The name of the date column.
        stock_value_column (str): The stock value to plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df[date_column], df[stock_value_column], marker='o', linestyle='-')
    plt.title('Stock Data Over Time')
    plt.xlabel('Date')
    plt.ylabel(stock_value_column)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
