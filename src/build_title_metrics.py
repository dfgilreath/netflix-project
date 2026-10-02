import pandas as pd

# Load the cleaned global dataset
global_df = pd.read_csv("data/processed/global_clean.csv")

print(f"Rows loaded: {len(global_df):,}")
print(f"Unique titles: {global_df['title'].nunique():,}")

# Build title-level metrics
title_metrics = (
    global_df
    .groupby(["category", "title"])
    .agg(
        total_views=("weekly_views", "sum"),
        total_hours_viewed=("weekly_hours_viewed", "sum"),
        avg_weekly_views=("weekly_views", "mean"),
        avg_weekly_hours_viewed=("weekly_hours_viewed", "mean"),
        peak_weekly_views=("weekly_views", "max"),
        peak_weekly_hours_viewed=("weekly_hours_viewed", "max"),
        weeks_in_top_10=("week", "count"),
        peak_rank=("weekly_rank", "min"),
        avg_rank=("weekly_rank", "mean"),
        first_appearance=("week", "min"),
        last_appearance=("week", "max"),
    )
    .reset_index()
)

print("\n=== TITLE METRICS ===")
print(f"Rows: {len(title_metrics):,}")
print(f"Columns: {len(title_metrics.columns)}")

print("\nColumns:")
print(title_metrics.columns.tolist())

print("\nSample:")
print(title_metrics.head(10))

print("\nMissing values:")
print(title_metrics.isna().sum())

# Save title-level metrics
output_path = "data/processed/title_metrics.csv"
title_metrics.to_csv(output_path, index=False)

print(f"\nSaved title metrics to {output_path}")