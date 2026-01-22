
Bitcoin Sentiment & Trader Performance Analysis

An exploratory data science project analyzing the relationship between the Bitcoin Fear & Greed Index and historical trader execution data from Hyperliquid.

📊 Project Overview

This project integrates daily market sentiment data with high-frequency trader activity to uncover how market psychology impacts PnL, risk-taking, and positioning. By processing over 211,000 trades, the analysis identifies specific "hidden patterns" where trader behavior deviates from the prevailing market mood.

🚀 Key Insights

1. Performance Distribution
Peak Profitability: Traders achieved the highest average PnL ($67.89) during Extreme Greed.

The Slump: Directionless Neutral markets resulted in the lowest profitability ($34.31), highlighting the difficulty of generating alpha in low-volatility environments.

2. The "Sell-Heavy" Hidden Pattern
Despite the extreme bullishness associated with Extreme Greed, the data revealed a significant counter-intuitive shift:

Positioning: The Sell-side ratio increased to 55.14% during Extreme Greed.

Interpretation: Top-performing traders on Hyperliquid appear to "fade" extreme retail euphoria, utilizing these periods for profit-taking or contrarian shorting rather than trend-following.

3. Risk Correlation
Fear vs. Greed: Profitability in Fear ($54.29) actually outperformed moderate Greed ($42.74), suggesting that volatility during fearful periods provides higher expectancy for disciplined traders.

🛠️ Tech Stack

Python 3.14

Pandas: Data cleaning, Unix timestamp normalization, and multi-dataset merging.

Seaborn/Matplotlib: Statistical data visualization.

📈 Strategic Recommendations

Sizing: Increase capital allocation during Extreme Greed but transition to a profit-taking bias.

Preservation: Reduce trading activity during Neutral sentiment phases to avoid capital erosion in "choppy" markets.
