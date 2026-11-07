import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from scipy.stats import spearmanr, kruskal


DATA_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv"
PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "coffee_ratings.csv"
CHART_DIR = PROJECT_DIR / "charts"
EXPECTED_SHAPE = (1339, 43)
SCORE_COLUMNS = [
    "aroma",
    "flavor",
    "aftertaste",
    "acidity",
    "body",
    "balance",
    "uniformity",
    "clean_cup",
    "sweetness",
    "cupper_points",
    "total_cup_points",
]
ANALYSIS_COLUMNS = [
    "country_of_origin",
    "number_of_bags",
    "species",
    "color",
    "altitude_mean_meters",
    *SCORE_COLUMNS,
]
CHART_FILENAMES = [
    "01_bags_by_country.png",
    "02_all_score_correlations.png",
    "03_selected_score_correlations.png",
    "04_scores_by_bean_color.png",
    "05_scores_by_country.png",
    "06_altitude_and_score.png",
]


def ensure_dataset(data_path=CSV_FILE):
    data_path = Path(data_path)
    if not os.path.exists(data_path):
        response = requests.get(DATA_URL, timeout=(10, 30))
        if response.status_code != 200:
            raise RuntimeError(
                f"Dataset download failed with HTTP {response.status_code}; expected HTTP 200."
            )
        data_path.write_bytes(response.content)
        print(f"Downloaded the coffee ratings dataset to {data_path}.")
    else:
        print(f"Using the existing coffee ratings dataset at {data_path}.")
    return data_path


