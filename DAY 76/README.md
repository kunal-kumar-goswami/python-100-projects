<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2076/day76banner.png" alt="Day 76 - Plotly and App Store Banner" width="100%">
</p>

# Day 76 - Beautiful Plotly Charts & Analysing the Android App Store 📱📊

A comprehensive analysis of the Google Play Store app market — thousands of Android apps analyzed for ratings, size, installs, pricing, and revenue potential, visualized with interactive `Plotly` charts (pie, bar, scatter, box plots).

## 🗂️ Project Structure

```
DAY 76/
├── app_analytics.ipynb
├── apps.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Cleaning
- Drops unused columns (`Last_Updated`, `Android_Version`).
- Finds and removes rows with `NaN` ratings, creating a clean `df_apps_clean` DataFrame.
- Detects and removes duplicate app entries (e.g. multiple "Instagram" rows) with `.duplicated()`/`.drop_duplicates()`.

### Initial Exploration
- Identifies the highest-rated apps, and discusses the pitfall of relying on ratings alone (e.g. an app with a perfect 5-star rating from only 3 reviews isn't necessarily "the best").
- Finds the 5 largest apps by file size (MB) and the 5 apps with the most reviews, checking whether any paid apps make the top 50 by review count.

### Categorical Visualization
- Builds **Plotly pie/donut charts** to visualize the distribution of Content Ratings (Everyone, Teen, Mature, etc.).

### Numeric Cleaning & Installs Analysis
- Converts the `Installs` column (originally formatted like `"1,000,000+"`) into a proper numeric type via string cleaning, then finds how many apps have over 1 billion installs vs. just a single install.

### Pricing & Revenue Analysis
- Converts the `Price` column to numeric, investigates the top 20 most expensive apps, and filters out junk entries priced over $250.
- Adds a `Revenue_Estimate` column (`price × installs`) as a ballpark sales estimate, and identifies the top 10 highest-grossing paid apps — checking how many are games.

### Category-Level Visualization
- **Bar charts:** highest-competition categories (most apps) and most popular categories (highest downloads).
- **Scatter plot:** downloads vs. competition per category, using bubble size, hover labels, color, and a log-scaled y-axis to handle the wide range of values.

### Nested Genre Data
- Investigates the `Genres` column, where a single app can belong to multiple genres separated by a delimiter — uses `.split()` combined with `.stack()` to properly unpack and count genre frequencies (since naive `.value_counts()` on the raw column would treat multi-genre combos as single unique values).

### Advanced Comparisons
- **Colour-scaled bar chart:** genre competition, using Plotly's built-in continuous colour scales.
- **Grouped bar chart:** free vs. paid app counts per category, sorted by total descending.
- **Box plots:** installs for free vs. paid apps (showing the "lost downloads" cost of charging money), and revenue by app category (identifying which categories — like Tools or Photography — actually recoup typical development costs).
- **Pricing strategy box plot:** examines the median and distribution of paid app prices across categories.

## 🧠 Concepts Practiced

- Data cleaning: dropping columns, handling NaNs, removing duplicates
- Numeric type conversion from messy string-formatted columns
- Building an estimated revenue metric from raw data
- Interactive visualization with `Plotly Express`: pie, bar, scatter, and box charts
- Log-scaled axes for visualizing highly skewed data
- Unpacking nested/multi-value column data with `.split()` and `.stack()`
- Comparative business analysis (free vs. paid, category-level revenue potential, pricing strategy)

## 🚀 Run It

```bash
pip install pandas plotly jupyter
jupyter notebook app_analytics.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
