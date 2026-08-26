<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2072/day72banner.png" alt="Day 72 - Pandas Data Exploration Banner" width="100%">
</p>

# Day 72 - Data Exploration with Pandas 📊🐼

A Jupyter notebook exploring a StackOverflow post-count dataset (posts per programming language over time), practicing core `pandas` data exploration, cleaning, reshaping, and visualization with `matplotlib`.

> **Note:** the notebook file is named `salaries_by_college.ipynb`, but its actual content analyzes StackOverflow post volume per programming language over time (Java, Python, etc.), not college major or salary data. This README documents what the notebook actually contains.

## 🗂️ Project Structure

```
DAY 72/
├── salaries_by_college.ipynb
├── QueryResults.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration
- Loads `QueryResults.csv` into a `DataFrame` with named columns (`DATE`, `TAG`, `POSTS`).
- Inspects the data with `.head()`, `.tail()`, `.shape`, and `.count()`.
- Aggregates total posts per language with `.groupby('TAG').sum()`, and counts how many months of data exist per language with `.groupby('TAG').count()`.

### Data Cleaning
- Converts the `DATE` column from string to proper `datetime` objects using `pd.to_datetime()`, both on a single value and across the whole column.

### Data Manipulation
- Demonstrates `.pivot()` on a small example dataset, then applies the same technique to reshape the real data — turning long-format (`DATE`, `TAG`, `POSTS`) rows into a wide-format table with one column per programming language.
- Handles missing values with `.fillna(0)` and checks for remaining NaNs with `.isna().values.any()`.

### Data Visualization
- Builds progressively richer `matplotlib` line charts:
  - A single language's post count over time.
  - Two languages overlaid on the same chart.
  - All languages plotted via a `for` loop, with legends and consistent axis formatting.
  - A **rolling average** (`.rolling(window=6).mean()`) applied before plotting, smoothing out noisy month-to-month fluctuations to reveal clearer long-term trends.

## 🧠 Concepts Practiced

- Loading and inspecting CSV data with `pandas`
- Aggregation with `.groupby()`
- Date/time conversion and handling
- Reshaping data with `.pivot()`
- Handling missing data (`.fillna()`, `.isna()`)
- Time-series visualization with `matplotlib`, including multi-series charts and rolling averages

## 🚀 Run It

```bash
pip install pandas matplotlib jupyter
jupyter notebook salaries_by_college.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
