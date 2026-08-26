<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2073/day73banner.png" alt="Day 73 - Matplotlib Programming Languages Banner" width="100%">
</p>

# Day 73 - Data Visualisation with Matplotlib: Programming Languages 📈💻

A deep dive into visualizing StackOverflow question trends per programming language over time — going from raw CSV data all the way to smoothed, multi-series time-series charts with `matplotlib`.

## 🗂️ Project Structure

```
DAY 73/
├── query.ipynb
├── QueryResults.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration
- Loads `QueryResults.csv` into a `DataFrame` with named columns (`DATE`, `TAG`, `POSTS`).
- Inspects the data with `.head()`, `.tail()`, `.shape`, and `.count()`.
- Aggregates total posts per language with `.groupby('TAG').sum()` to find which language has the most posts overall, and checks entry counts per language with `.groupby('TAG').count()`.

### Data Cleaning
- Converts the `DATE` column from a string (`"2008-07-01 00:00:00"`) to a proper `datetime` object using `pd.to_datetime()`, first on a single value to verify the conversion, then applied across the whole column.

### Data Manipulation
- Demonstrates `.pivot()` on a small toy dataset first, to build intuition before applying it to the real data.
- Reshapes the long-format data (`DATE`, `TAG`, `POSTS`) into a wide-format table with one column per programming language and dates as the index.
- Fills missing values with `.fillna(0, inplace=True)` and verifies no `NaN`s remain with `.isna().values.any()`.

### Data Visualization with Matplotlib
- Builds up progressively richer charts:
  - A single language's post trend (Java) plotted on its own.
  - A larger, properly labeled chart (`figsize`, font sizes, axis labels, y-limit) for a single language.
  - Two languages (Java and Python) overlaid on the same axes for direct comparison.
  - **All** languages plotted at once using a `for` loop over `reshaped_df.columns`, with a legend labeling each line.
- **Smoothing time-series data:** applies a 6-month rolling average (`.rolling(window=6).mean()`) before plotting, which reduces noisy month-to-month spikes and reveals clearer long-term adoption trends for each language.

## 🧠 Concepts Practiced

- End-to-end data pipeline: load → explore → clean → reshape → visualize
- `datetime` conversion and its role in time-series analysis
- Reshaping data with `.pivot()` for multi-series plotting
- Handling missing data before visualization
- Building progressively more informative `matplotlib` charts (labels, legends, sizing)
- Rolling averages for smoothing noisy time-series trends

## 🚀 Run It

```bash
pip install pandas matplotlib jupyter
jupyter notebook query.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
