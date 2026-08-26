<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2081/day81banner.png" alt="Day 81 - Predict House Prices Banner" width="100%">
</p>

# Day 81 - Capstone Project: Predict House Prices 🏠💵

A full end-to-end machine learning capstone: building a multivariable linear regression model on the classic Boston housing dataset to estimate residential property values based on 13 real-world features, including a data-transformation step to meaningfully improve model fit.

## 🗂️ Project Structure

```
DAY 81/
├── multivariable_regression_and_valuation_model.ipynb
├── boston.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration & Cleaning
- Loads the 506-row Boston housing dataset (13 features + `PRICE` target), checks shape, NaNs, and duplicates — none found.
- Computes descriptive statistics: average pupil-teacher ratio, average home price, and understanding `CHAS` as a binary "next to Charles River" dummy variable.

### Visualizing Features
- **Seaborn `.displot()`** with KDE overlay for `PRICE`, `DIS` (commute distance), and `RM` (rooms) — spotting a suspicious spike of homes capped at $50,000, likely a data collection artifact.
- **Matplotlib histogram** for `RAD` (highway accessibility index).
- **Plotly bar chart** showing only 35 of 506 homes are located next to the Charles River.

### Exploring Relationships
- **Seaborn `.pairplot()`** across all features at once, for a full-grid overview of correlations.
- **Targeted `.jointplot()`s** investigating specific relationships: distance vs. pollution (NOX drops with distance), industry vs. pollution, poverty (LSTAT) vs. room count, poverty vs. price, and rooms vs. price.

### Building the Model
- Splits data 80/20 into train/test sets with `train_test_split()` (`random_state=10` for reproducibility).
- Fits a **multivariable `LinearRegression()`** using all 13 features, achieving an initial training R² of **0.75**.
- Extracts and interprets the model's coefficients (e.g. calculating the exact dollar "premium" of an extra room), checking that each coefficient's sign matches real-world intuition.
- **Residual analysis:** plots actual vs. predicted prices, and residuals vs. predicted values, to check for systematic bias. Finds the residuals have a skew of 1.46 — room for improvement.

### Improving the Model with a Log Transformation
- Investigates whether a **log transformation** of `PRICE` reduces skew (it does — from a positively-skewed raw distribution to something much closer to normal).
- Re-runs the entire regression using `log(PRICE)` as the target, achieving an improved training R² of **0.79**.
- Re-examines coefficients under the new model (e.g. confirming river proximity remains a positive factor, and higher pupil-teacher ratio remains a clear negative).
- Repeats the residual analysis — the log-price model's residual skew drops dramatically to **0.09**, much closer to a normal distribution than the original model.

### Out-of-Sample Testing & Prediction
- Compares both models' R² on the **held-out test set** (never seen during training) — confirming the log-price model still performs well, validating it's not just overfit to training data.
- **Makes real predictions:** first for a home with average characteristics (~$20,700), then for a custom property (8 rooms, next to the river, low pollution, low poverty, short commute) by adjusting `property_stats` and reversing the log transform with `np.exp()` to get a dollar estimate.

## 🧠 Concepts Practiced

- Full ML workflow: explore → clean → visualize → split → train → evaluate → improve → predict
- Multivariable linear regression with `scikit-learn`
- Interpreting regression coefficients in real-world terms
- Residual analysis for diagnosing model bias (skew, mean)
- Data transformation (log) to improve linear model fit
- Train/test splitting and out-of-sample validation
- Using a fitted model to generate real-world predictions on custom input

## 🚀 Run It

```bash
pip install pandas numpy seaborn plotly matplotlib scikit-learn jupyter
jupyter notebook multivariable_regression_and_valuation_model.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
