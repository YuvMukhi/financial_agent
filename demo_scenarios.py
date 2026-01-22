from agents.executive_agent import ExecutiveAgent
from textblob import TextBlob

def analyze_mock_news(headlines):
    """
    Helper to simulate what the NewsAgent does.
    """
    sentiments = []
    for h in headlines:
        analysis = TextBlob(h)
        sentiments.append(analysis.sentiment.polarity)
    
    avg_score = sum(sentiments) / len(sentiments) if sentiments else 0
    summary = f"Mock Analysis of {len(headlines)} headlines. Avg Score: {avg_score:.2f} | Headlines: {headlines[:2]}..."
    return avg_score, summary

def run_demo():
    executive = ExecutiveAgent()
    
    print("\nXXX --- RUNNING DUMMY TEST SCENARIOS (INDIAN MARKET CONTEXT) --- XXX\n")

    # SCENARIO 1: The "To the Moon" (Bullish News + Bullish Tech)
    print(">>> TEST CASE 1: INFOSYS (Bullish News + Bullish Tech)")
    news_1 = [
        "Infosys reports 20% jump in quarterly profits",
        "Infosys signs massive deal with global AI firm",
        "Analysts upgrade Infosys rating to Buy"
    ]
    news_score_1, news_summary_1 = analyze_mock_news(news_1)
    tech_score_1 = 0.85 
    tech_summary_1 = "Golden Cross verified. Price broke multi-year resistance. RSI Healthy (60)."
    
    print(executive.make_decision("INFY.NS", news_score_1, tech_score_1, news_summary_1, tech_summary_1))


    # SCENARIO 2: The "Market Crash" (Bearish News + Bearish Tech)
    print(">>> TEST CASE 2: ADANI ENT (Bad News + Breakdown)")
    news_2 = [
        "Reports allege accounting irregularities",
        "Stock plunges 10% as CEO steps down",
        "Regulatory body launches investigation"
    ]
    news_score_2, news_summary_2 = analyze_mock_news(news_2)
    tech_score_2 = -0.90
    tech_summary_2 = "Death Cross active. Price below all major SMAs. High volume selling."

    print(executive.make_decision("ADANIENT.NS", news_score_2, tech_score_2, news_summary_2, tech_summary_2))


    # SCENARIO 3: The "Confused Market" (Good News but Overbought Tech)
    print(">>> TEST CASE 3: ITC (Good News vs Overbought)")
    news_3 = [
        "ITC declares strong dividend payout",
        "FMCG sector looking positive for upcoming quarter"
    ]
    news_score_3, news_summary_3 = analyze_mock_news(news_3) # Should be positive
    tech_score_3 = -0.3 # Negative because maybe Overbought?
    tech_summary_3 = "RSI Extremely Overbought (85). Divergence detected. Price far above 50SMA (Correction likely)."

    print(executive.make_decision("ITC.NS", news_score_3, tech_score_3, news_summary_3, tech_summary_3))

if __name__ == "__main__":
    run_demo()
