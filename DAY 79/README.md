<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2079/day79banner.png" alt="Day 79 - Nobel Prize Analysis Banner" width="100%">
</p>

# Day 79 - Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn 🏅🌍

A deep, multi-tool investigation into over a century of Nobel Prize data — exploring gender gaps, repeat winners, category trends, geographic patterns, top institutions, and how laureate age at the time of winning has shifted over time.

## 🗂️ Project Structure

```
DAY 79/
├── nobel_prize_analysis.ipynb
├── nobel_prize_data.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration & Cleaning
- Checks shape, duplicates, and NaN values — discovering that missing `birth_date` and `organization_name` values reveal something meaningful: some prizes go to **organizations**, not individuals.
- Converts `birth_date` to `datetime`, and derives a `share_pct` column from the `prize_share` string (e.g. `"1/3"` → `0.33`) by splitting and converting to numeric.

### Gender & Repeat Winners
- **Donut chart (Plotly):** percentage of male vs. female laureates.
- Identifies the first 3 female Nobel laureates and their categories.
- Finds **repeat winners** two different ways — `.duplicated(subset=...)` and a `.groupby().filter()` approach — cross-checking the same answer with two techniques.

### Category-Level Analysis
- Bar chart of prizes awarded per category (Plotly, `Aggrnyl` color scale).
- Finds when the Economics category was first awarded (it was added later than the original five).
- **Grouped bar chart:** male vs. female winners split by category.

### Trends Over Time
- Line/scatter charts with a **5-year rolling average** showing how many prizes are awarded per year, with custom x-axis tick spacing (every 5 years) — visually inspecting whether the World Wars caused visible dips.
- **Dual-axis chart:** overlays the rolling average of prize *share percentage* against the prize count trend, with the secondary axis inverted for clearer comparison.

### Geographic Analysis
- Horizontal bar chart of the top 20 countries by number of prizes, discussing the tradeoffs between `birth_country`, `birth_country_current`, and `organization_country` as the "correct" country to attribute a prize to.
- **Choropleth world map (Plotly)** visualizing prize counts by country using ISO codes.
- **Stacked/grouped horizontal bar chart** breaking down each top-20 country's prizes by category (built via a two-step `groupby` + `merge`).
- **Cumulative line chart** tracking each country's total prize count over time — revealing when the U.S. overtook other nations as the leading country.

### Institutions & Cities
- Top 20 research institutions and top 20 organization cities by prize count.
- Top 20 laureate **birth cities**.
- **Sunburst chart (Plotly):** hierarchical breakdown of country → city → organization.

### Laureate Age Analysis
- Computes `winning_age` (award year minus birth year) as a new column.
- Finds the oldest and youngest laureates ever, and descriptive statistics (mean, quartiles) for winning age.
- **Histogram (Seaborn):** distribution of winning ages, experimenting with different bin counts.
- **Regression plot with LOWESS smoothing (Seaborn):** age at time of award over history, to see if laureates are winning later in life.
- **Box plots (Seaborn and Plotly):** winning age distribution by category, sorted by mean age.
- **Faceted regression plots (`sns.lmplot()`):** age trends per category shown as separate subplots (`row=`) and then overlaid on one chart (`hue=`), comparing whether different categories show different long-term age trends.

## 🧠 Concepts Practiced

- Deep, multi-stage exploratory data analysis on a rich real-world dataset
- Understanding *why* missing data exists rather than just detecting it
- String parsing and derived column creation (`share_pct`)
- A wide range of chart types: donut, bar (vertical/horizontal/grouped/stacked), choropleth map, sunburst, scatter with rolling average, dual-axis, histogram, box plot, and faceted regression plots
- Combining `Plotly`, `Matplotlib`, and `Seaborn` in one analysis, choosing the right tool per chart type
- Cross-verifying a result using two different pandas approaches
- LOWESS-smoothed trend lines for non-linear historical patterns

## 🚀 Run It

```bash
pip install pandas numpy plotly seaborn matplotlib jupyter
jupyter notebook nobel_prize_analysis.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
