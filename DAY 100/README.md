<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%20100/day100banner.png" alt="Day 100 - Police Killings Analysis Banner" width="100%">
</p>

# Day 100 - Professional Portfolio: Data Science — Analysing Fatal Police Shootings 🎓🏁

The **final day** of the 100 Days of Code challenge — a comprehensive, multi-dataset socioeconomic analysis combining The Washington Post's fatal police shootings database with US Census data on poverty, education, and race, to explore the demographic and geographic patterns behind these deaths.

## 🗂️ Project Structure

```
DAY 100/
├── death_analyzing.ipynb
├── Deaths_by_Police_US.csv
├── Median_Household_Income_2015.csv
├── Pct_People_Below_Poverty_Level.csv
├── Pct_Over_25_Completed_High_School.csv
├── Share_of_Race_By_City.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Cleaning
- Loads five separate CSVs (fatalities, household income, poverty rate, high school completion, racial makeup by city), each requiring different `windows-1252` encoding handling.
- Fills missing income values with 0, converts placeholder `'-'` values in percentage columns to `NaN` before casting to numeric types, and checks all five DataFrames for duplicates.

### Socioeconomic Patterns by State
- **Bar chart:** poverty rate ranked by US state.
- **Scatter plot:** high school graduation rate by state.
- **Dual-axis chart:** poverty rate vs. graduation rate overlaid, to visually assess whether they move together.
- **Seaborn `.jointplot()` (KDE)** and **`.regplot()`/`.lmplot()`**: statistically visualizing and fitting a linear relationship between poverty and graduation rates.
- **Stacked bar chart:** racial makeup (white/black/Native American/Asian/Hispanic share) per state.

### The Fatalities Dataset
- **Donut chart:** victims by race, with custom percentage + count labels via a helper function (`make_autopct`).
- **Pie chart:** gender breakdown of victims.
- **Box plot:** age distribution by manner of death, split by gender.
- **Weapon analysis:** consolidates dozens of specific weapon types into a simplified "armed" vs. "unarmed" pie chart, plus a full horizontal bar chart of every weapon type recorded.
- **Age analysis:** percentage of victims under 25, plus histogram/KDE plots of age distribution overall and split by race.
- **Mental illness:** pie chart showing what share of victims had documented signs of mental illness.

### Geographic Analysis
- **Top 10 most-affected cities:** bar chart of raw killing counts.
- **Per-city racial breakdown:** for each of the top 10 cities, a separate bar chart showing which races were affected, to distinguish "more killings overall" from "disproportionate impact."
- **Choropleth map (Plotly `go.Figure`):** police killings by US state, directly comparable to the earlier poverty-rate-by-state chart to explore correlation.

### Trends Over Time
- **Monthly time series:** total killings per month across the full dataset period, to check for any long-term trend.

## 🐛 Notes on the current code

- **A calculation error in the "under 25" percentage:** `round((under / over) * 100)` divides the under-25 count by the *over-25* count, not by the *total* count — so this doesn't actually compute "the percentage of people killed who were under 25." A correct version would be `under / (under + over) * 100`, dividing by the total rather than just the complementary group.
- **Deprecated pandas method:** `top_10 = top_10.append(org, ...)` in an earlier day's space-race notebook pattern (and similar patterns here) rely on `.append()`, which was removed in modern pandas versions — `pd.concat()` is the current replacement.

## 🧠 Concepts Practiced

- Merging insights across multiple independent datasets (fatalities + four census datasets)
- Comprehensive data cleaning across differently-encoded, inconsistently-formatted CSVs
- A very wide range of chart types: bar, scatter, dual-axis, KDE jointplot, regression plot, stacked bar, donut/pie, box plot, histogram, choropleth, and time series
- Socioeconomic correlation analysis (poverty vs. education, poverty vs. killings by state)
- Careful, sensitive handling and presentation of real demographic data
- Custom labeling functions for enhanced pie chart readability

## 🎓 Closing Note

This marks **Day 100 of 100** — the completion of the full 100 Days of Code journey, from `print("Hello, World!")` through data structures, OOP, web development, Flask, databases, authentication, GUIs, games, and finally a full portfolio of real-world data science and automation projects.

## 🚀 Run It

```bash
pip install pandas numpy plotly matplotlib seaborn jupyter
jupyter notebook death_analyzing.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)🎉
