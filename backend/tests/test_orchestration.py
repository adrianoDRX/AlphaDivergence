from src.agents.listener import ListenerAgent
from src.agents.analyst import AnalystAgent
from src.agents.judge import JudgeAgent

def run_orchestration():
    # Initialize Agents
    listener = ListenerAgent()
    analyst = AnalystAgent()
    judge = JudgeAgent()

    token = "PEPE"
    print(f"--- Starting AlphaDivergence Analysis for {token} ---\n")

    # 1. Listener Agent
    hype_data = listener.analyze_sentiment(token)
    print(f"Listener Output: Hype Score {hype_data['hype_score']} | Volume {hype_data['trending_volume']}")

    # 2. Analyst Agent
    onchain_data = analyst.analyze_onchain_data(token)
    print(f"Analyst Output: Flow {onchain_data['net_smart_money_flow']} | Whale Conc {onchain_data['whale_concentration']}%")

    # 3. Judge Agent
    verdict = judge.assess_risk(hype_data, onchain_data)
    
    print("\n--- FINAL VERDICT ---")
    print(f"Risk Level: {verdict['risk_level']}")
    print(f"Verdict: {verdict['verdict']}")
    print(f"Reasoning: {verdict['reasoning']}")

if __name__ == "__main__":
    run_orchestration()
