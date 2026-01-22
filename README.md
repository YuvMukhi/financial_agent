# Financial Multi-Agent System (Indian Market Edition)

A modular AI system that combines News Analysis (NLP) and Technical Analysis to make trading decisions for the Indian Stock Market (NSE).

## 📂 Project Structure

- **`main.py`**: The entry point. Run this to analyze a stock.
- **`agents/`**: Contains the logic for individual agents.
  - `news_agent.py`: Fetches news and performs sentiment analysis using TextBlob.
  - `technical_agent.py`: Fetches live prices and calculates SMA/RSI.
  - `executive_agent.py`: Aggregates data and makes the final BUY/SELL decision.
- **`requirements.txt`**: List of Python dependencies.

## 🚀 How to Run

1.  **Install Expectations**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Analysis**:
    ```bash
    python main.py <TICKER>
    ```
    *Example:*
    ```bash
    python main.py RELIANCE
    python main.py TATASTEEL
    python main.py HDFCBANK
    ```
    *(The system automatically appends `.NS` for NSE tickers)*

## 🧪 Testing
- **`demo_scenarios.py`**: Run this to see how the Executive Agent handles various hardcoded scenarios (Bullish, Bearish, Mixed).

## 📊 Logic
1.  **News Agent**: Scans recent headlines for sentiment (-1 to +1).
2.  **Technical Agent**: Checks for Golden Cross (SMA50 > SMA200) and RSI levels (Overbought/Oversold).
3.  **Executive Agent**: Weighs Technicals (60%) and News (40%) to issue a "STRONG BUY", "ACCUMULATE", "HOLD", or "SELL" signal.