def load_data(data_path=CSV_FILE):
    data_path = ensure_dataset(data_path)
    data = pd.read_table(data_path, dialect="excel")
    missing_columns = [column for column in ANALYSIS_COLUMNS if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required analysis columns: {missing_columns}.")
    if data.shape != EXPECTED_SHAPE:
        raise ValueError(
            f"Unexpected dataset shape {data.shape}; expected {EXPECTED_SHAPE[0]} rows by {EXPECTED_SHAPE[1]} columns."
        )
    numeric_columns = [
        "number_of_bags",
        "altitude_mean_meters",
        *SCORE_COLUMNS,
    ]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    print(f"Validated dataset: {data.shape[0]} rows by {data.shape[1]} columns.")
    return data


def save_chart(figure, filename):
    chart_path = CHART_DIR / filename
    try:
        figure.tight_layout()
        figure.savefig(chart_path, dpi=180, bbox_inches="tight")
    finally:
        plt.close(figure)
    print(f"Saved chart: {chart_path.name}")


def bags_by_country(data, zero_score_mask):
    print("\nTask 1: Bags represented by rated samples")
    zero_score_rows = data.loc[zero_score_mask]
    zero_score_bags = int(zero_score_rows["number_of_bags"].sum())
    zero_score_countries = set(zero_score_rows["country_of_origin"].dropna())
    if zero_score_bags != 275 or zero_score_countries != {"Honduras"}:
        raise ValueError("The zero-score record is not the expected 275-bag Honduras record.")
    print("The zero-score record remains in this task: Honduras, 275 bags.")

    missing_country = int(data["country_of_origin"].isna().sum())
    missing_bags = int(data["number_of_bags"].isna().sum())
    print(
        f"Rows missing country: {missing_country}; rows missing bag count: {missing_bags}. "
        "Country totals sum available bag counts."
    )
    totals = (
        data.groupby("country_of_origin")["number_of_bags"]
        .sum(min_count=1)
        .sort_values(ascending=False)
    )
    top_ten = totals.head(10)
    actual_top_three = [(name, int(value)) for name, value in top_ten.head(3).items()]
    expected_top_three = [
        ("Colombia", 41204),
        ("Guatemala", 36868),
        ("Brazil", 30534),
    ]
    if actual_top_three != expected_top_three:
        raise ValueError(f"Unexpected top-three bag totals: {actual_top_three}.")
    print("Top ten countries by bags recorded for rated samples:")
    print(top_ten.to_string())

    figure, axis = plt.subplots(figsize=(10, 6))
    axis.barh(top_ten.index, top_ten.values, color=sns.color_palette("YlOrBr", len(top_ten)))
    axis.invert_yaxis()
    axis.set_title("Top 10 countries by bags in rated samples\nNot total national coffee production")
    axis.set_xlabel("Number of bags represented by rated samples")
    axis.set_ylabel("Country of origin")
    save_chart(figure, CHART_FILENAMES[0])


def score_correlations(scores):
    print("\nTask 2: Pearson correlations between coffee scores")
    score_values = scores[SCORE_COLUMNS].apply(pd.to_numeric, errors="coerce")
    sample_report = pd.DataFrame(
        {
            "valid_samples": score_values.count(),
            "missing_samples": score_values.isna().sum(),
        }
    )
    print("Samples used for each score measure:")
    print(sample_report.to_string())
    correlations = score_values.corr(method="pearson")

    figure, axis = plt.subplots(figsize=(13, 10))
    sns.heatmap(
        correlations,
        annot=True,
        fmt=".2f",
        vmin=-1,
        vmax=1,
        cmap="vlag",
        square=True,
        ax=axis,
    )
    axis.set_title("All coffee score measures: Pearson correlations")
    save_chart(figure, CHART_FILENAMES[1])

    excluded = {"sweetness", "uniformity", "clean_cup"}
    eligible = [column for column in SCORE_COLUMNS if column not in excluded]
    pair_counts = score_values[eligible].notna().astype(int).T.dot(
        score_values[eligible].notna().astype(int)
    )
    pairs = []
    for index, first in enumerate(eligible):
        for second in eligible[index + 1 :]:
            coefficient = correlations.loc[first, second]
            if pd.notna(coefficient) and coefficient >= 0.65:
                pairs.append((first, second, coefficient, int(pair_counts.loc[first, second])))

    print("Distinct score pairs with Pearson r >= 0.65:")
    for first, second, coefficient, count in sorted(pairs, key=lambda pair: pair[2], reverse=True):
        print(f"  {first} and {second}: r={coefficient:.4f}, n={count}")
    measures = [
        column
        for column in eligible
        if any(column in (first, second) for first, second, _, _ in pairs)
    ]
    if not measures:
        raise ValueError("No distinct score pairs reached Pearson r >= 0.65.")
    figure, axis = plt.subplots(figsize=(11, 9))
    sns.heatmap(
        correlations.loc[measures, measures],
        annot=True,
        fmt=".2f",
        vmin=-1,
        vmax=1,
        cmap="vlag",
        square=True,
        ax=axis,
    )
    axis.set_title(
        "Measures participating in pairs with Pearson r >= 0.65\n"
        "Other displayed cells may have r below 0.65"
    )
    save_chart(figure, CHART_FILENAMES[2])


def scores_by_color(scores):
    print("\nTask 3: Mean coffee score by species and bean color")
    fields = ["species", "color", "total_cup_points"]
    missing_by_field = scores[fields].isna().sum()
    subset = scores.dropna(subset=fields)
    print(
        f"Rows excluded for missing task fields: {len(scores) - len(subset)} of {len(scores)}."
    )
    print("Missing values by field:")
    print(missing_by_field.to_string())
    means = subset.pivot_table(
        index="species",
        columns="color",
        values="total_cup_points",
        aggfunc="mean",
        observed=True,
    )
    counts = subset.pivot_table(
        index="species",
        columns="color",
        values="total_cup_points",
        aggfunc="count",
        observed=True,
    ).reindex(index=means.index, columns=means.columns, fill_value=0).fillna(0).astype(int)
    print("Mean scores by species and bean color:")
    print(means.round(2).to_string())
    print("Sample counts by species and bean color:")
    print(counts.to_string())
    for species in means.index:
        for bean_color in means.columns:
            mean_score = means.loc[species, bean_color]
            sample_count = int(counts.loc[species, bean_color])
            if pd.isna(mean_score):
                print(f"  {species}, {bean_color}: no samples (n={sample_count})")
            else:
                print(f"  {species}, {bean_color}: mean={mean_score:.2f}, n={sample_count}")

    palette = sns.color_palette("husl", n_colors=len(means.columns))
    figure, axis = plt.subplots(figsize=(11, 6))
    means.plot.bar(ax=axis, color=palette, rot=0)
    axis.set_title("Mean coffee score by species and bean color")
    axis.set_xlabel("Species")
    axis.set_ylabel("Mean total cup points")
    axis.legend(title="Bean color")
    save_chart(figure, CHART_FILENAMES[3])


def scores_by_country(scores):
    print("\nTask 4: Coffee score by country of origin")
    fields = ["country_of_origin", "total_cup_points"]
    missing_by_field = scores[fields].isna().sum()
    subset = scores.dropna(subset=fields)
    print(
        f"Rows excluded for missing task fields: {len(scores) - len(subset)} of {len(scores)}."
    )
    print("Missing values by field:")
    print(missing_by_field.to_string())
    summary = subset.groupby("country_of_origin")["total_cup_points"].agg(
        mean="mean", count="count"
    )
    print("Mean score and valid sample count for every country:")
    print(summary.sort_values("mean", ascending=False).round(2).to_string())

    minimum_samples = 10
    shown = summary.loc[summary["count"] >= minimum_samples].sort_values("mean")
    if len(shown) < 2:
        raise ValueError("Kruskal-Wallis requires at least two countries with 10 valid samples each.")
    print(
        f"The country chart and test include {len(shown)} countries with at least "
        f"{minimum_samples} valid samples each."
    )
    print(
        "Country names have no meaningful numerical order, so Spearman correlation is not applicable."
    )
    print(
        "Kruskal-Wallis compares score distributions across the countries shown; it does not "
        "prove causation or identify which individual countries differ."
    )
    groups = [
        subset.loc[subset["country_of_origin"].eq(country), "total_cup_points"]
        for country in shown.index
    ]
    statistic, p_value = kruskal(*groups)
    print(f"Kruskal-Wallis test: H={statistic:.6f}, p={p_value:.6g}.")

    labels = [f"{country} (n={int(row['count'])})" for country, row in shown.iterrows()]
    figure, axis = plt.subplots(figsize=(12, 9))
    axis.barh(labels, shown["mean"], color=sns.color_palette("viridis", n_colors=len(shown)))
    axis.set_title(f"Mean coffee score by country (minimum {minimum_samples} valid samples)")
    axis.set_xlabel("Mean total cup points")
    axis.set_ylabel("Country of origin and valid sample count")
    axis.set_xlim(0, shown["mean"].max() + 8)
    save_chart(figure, CHART_FILENAMES[4])


def altitude_and_score(scores):
    print("\nTask 5: Altitude and coffee score")
    altitude_column = "altitude_mean_meters"
    score_column = "total_cup_points"
    missing_altitude = scores[altitude_column].isna()
    missing_score = scores[score_column].isna()
    missing_either = missing_altitude | missing_score
    available = scores.loc[~missing_either].copy()
    print(
        f"Missing altitude: {int(missing_altitude.sum())}; missing score: {int(missing_score.sum())}; "
        f"rows removed for either missing field: {int(missing_either.sum())}."
    )
    in_range = available[altitude_column].between(0, 3000, inclusive="both")
    subset = available.loc[in_range].copy()
    print(
        f"Altitude cleaning range: 0 to 3,000 meters inclusive; "
        f"additional records removed: {len(available) - len(subset)}."
    )
    print("This altitude range is an analysis choice and does not verify the original altitude values.")
    print(f"Samples remaining for altitude analysis: {len(subset)}.")
    result = spearmanr(subset[altitude_column], subset[score_column])
    print(
        f"Spearman association: rho={result.statistic:.6f}, p={result.pvalue:.6g}; "
        "this describes association, not causation."
    )

    figure, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.kdeplot(
        data=subset,
        x=altitude_column,
        y=score_column,
        fill=True,
        cmap="Blues",
        levels=12,
        ax=axes[0],
        cut=0,
    )
    axes[0].set_title("Altitude and score: two-dimensional density")
    hexagons = axes[1].hexbin(
        subset[altitude_column],
        subset[score_column],
        gridsize=35,
        mincnt=1,
        cmap="viridis",
    )
    axes[1].set_title("Altitude and score: sample counts")
    figure.colorbar(hexagons, ax=axes[1], label="Rated samples per hexagon")
    for axis in axes:
        for altitude in (500, 2000):
            axis.axvline(altitude, color="darkorange", linestyle="--", linewidth=1)
        for score in (80, 85):
            axis.axhline(score, color="firebrick", linestyle="--", linewidth=1)
        axis.set_xlabel("Mean altitude (meters)")
        axis.set_ylabel("Total cup points")
    save_chart(figure, CHART_FILENAMES[5])


def validate_chart_outputs():
    missing = [filename for filename in CHART_FILENAMES if not (CHART_DIR / filename).is_file()]
    if missing:
        raise RuntimeError(f"Required charts were not created: {missing}.")
    for filename in CHART_FILENAMES:
        chart_path = CHART_DIR / filename
        if chart_path.stat().st_size == 0:
            raise RuntimeError(f"Required chart is empty: {chart_path}.")
        image = plt.imread(chart_path)
        if image.ndim != 3 or image.shape[0] < 1 or image.shape[1] < 1:
            raise RuntimeError(f"Required chart is not a readable PNG: {chart_path}.")
    print("Verified that all six required charts are nonempty, readable PNG files.")


def main():
    sns.set_theme(style="whitegrid")
    CHART_DIR.mkdir(exist_ok=True)
    data = load_data()
    zero_score_mask = data["total_cup_points"].eq(0).fillna(False)
    zero_score_count = int(zero_score_mask.sum())
    if zero_score_count != 1:
        raise ValueError(f"Expected one zero-score record; found {zero_score_count}.")
    print(
        "The one zero-score record is treated as suspect and excluded from score analyses; "
        "its cause is unverified."
    )
    bags_by_country(data, zero_score_mask)
    scores = data.loc[~zero_score_mask].copy()
    print(
        f"Score-analysis dataset: {len(scores)} rows; only the suspect zero-score record is excluded. "
        "Each task handles missing values separately."
    )
    score_correlations(scores)
    scores_by_color(scores)
    scores_by_country(scores)
    altitude_and_score(scores)
    validate_chart_outputs()
    print(f"All five tasks completed. Charts are saved in {CHART_DIR}.")


if __name__ == "__main__":
    main()
