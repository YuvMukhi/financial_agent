import yfinance as yf
import pandas as pd
import numpy as np

class TechnicalAgent:
    def __init__(self):
        self.role = "Technical Analyst"

    def calculate_rsi(self, data, window=14):
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def analyze_price_action(self, ticker_symbol):
        """
        Fetches historical data and calculates technical indicators (SMA, RSI).
        Returns a signal (-1 to 1) and a reason.
        """
        print(f"[{self.role}] Analyzing technicals for {ticker_symbol}...")
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Fetch 1 year of data to calculate 200 SMA
            hist = ticker.history(period="1y")
            
            if hist.empty or len(hist) < 200:
                print(f"[{self.role}] Insufficient data for technical analysis.")
                return 0, "Insufficient data"

            # Calculate Indicators
            hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
            hist['SMA_200'] = hist['Close'].rolling(window=200).mean()
            hist['RSI'] = self.calculate_rsi(hist)

            # Fetch Live Price
            try:
                current_price = ticker.fast_info['last_price']
                print(f"[{self.role}] Live Price: {current_price:.2f}")
            except:
                current_price = hist['Close'].iloc[-1]
                print(f"[{self.role}] Could not fetch live price, using last close: {current_price:.2f}")

            sma_50 = hist['SMA_50'].iloc[-1]
            sma_200 = hist['SMA_200'].iloc[-1]
            rsi = hist['RSI'].iloc[-1]
            
            signal_score = 0
            reasons = []

            # SMA Logic
            if sma_50 > sma_200:
                signal_score += 0.5
                reasons.append(f"Golden Cross (Bullish) | 50SMA: {sma_50:.2f}")
            elif sma_50 < sma_200:
                signal_score -= 0.5
                reasons.append(f"Death Cross (Bearish) | 50SMA: {sma_50:.2f}")

            # RSI Logic
            if rsi < 30:
                signal_score += 0.5
                reasons.append(f"RSI Oversold ({rsi:.2f})")
            elif rsi > 70:
                signal_score -= 0.5
                reasons.append(f"RSI Overbought ({rsi:.2f})")
            else:
                reasons.append(f"RSI Neutral ({rsi:.2f})")

            # Price vs SMA (Using Live Price)
            if current_price > sma_50:
                signal_score += 0.2
                reasons.append("Price > 50 SMA")
            elif current_price < sma_50:
                signal_score -= 0.2
                reasons.append("Price < 50 SMA")

            # Cap score
            signal_score = max(min(signal_score, 1.0), -1.0)
            
            report = f"Score: {signal_score:.2f} | Signals: {', '.join(reasons)}"
            print(f"[{self.role}] {report}")
            
            return signal_score, report

        except Exception as e:
            print(f"[{self.role}] Error analyzing technicals: {e}")
            return 0, f"Error: {e}"
