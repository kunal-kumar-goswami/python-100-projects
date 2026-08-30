<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2099/day99banner.png" alt="Day 99 - Space Race Analysis Banner" width="100%">
</p>

# Day 99 - Professional Portfolio: Data Science — Analysing the Space Race 🚀🌍

A capstone-level data science deep dive into every space mission since 1957 — covering organizations, countries, costs, success/failure rates, and a full geopolitical comparison of the USA vs. USSR space race, using `pandas`, `Plotly`, `Matplotlib`, and `Seaborn` together.

## 🗂️ Project Structure

```
DAY 99/
├── space_race_analyzing.ipynb
├── mission_launches.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Cleaning
- Drops junk index columns (`Unnamed: 0`, `Unnamed: 0.1`) left over from the original scrape.
- Cleans the `Price` column (stored as a comma-formatted string) into a proper numeric type for statistics and aggregation.

### Organizations & Rockets
- Counts launches per organization and active vs. retired rocket status.
- Breaks down mission outcomes (`Mission_Status`) to see success/failure distribution.
- **Histogram:** distribution of launch prices (in USD millions).

### Geographic Analysis
- **Country extraction & wrangling:** derives a `Country` column from the `Location` field, then manually corrects a long list of edge cases (military test sites, disputed/renamed regions, historical USSR territory) before converting names to ISO Alpha-3 codes via the `iso3166` package.
- **Choropleth maps (Plotly):** total launches by country, and separately, total **mission failures** by country.
- **Sunburst chart:** hierarchical breakdown of Country → Organization → Mission Status.

### Financial Analysis
- Total money spent per organization, and average cost per launch per organization — revealing which players run the most expensive vs. most cost-efficient programs.

### Time-Based Trends
- Launches per year and per calendar month (finding the most/least popular months for launches — likely influenced by weather).
- Average launch price trend over time (`.groupby("year").mean()`).
- Top 10 most active organizations' launch activity over time (via a histogram).

### Cold War Deep Dive: USA vs. USSR
- Filters to just USA/Russia (including historical Soviet launches) for the Cold War period (through 1991).
- **Pie chart:** total launch share between the two superpowers.
- **Year-on-year line chart:** launches per year for each superpower, unstacked for direct comparison.
- **Sunburst + pie charts:** mission failures by year, and how failure rates changed over time (did the superpowers get safer as the space race matured?).

### Leadership Over Time
- For every year, identifies which **country** led in total launches, and separately which **organization** led — visualized as a multi-line chart showing shifting dominance (e.g. Cold War-era Soviet/US agencies vs. modern players like CASC in the 2018–2020 era).

## 🧠 Concepts Practiced

- Real-world messy data cleaning (junk columns, inconsistent location naming, currency-formatted strings)
- Country name normalization and ISO code mapping for geographic visualization
- Choropleth and sunburst charts for hierarchical/geographic data
- Multi-library visualization (Plotly, Matplotlib, Seaborn) chosen per chart type
- Historical/geopolitical trend analysis through data (Cold War space race dynamics)
- Time-based aggregation and leadership/dominance tracking across categories

## 🚀 Run It

```bash
pip install pandas numpy plotly matplotlib seaborn iso3166 jupyter
jupyter notebook space_race_analyzing.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
