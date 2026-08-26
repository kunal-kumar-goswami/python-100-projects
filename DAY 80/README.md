<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2080/day80banner.png" alt="Day 80 - Dr Semmelweis Handwashing Discovery Banner" width="100%">
</p>

# Day 80 - The Tragic Discovery of Handwashing: T-Test & Distributions 🧼🩺

Stepping into the shoes of Dr. Ignaz Semmelweis, using real 1840s Vienna General Hospital data to prove — statistically — that handwashing dramatically reduced deaths from childbed fever, culminating in a formal t-test of statistical significance.

## 🗂️ Project Structure

```
DAY 80/
├── Dr_semmelweis_handwashing_discovery.ipynb
├── annual_deaths_by_clinic.csv
├── monthly_deaths.csv
└── README.md
```

## ⚙️ What's Inside the Notebook

### Data Exploration
- Loads yearly and monthly death/birth data across two maternity clinics, checking shape, NaNs, and duplicates.
- Calculates the overall percentage of women who died in childbirth in 1840s Vienna, comparing it against the modern U.S. maternal death rate for context.

### Visualizing Births & Deaths Over Time
- **Dual-axis Matplotlib chart:** total monthly births vs. deaths, with proper year/month tick locators, gridlines, and distinct line styles/colors for each metric.
- **Plotly line charts:** yearly births and deaths split by clinic, comparing which clinic was busier and which had more deaths.
- Adds a `pct_deaths` column and compares the average death rate between Clinic 1 and Clinic 2 — revealing a significant disparity between the two.

### The Handwashing Intervention
- Marks June 1st, 1847 as the date handwashing became mandatory (with chlorinated water, not just plain water).
- Splits the monthly data into **before** and **after** subsets, calculating and comparing average death rates for each period.
- Computes a **6-month rolling average** of the death rate leading up to the policy change.
- **Combined Matplotlib chart:** overlays the pre-handwashing rate (thin dashed black), the rolling average (thick crimson dashed), and the post-handwashing rate (skyblue with markers) — visually showing the dramatic drop.
- Calculates the exact percentage-point reduction and the "times lower" improvement factor in death rate.

### Statistical Validation
- **Box plots (Plotly):** death rate distribution before vs. after handwashing, using `np.where()` to label each row.
- **Overlapping histograms (Plotly):** normalized (`histnorm='percent'`) so the differing time-period lengths are comparable, with a marginal box plot layered on top.
- **KDE plots (Seaborn):** smoothed distribution comparison before vs. after — including catching and fixing a real problem (the default KDE implies impossible negative death rates) by clipping the distribution to a valid `[0, 1]` range.
- **T-test (`scipy.stats.ttest_ind`):** formally tests whether the difference in average death rates before/after handwashing is statistically significant, computing both the t-statistic and p-value to determine confidence at the 99% level.

## 🧠 Concepts Practiced

- Historical data storytelling through visualization
- Dual-axis time-series charts with proper date-axis formatting
- Before/after intervention analysis
- Rolling averages for trend smoothing
- Multiple distribution visualization techniques: box plots, histograms, and KDE
- Recognizing and correcting a flawed default visualization (negative-value KDE)
- Formal hypothesis testing with a two-sample t-test to validate a real historical medical discovery

## 🚀 Run It

```bash
pip install pandas numpy plotly seaborn matplotlib scipy jupyter
jupyter notebook Dr_semmelweis_handwashing_discovery.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
