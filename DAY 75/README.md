<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2075/day75banner.png" alt="Day 75 - Google Trends Data Banner" width="100%">
</p>

# Day 75 - Google Trends Data: Resampling & Visualising Time Series 📉🔍

An investigation into whether Google search volume correlates with real-world signals — comparing Tesla search trends to its stock price, Bitcoin search interest to its price, and "Unemployment Benefits" search volume to the actual U.S. unemployment rate.

## 🗂️ Project Structure

```
DAY 75/
├── data_visualisation.ipynb
├── TESLA Search Trend vs Price.csv
├── Bitcoin Search Trend.csv
├── Daily Bitcoin Price.csv
├── UE Benefits Search vs UE Rate 2004-19.csv
├── UE Benefits Search vs UE Rate 2004-20.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration
- Loads four datasets: Tesla search vs. price, Bitcoin search trend, daily Bitcoin price, and unemployment benefits search vs. actual rate.
- Inspects shape, head, and `.describe()` for descriptive statistics; identifies max/min search values for Tesla and unemployment benefits queries.

### Data Cleaning
- Checks all four DataFrames for missing values with `.isna().values.any()`, finds and inspects the specific missing rows in the Bitcoin price data, then drops them.
- Converts date columns (`MONTH`/`DATE`) from strings to proper `datetime` objects across all four datasets.
- **Resamples** daily Bitcoin price data down to **monthly** frequency using `.resample('M', on='DATE').last()`, so it aligns with the monthly Google Trends data for comparison.

### Data Visualization (Dual-Axis Charts)
Builds a series of increasingly polished dual-axis line charts (`ax1.twinx()`), each comparing a search-trend line against a real-world metric:
- **Tesla:** stock price vs. search volume, progressively adding color styling, larger figure size, rotated x-axis labels, thicker lines, a title, DPI adjustments, axis limits, and proper year/month tick formatting via `matplotlib.dates`.
- **Bitcoin:** resampled monthly price vs. news search volume, styled with a dashed line for price and circle markers for search data points.
- **Unemployment:** actual U/E rate vs. "unemployment benefits" search volume, with a grid overlay for readability, and later a **6-month rolling average** applied to smooth out noise and reveal the underlying trend.
- **2020 comparison:** loads an extended dataset including 2020 data to see how the COVID-era unemployment spike shows up in both the actual rate and the search trend.

## 🧠 Concepts Practiced

- Comparing time series from different sources/frequencies (daily vs. monthly)
- Resampling data with `.resample()` to align mismatched frequencies
- Detecting and handling missing data
- Dual-axis (`twinx()`) charts for visualizing two differently-scaled metrics together
- Progressive chart styling: colors, fonts, DPI, axis limits, line styles, markers, grids
- Custom date-axis tick formatting with `matplotlib.dates` (`YearLocator`, `MonthLocator`, `DateFormatter`)
- Rolling averages for smoothing noisy search trend data
- Investigating real-world correlation questions through visualization (search interest vs. price/economic indicators)

## 🚀 Run It

```bash
pip install pandas matplotlib jupyter
jupyter notebook data_visualisation.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
