<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2078/day78banner.png" alt="Day 78 - Seaborn and Linear Regression Banner" width="100%">
</p>

# Day 78 - Linear Regression & Data Visualisation with Seaborn 🎬📈

Investigating whether higher film budgets lead to higher box office revenue, using real movie financial data scraped from the-numbers.com — combining `Seaborn` visualization with an actual `scikit-learn` linear regression model.

## 🗂️ Project Structure

```
DAY 78/
├── seaborn_and_linear_regression.ipynb
├── cost_revenue_dirty.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration & Cleaning
- Inspects shape, samples, NaNs, duplicates, and column data types.
- Converts `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` from formatted currency strings (with `$` and `,`) into proper numeric types.
- Converts `Release_Date` to a `datetime` column.

### Descriptive Statistics
- Finds average production budget and worldwide gross, minimum revenue figures, and the highest-budget/highest-grossing films.
- Investigates the cheapest and most expensive films in the dataset directly.

### Investigating Zero-Revenue & Special Cases
- Finds films that grossed $0 domestically and $0 worldwide, sorted by budget to spot high-budget flops or data anomalies.
- Filters for **international-only releases** (zero U.S. revenue but nonzero worldwide revenue) two ways: boolean indexing (`.loc[]`) and the more readable `.query()` method.
- Identifies and **excludes unreleased films** (release date after the May 2018 scrape date) to build a clean `data_clean` DataFrame.
- Calculates what percentage of films lost money (production budget exceeded worldwide gross).

### Seaborn Visualization
- **Bubble charts:** budget vs. worldwide gross as a scatter plot, progressively enhanced with color/size mapping tied to revenue, and styled with Seaborn's `darkgrid` theme.
- **Time-based bubble chart:** release date vs. production budget, colored/sized by worldwide gross, to see how budgets have trended over the decades.
- **Decade extraction trick:** converts release year to decade using floor division (`year // 10 * 10`), adding a `Decade` column — then splits the dataset into `old_films` (≤1969) and `new_films` (1970 onward) for separate analysis.
- **Regression plots (`sns.regplot()`):** overlays a fitted linear regression line directly on the scatter plot for both old and new films, with custom styling (HEX colors, alpha transparency, axis limits/labels) to compare how well a straight-line model fits each era.

### Running an Actual Linear Regression (scikit-learn)
- Fits a `LinearRegression()` model on `new_films`, treating production budget as the explanatory variable and worldwide gross as the target.
- Extracts the model's intercept (θ₀), slope coefficient (θ₁), and R² score (how much of the variance in revenue the model explains).
- Repeats the same regression for `old_films` to compare model fit across eras.
- **Makes a prediction:** manually computes the estimated worldwide revenue for a hypothetical $350 million budget film using the fitted model's equation.

## 🧠 Concepts Practiced

- End-to-end data cleaning: currency parsing, date conversion, duplicate/NaN detection
- Multi-condition filtering with both boolean indexing and `.query()`
- Feature engineering (decade bucketing via floor division)
- Statistical visualization with `Seaborn` (scatter/bubble charts, regression plots)
- Fitting and interpreting a real linear regression model with `scikit-learn`
- Using a fitted model to make predictions on new input values
- Comparing model fit across different data subsets (old vs. new films)

## 🚀 Run It

```bash
pip install pandas matplotlib seaborn scikit-learn jupyter
jupyter notebook seaborn_and_linear_regression.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
