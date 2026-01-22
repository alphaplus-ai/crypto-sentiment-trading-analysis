import pandas as pd

# 1. Load data
trader_df = pd.read_csv('historical_data.csv')
sentiment_df = pd.read_csv('fear_greed_index.csv')

# 2. Clean column names (lowercase and remove spaces)
trader_df.columns = trader_df.columns.str.strip().str.lower()
sentiment_df.columns = sentiment_df.columns.str.strip().str.lower()

# 3. AUTO-DETECT Date/Time Columns
# Finds the first column that has 'time' or 'date' in its name
try:
    sent_date_col = [c for c in sentiment_df.columns if 'time' in c or 'date' in c][0]
    trader_time_col = [c for c in trader_df.columns if 'time' in c or 'date' in c][0]
    print(f"Detected columns: Sentiment='{sent_date_col}', Trader='{trader_time_col}'")
except IndexError:
    print("Error: Could not find a time/date column. Available columns are:")
    print("Trader:", trader_df.columns.tolist())
    print("Sentiment:", sentiment_df.columns.tolist())
    exit()

# 4. Convert Dates
# Sentiment: Unix seconds (1517463000)
sentiment_df['merge_date'] = pd.to_datetime(sentiment_df[sent_date_col], unit='s').dt.date

# Trader: String format with dayfirst handling
trader_df['merge_date'] = pd.to_datetime(trader_df[trader_time_col], dayfirst=True, errors='coerce').dt.date

# 5. Remove any rows with invalid dates
sentiment_df = sentiment_df.dropna(subset=['merge_date'])
trader_df = trader_df.dropna(subset=['merge_date'])

# 6. Merge the datasets
merged_df = pd.merge(trader_df, sentiment_df, on='merge_date', how='inner')

# 7. Final Output & Analysis
if merged_df.empty:
    print("No overlapping dates found.")
    print(f"Trader Dates: {trader_df['merge_date'].min()} to {trader_df['merge_date'].max()}")
    print(f"Sentiment Dates: {sentiment_df['merge_date'].min()} to {sentiment_df['merge_date'].max()}")
else:
    print(f"Success! Merged {len(merged_df)} rows.")
    
    # Auto-detect PnL and Classification columns
    pnl_col = [c for c in merged_df.columns if 'pnl' in c][0]
    class_col = [c for c in merged_df.columns if 'class' in c or 'fear' in c][0]
    
    # Final Analysis
    analysis = merged_df.groupby(class_col)[pnl_col].mean()
    print("\n--- Average PnL by Market Sentiment ---")
    print(analysis)