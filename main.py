import sys
from agents.news_agent import NewsAgent
from agents.technical_agent import TechnicalAgent
from agents.executive_agent import ExecutiveAgent

def run_system():
    print("Initializing Financial Multi-Agent System...")
    
    # Initialize Agents
    news_agent = NewsAgent()
    tech_agent = TechnicalAgent()
    executive = ExecutiveAgent()

    # Get Ticker
    if len(sys.argv) > 1:
        ticker = sys.argv[1].upper()
    else:
        ticker = input("Enter Indian Stock Ticker (e.g., RELIANCE, TATASTEEL): ").upper().strip()
    
    if not ticker:
        print("Invalid ticker.")
        return

    # Auto-append .NS for Indian NSE if no suffix provided
    if not ticker.endswith(".NS") and not ticker.endswith(".BO"):
        print(f"Assuming NSE for {ticker} -> {ticker}.NS")
        ticker = f"{ticker}.NS"

    print(f"\n--- Starting Analysis for {ticker} ---\n")

    # Parallel execution is possible here, but for simplicity we run sequential
    sentiment_score, sentiment_summary = news_agent.get_market_sentiment(ticker)
    tech_score, tech_summary = tech_agent.analyze_price_action(ticker)
    
    # Executive Decision
    final_output = executive.make_decision(
        ticker, 
        sentiment_score, 
        tech_score, 
        sentiment_summary, # Pass summaries for display
        tech_summary
    )
    
    print(final_output)

if __name__ == "__main__":
    run_system()
