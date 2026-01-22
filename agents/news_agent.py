import yfinance as yf
from textblob import TextBlob

class NewsAgent:
    def __init__(self):
        self.role = "News Analyst"

    def get_market_sentiment(self, ticker_symbol):
        """
        Fetches news for the ticker and calculates an average sentiment score (-1 to 1).
        """
        print(f"[{self.role}] Fetching news for {ticker_symbol}...")
        try:
            ticker = yf.Ticker(ticker_symbol)
            news = ticker.news
            
            if not news:
                print(f"[{self.role}] No news found for {ticker_symbol}.")
                return 0.0, "No recent news found."

            sentiments = []
            headlines = []
            
            # yfinance news is a list of dicts. Key 'title' contains the headline.
            for item in news:
                if 'title' in item:
                    headline = item['title']
                    analysis = TextBlob(headline)
                    score = analysis.sentiment.polarity
                    sentiments.append(score)
                    headlines.append(headline)

            if not sentiments:
                return 0.0, "No scorable headlines found."

            avg_sentiment = sum(sentiments) / len(sentiments)
            
            summary = f"Analyzed {len(sentiments)} headlines. Average Polarity: {avg_sentiment:.2f}"
            print(f"[{self.role}] {summary}")
            
            # Return score and a few top headlines for context if needed
            return avg_sentiment, headlines[:3]

        except Exception as e:
            print(f"[{self.role}] Error fetching news: {e}")
            return 0.0, "Error during analysis."
