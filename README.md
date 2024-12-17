# Financial News Sentiment and Stock Analysis

## Project Overview

This project analyzes a large corpus of financial news data to discover **correlations between news sentiment and stock market movements**. The analysis involves performing **sentiment analysis** on financial headlines, calculating **technical indicators** for stock prices, and establishing statistical relationships between sentiment and stock price changes.

The project is structured into clear, modular tasks to ensure scalability, reusability, and maintainability.

---

## **Objectives**

- Perform **Exploratory Data Analysis (EDA)** to understand financial news and stock price trends.
- Use **Natural Language Processing (NLP)** techniques to analyze sentiment in news headlines.
- Calculate **technical indicators** (Moving Averages, RSI, MACD) using TA-Lib.
- Establish **correlations** between sentiment scores and stock price movements.
- Visualize insights and trends to assist in investment strategies.

---

## **Project Structure**

The project follows a modular design to separate logic and ensure clean code. Below is the directory structure:

```
project-folder/
├── data/
│   ├── raw_data.csv              # Input data (financial news and stock prices)
│   ├── processed_data.csv        # Processed data after EDA
│   └── stock_data_with_indicators.csv  # Data with technical indicators
├── notebooks/
│   ├── data_processing.ipynb     # Jupyter notebook for EDA and analysis
│   
├── scripts/
│   ├── load_stock_data.py        # Functions to load stock price data
│   ├── technical_indicators.py   # Functions to calculate indicators (SMA, RSI, MACD)
│   ├── plot_indicators.py        # Functions for plotting stock data
│   └── utils.py                  # Utility functions for data loading and processing
├── tests/
│   └── test_scripts.py           # Unit tests for scripts
├── .github/
│   └── workflows/
│       └── unittests.yml         # GitHub Actions CI/CD pipeline
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

---

## **Setup Instructions**

To set up the project locally, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/financial-sentiment-analysis.git
cd financial-sentiment-analysis
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
Install all required Python packages from `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **4. Install TA-Lib (for Technical Indicators)**

- **macOS:**
  ```bash
  brew install ta-lib
  pip install TA-Lib
  ```

---

## **How to Run the Project**

### **1. Exploratory Data Analysis (EDA)**
Run the `data_processing.ipynb` notebook to:
- Analyze headline lengths, article frequency, and publisher trends.
- Perform sentiment analysis on financial news headlines.

### **2. Quantitative Analysis (Task 2)**
Run the `task_2_analysis.ipynb` notebook to:
- Load stock price data for specific tickers (e.g., AAPL).
- Calculate technical indicators (SMA, RSI, MACD) using TA-Lib.
- Visualize stock trends and patterns.

### **3. Correlation Analysis (Task 3)**
- Align sentiment scores and stock price movements by dates.
- Analyze correlations between sentiment and stock returns.
- Generate insights for predictive analysis.

---

## **Usage**

1. **Data Input**:
   - Place raw data in the `data/` folder (`raw_data.csv`).

2. **Scripts**:
   - Use modular scripts in the `scripts/` folder for data processing, analysis, and visualization.

3. **Testing**:
   - Run unit tests to verify the functionality of the scripts:
     ```bash
     pytest tests/test_scripts.py
     ```

4. **CI/CD**:
   - GitHub Actions automates the testing process (`.github/workflows/unittests.yml`).

---

## **Dependencies**

- Python 3.10+
- TA-Lib
- yfinance
- pandas
- numpy
- matplotlib
- seaborn
- textblob
- nltk
- pytest

All dependencies are listed in `requirements.txt`.

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your fork and create a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or collaboration:
- **Author**: Mulusew M. Tesfaye
- **Email**: your-email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/muliemes)
- **GitHub**: [Your GitHub Profile](https://github.com/mulsewm)

---

## **Acknowledgments**

- Tools and libraries: TA-Lib, yfinance, TextBlob, Pandas, Matplotlib.
- References and inspiration: [Investopedia](https://www.investopedia.com).
