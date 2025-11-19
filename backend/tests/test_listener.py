from src.agents.listener import ListenerAgent

def test_listener():
    agent = ListenerAgent()
    token = "DOGE"
    result = agent.analyze_sentiment(token)
    print(f"\n--- Result for {token} ---")
    print(result)

if __name__ == "__main__":
    test_listener()
