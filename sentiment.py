import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
trader_df = pd.read_csv('historical_data.csv')
sentiment_df = pd.read_csv('fear_greed_index.csv')

# 2. Clean column names
trader_df.columns = trader_df.columns.str.strip().str.lower()
sentiment_df.columns = sentiment_df.columns.str.strip().str.lower()

print("Columns found in Trader Data:", trader_df.columns.tolist())

# 3. Detect date columns and convert
sent_date_col = [c for c in sentiment_df.columns if 'time' in c or 'date' in c or 'stamp' in c][0]
trader_time_col = [c for c in trader_df.columns if 'time' in c or 'date' in c or 'stamp' in c][0]

sentiment_df['merge_date'] = pd.to_datetime(sentiment_df[sent_date_col], unit='s').dt.date
trader_df['merge_date'] = pd.to_datetime(trader_df[trader_time_col], dayfirst=True, errors='coerce').dt.date

# 4. Merge
merged_df = pd.merge(trader_df, sentiment_df, on='merge_date', how='inner').dropna(subset=['merge_date'])

# 5. Define Logical Order
order = ['extreme fear', 'fear', 'neutral', 'greed', 'extreme greed']
class_col = [c for c in merged_df.columns if 'class' in c or 'fear' in c][0]
merged_df[class_col] = merged_df[class_col].str.lower()

# 6. DYNAMIC COLUMN FINDER (Failsafe)
def find_col(possible_names, df):
    for name in possible_names:
        found = [c for c in df.columns if name in c]
        if found: return found[0]
    return None

pnl_col = find_col(['pnl', 'profit'], merged_df)
lev_col = find_col(['leverage', 'lev', 'margin'], merged_df)
size_col = find_col(['size', 'qty', 'amount', 'volume'], merged_df)
side_col = find_col(['side', 'dir', 'type'], merged_df)

# 7. Analysis with existence checks
print("\n--- PERFORMANCE SUMMARY ---")
pnl_stats = merged_df.groupby(class_col)[pnl_col].mean().reindex(order)
print(pnl_stats)

if lev_col and size_col:
    print("\n--- RISK SUMMARY ---")
    risk_stats = merged_df.groupby(class_col)[[lev_col, size_col]].mean().reindex(order)
    print(risk_stats)

if side_col:
    print("\n--- POSITIONING (LONG/SHORT %) ---")
    pos_stats = pd.crosstab(merged_df[class_col], merged_df[side_col], normalize='index').reindex(order)
    print(pos_stats * 100)

# 8. Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=pnl_stats.index, y=pnl_stats.values, palette='RdYlGn')
plt.title('Average PnL vs Market Sentiment')
plt.savefig('trading_analysis_final.png')
print("\nSuccess! Results printed and chart saved as 'trading_analysis_final.png'.")

