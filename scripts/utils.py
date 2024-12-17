import pandas as pd

def read_csv_file(file_path):
    """
    Reads a CSV file into a Pandas DataFrame.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        dict: Dictionary with keys 'data' and 'info'.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return {"data": df, "info": df.info()}
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")
