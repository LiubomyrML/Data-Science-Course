print("Starting my coffee project...")
import os
import urllib.request


FILENAME = os.path.join(os.path.dirname(__file__), "coffee_ratings.csv")
URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv"

if not os.path.exists(FILENAME):
    print(f"{FILENAME} not found. Downloading...", flush=True)
    urllib.request.urlretrieve(URL, FILENAME)
    print("Download complete.", flush=True)
else:
    print(f"{FILENAME} already exists. Skipping download.", flush=True)

import pandas as pd

data = pd.read_table(FILENAME, sep=",")

print(data.head())
data.info()
print(data.isna().sum())


print("\nDataset size:")
print(data.shape)

print("\nFive coffee records:")
print(data[["country_of_origin", "species", "total_cup_points"]].head())


print("\nRecords with a colour value:")
print(data["color"].count())
print(data["color"].isna().sum())

print("\nRecords with altitude_mean_meters")
print(data["altitude_mean_meters"].count())


print("\nCoffee species:")
print(data["species"].value_counts())

print("\nBean colours:")
print(data["color"].value_counts(dropna=False))


print("\nCoffee score summary:")
print(data["total_cup_points"].describe())

# DAY 1 FINDINGS
# The dataset contains 1,339 records and 43 columns.
# Arabica has 1,311 records; Robusta has 28.
# Colour is missing for 270 records.
# Mean altitude is missing for 230 records.
# The average total score is approximately 82.09.
# Scores range from 0 to 90.58; investigate the zero score.
# Missing values will be handled separately for each analysis.