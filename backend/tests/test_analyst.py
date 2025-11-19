from src.agents.analyst import AnalystAgent

def test_analyst():
    agent = AnalystAgent()
    token = "DOGE"
    result = agent.analyze_onchain_data(token)
    print(f"\n--- Result for {token} ---")
    print(result)

if __name__ == "__main__":
    test_analyst()
