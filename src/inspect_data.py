import pandas as pd

# Load Netflix Top 10 data
global_df = pd.read_csv("data/raw/all-weeks-global.tsv", sep="\t")
country_df = pd.read_csv("data/raw/all-weeks-countries.tsv", sep="\t")


# ============================================================
# BASIC DATASET INFORMATION
# ============================================================

print("=== GLOBAL DATA ===")
print(f"Rows: {len(global_df):,}")
print(f"Columns: {len(global_df.columns)}")
print(f"Date range: {global_df['week'].min()} to {global_df['week'].max()}")

print("\n=== COUNTRY DATA ===")
print(f"Rows: {len(country_df):,}")
print(f"Columns: {len(country_df.columns)}")
print(f"Date range: {country_df['week'].min()} to {country_df['week'].max()}")


# ============================================================
# COLUMN INFORMATION
# ============================================================

print("\n=== GLOBAL COLUMNS ===")
print(global_df.columns.tolist())

print("\n=== COUNTRY COLUMNS ===")
print(country_df.columns.tolist())


# ============================================================
# DATA QUALITY CHECKS
# ============================================================

print("\n=== GLOBAL DATA QUALITY ===")

print(f"Duplicate rows: {global_df.duplicated().sum():,}")
print(f"Missing values: {global_df.isna().sum().sum():,}")

print("\nMissing values by column:")
print(global_df.isna().sum())


print("\n=== COUNTRY DATA QUALITY ===")

print(f"Duplicate rows: {country_df.duplicated().sum():,}")
print(f"Missing values: {country_df.isna().sum().sum():,}")

print("\nMissing values by column:")
print(country_df.isna().sum())


# ============================================================
# CATEGORIES AND GEOGRAPHY
# ============================================================

print("\n=== GLOBAL CATEGORIES ===")
print(global_df["category"].value_counts())

print("\n=== COUNTRIES ===")
print(f"Unique countries: {country_df['country_iso2'].nunique():,}")

print("\n=== COUNTRY CATEGORIES ===")
print(country_df["category"].value_counts())


# ============================================================
# SAMPLE DATA
# ============================================================

print("\n=== GLOBAL SAMPLE ===")
print(global_df.head())

print("\n=== COUNTRY SAMPLE ===")
print(country_df.head())

# ============================================================
# INVESTIGATE MISSING VALUES
# ============================================================

print("\n=== GLOBAL ROWS MISSING WEEKLY VIEWS ===")
print(
    global_df[global_df["weekly_views"].isna()]
    [["week", "category", "show_title", "season_title"]]
    .head(10)
)

print("\n=== GLOBAL ROWS MISSING RUNTIME ===")
print(
    global_df[global_df["runtime"].isna()]
    [["week", "category", "show_title", "season_title"]]
    .head(10)
)

print("\n=== GLOBAL MISSING VIEWS BY CATEGORY ===")
print(
    global_df[global_df["weekly_views"].isna()]
    ["category"]
    .value_counts()
)

print("\n=== COUNTRY MISSING SEASON TITLE BY CATEGORY ===")
print(
    country_df[country_df["season_title"].isna()]
    ["category"]
    .value_counts()
)

# ============================================================
# INVESTIGATE MISSING GLOBAL METRICS OVER TIME
# ============================================================

print("\n=== MISSING VIEWS BY WEEK ===")

missing_views_by_week = (
    global_df[global_df["weekly_views"].isna()]
    .groupby("week")
    .size()
)

print(missing_views_by_week)


print("\n=== MISSING VIEWS BY CATEGORY AND WEEK ===")

missing_views_by_category_week = (
    global_df[global_df["weekly_views"].isna()]
    .groupby(["week", "category"])
    .size()
)

print(missing_views_by_category_week)