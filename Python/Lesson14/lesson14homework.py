"""Step-by-step analysis of the pandas movies dataset."""
from pathlib import Path
from urllib.request import urlopen

import pandas as pd

URL = (
    "https://gist.githubusercontent.com/tiangechen/"
    "b68782efa49a16edaf07dc2cdaa855ea/raw/"
    "0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv"
)
DATA_PATH = Path("movies.csv")
OUTPUT_PATH = Path("top_10_comedies.csv")

# 1. Download the dataset only when it is not already in the working directory.
if not DATA_PATH.exists():
    DATA_PATH.write_bytes(urlopen(URL, timeout=30).read())

movies = pd.read_csv(DATA_PATH)
initial_rows = len(movies)
movies = movies.drop_duplicates().copy()
print(f"\n1. Loaded {initial_rows} rows; {len(movies)} remain after removing exact duplicates.\n")

# 2. Inspect the fields, types, completeness, and descriptive statistics.
print("2. Columns:")
print(list(movies.columns))
print("\nData types:")
print(movies.dtypes.to_string())
print("\nDataFrame info:")
movies.info()
print("\nNumeric statistics:")
print(movies.describe().to_string())
print("\nCategory counts:")
for column in ["Genre", "Lead Studio", "Year"]:
    print(f"\n{column}:\n{movies[column].value_counts(dropna=False).sort_index().to_string()}")

# 3. Count movies (unique film titles, after removing repeated rows).
print(f"\n3. Unique film titles: {movies['Film'].nunique()}")

# 4. Count films released in each year.
print("\n4. Films per year:")
print(movies.groupby("Year")["Film"].count().sort_index().to_string())

# 5. Show complete records at the minimum and maximum profitability values.
profit_col = "Profitability"
print("\n5. Least profitable film(s):")
print(movies.loc[movies[profit_col].eq(movies[profit_col].min())].to_string(index=False))
print("\nMost profitable film(s):")
print(movies.loc[movies[profit_col].eq(movies[profit_col].max())].to_string(index=False))

# 6. Standardize known genre typos and inconsistent capitalization.
genre_fixes = {
    "romence": "Romance",
    "romance": "Romance",
    "comdy": "Comedy",
    "comedy": "Comedy",
}
print("\n6. Genres before correction:")
print(movies["Genre"].value_counts(dropna=False).to_string())
normalized = movies["Genre"].astype("string").str.strip()
movies["Genre"] = normalized.map(
    lambda value: genre_fixes.get(value.casefold(), value) if pd.notna(value) else value
)
print("\nGenres after correction:")
print(movies["Genre"].value_counts(dropna=False).to_string())

# 7. Export the ten highest audience-score comedies, with only requested columns.
# Sort by title as a stable tie-breaker when audience scores are equal.
top_comedies = (
    movies.loc[movies["Genre"].eq("Comedy")]
    .sort_values(["Audience score %", "Film"], ascending=[False, True], kind="stable")
    .head(10)[["Film", "Year", "Lead Studio"]]

)
top_comedies.to_csv(OUTPUT_PATH, index=False)
print(f"\n7. Saved {len(top_comedies)} rows to {OUTPUT_PATH}:")
print(top_comedies.to_string(index=False))

print("\n8. Requested pip installs (already run for this environment):")
print("python -m pip install lxml mysql-connector-python")