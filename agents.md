# AlphaDivergence Agents

## Agent A: The Listener (Sentiment Analysis)
**Goal:** Detect trending tokens and analyze social sentiment.
- **Role:** The "Social Ear". Listens to social media to detect hype.
- **Data Sources:**
    - **Reddit:** Scrapes r/CryptoMoonShots, r/SatoshiStreetBets, etc. (Real)
- **Output:**
    - `hype_score` (0-100)
    - `trending_volume` (Low/Medium/High)
    - `sentiment_analysis` (Positive/Negative/Neutral)

---

## Agent B: The Analyst (On-Chain Forensics)
**Goal:** Verify if "Smart Money" is backing the hype.

**Data Sources:**
- **Etherscan / Solscan APIs:**
    - Check top holders.
    - Monitor "Whale" wallets (> $1M balance).
    - Track recent inflows/outflows for the specific token.

**Output:**
- `Net Smart Money Flow` (Buy/Sell/Neutral)
- `Whale Concentration` (% held by top 10 excluding CEX)
- `Liquidity Health`

---

## Agent C: The Judge (Risk Assessment)
**Goal:** Cross-reference Hype vs. Reality to flag risks.

**Logic:**
1.  **High Hype + Smart Money Buying** = ✅ **Potential Gem**
2.  **High Hype + Smart Money Selling** = 🚨 **Rug Pull Risk / Exit Liquidity Event**
3.  **Low Hype + Smart Money Buying** = 🕵️ **Accumulation Phase (Hidden Gem)**
4.  **Low Hype + Smart Money Selling** = 💀 **Dead Token**

**Output:**
- `Risk Level` (Low, Medium, High, Critical)
- `Verdict` (e.g., "Fake Hype Detected", "Organic Growth")
