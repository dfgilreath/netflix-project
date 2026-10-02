import pandas as pd

# Load raw Netflix global data
global_df = pd.read_csv(
    "data/raw/all-weeks-global.tsv",
    sep="\t"
)

print(f"Raw rows: {len(global_df):,}")

# Convert week to a date
global_df["week"] = pd.to_datetime(global_df["week"])

print(f"Date range: {global_df['week'].min().date()} to {global_df['week'].max().date()}")

# Keep records from the point where Netflix began reporting weekly views
# and runtime consistently.
global_df = global_df[global_df["week"] >= "2023-06-18"].copy()

print(f"Rows after date filter: {len(global_df):,}")
print(
    f"Filtered date range: "
    f"{global_df['week'].min().date()} to {global_df['week'].max().date()}"
)

# Create a single title field using season_title when available.
global_df["title"] = global_df["season_title"].fillna(global_df["show_title"])

print("\nSample titles:")
print(global_df[["show_title", "season_title", "title"]].head(10))