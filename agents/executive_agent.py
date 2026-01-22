class ExecutiveAgent:
    def __init__(self):
        self.role = "Executive (CEO)"

    def make_decision(self, ticker, sentiment_score, technical_score, sentiment_summary, technical_summary):
        """
        Aggregates insights and makes a trade decision.
        """
        print(f"[{self.role}] Aggregating reports for {ticker}...")
        
        # Weighted decision: Technicals might be more reliable for short term, News for volatility.
        # Let's say 60% Technical, 40% News for this simple model
        final_score = (technical_score * 0.6) + (sentiment_score * 0.4)
        
        print(f"[{self.role}] Weighted Score: {final_score:.2f} (Tech: {technical_score}, News: {sentiment_score})")

        decision = "HOLD"
        reasoning = ""

        if final_score > 0.4:
            decision = "STRONG BUY / GO LONG"
            reasoning = "Strong bullish momentum confirmed by technicals and sentiment."
        elif final_score > 0.15:
            decision = "BUY / ACCUMULATE"
            reasoning = "Positive trend, good for accumulation."
        elif final_score < -0.4:
            decision = "STRONG SELL / SHORT"
            reasoning = "Bearish breakdown. Look for shorting opportunities."
        elif final_score < -0.15:
            decision = "SELL / REDUCE"
            reasoning = "Weakness observed. Reduce exposure."
        else:
            decision = "HOLD / NO TRADE"
            reasoning = "Market is choppy or directionless."

        final_report = f"""
=========================================
FINAL DECISION FOR {ticker}: {decision}
=========================================
Reasoning: {reasoning}
-----------------------------------------
Technical Analysis: {technical_summary}
News Analysis: {sentiment_summary}
=========================================
"""
        return final_report
