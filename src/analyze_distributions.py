import pandas as pd


# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------

global_df = pd.read_csv("data/processed/global_clean.csv")
title_metrics = pd.read_csv("data/processed/title_metrics.csv")


# ---------------------------------------------------------
# Dataset overview
# ---------------------------------------------------------

print("\n=== DATASET OVERVIEW ===")

print(f"Global rows: {len(global_df):,}")
print(f"Title metric rows: {len(title_metrics):,}")
print(f"Unique titles: {title_metrics['title'].nunique():,}")

print(
    f"Date range: "
    f"{global_df['week'].min()} to {global_df['week'].max()}"
)

print("\nCategories:")
print(global_df["category"].value_counts().sort_index())


# ---------------------------------------------------------
# Metric distributions
# ---------------------------------------------------------

distribution_metrics = [
    "total_views",
    "total_hours_viewed",
    "avg_weekly_views",
    "avg_weekly_hours_viewed",
    "weeks_in_top_10",
    "peak_weekly_views",
    "peak_weekly_hours_viewed",
]

print("\n=== METRIC DISTRIBUTIONS ===")

for metric in distribution_metrics:
    print(f"\n--- {metric} ---")

    summary = (
        title_metrics
        .groupby("category")[metric]
        .agg(
            count="count",
            mean="mean",
            median="median",
            min="min",
            max="max",
        )
        .round(2)
    )

    print(summary)


# ---------------------------------------------------------
# Metric correlation
# ---------------------------------------------------------

print("\n=== VIEWS VS HOURS CORRELATION ===")

overall_correlation = title_metrics["total_views"].corr(
    title_metrics["total_hours_viewed"]
)

print(f"Overall: {overall_correlation:.3f}")

category_correlations = (
    title_metrics
    .groupby("category")
    .apply(
        lambda group: group["total_views"].corr(
            group["total_hours_viewed"]
        ),
        include_groups=False
    )
)

print("\nBy category:")
print(category_correlations.round(3))


# ---------------------------------------------------------
# Top titles by metric
# ---------------------------------------------------------

print("\n=== TOP 10 TITLES BY METRIC ===")

ranking_metrics = [
    "total_views",
    "total_hours_viewed",
    "avg_weekly_views",
    "weeks_in_top_10",
    "peak_weekly_views",
]

for metric in ranking_metrics:
    print(f"\n--- {metric} ---")

    top_titles = (
        title_metrics
        .nlargest(10, metric)[
            ["category", "title", metric]
        ]
    )

    print(top_titles.to_string(index=False))


print("\n=== ANALYSIS COMPLETE ===")