<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2074/day74banner.png" alt="Day 74 - LEGO Dataset Analysis Banner" width="100%">
</p>

# Day 74 - Aggregate & Merge Data with Pandas: LEGO Dataset 🧱📊

A deep exploration of a real-world LEGO dataset (from Rebrickable) — investigating LEGO's history, product growth, theme popularity, and how set complexity has changed over time, using `.groupby()`, `.agg()`, and DataFrame merging.

## 🗂️ Project Structure

```
DAY 74/
├── lego_analysis.ipynb
├── assets/
│   ├── bricks.jpg
│   ├── lego_sets.png
│   └── lego_themes.png
│   └── rebrickable_schema.png
├── data/
│   ├── colors.csv
│   ├── sets.csv
│   └── themes.csv
└── README.md
```

## ⚙️ Questions Explored

- What's the most enormous LEGO set ever created, and how many parts did it have?
- How did LEGO start out — what year did they launch, and how many sets did they sell initially?
- Which LEGO theme has the most individual sets — an in-house theme or a licensed one (Star Wars, Harry Potter, Marvel)?
- When did LEGO's product offering really expand, based on themes/sets released year-on-year?
- Have LEGO sets grown in size/complexity over time (more parts per set)?

## ⚙️ What's Inside the Notebook

### Data Exploration
- Loads `colors.csv`, finds the number of unique colors LEGO produces via `.nunique()`, and compares transparent vs. opaque color counts two different ways (`.groupby().count()` and `.value_counts()`).
- Loads `sets.csv`, inspects first/last rows, and finds the earliest LEGO sets by sorting on `year`.
- Filters for the company's very first year (1949) to see how many sets launched.
- Finds the top 5 largest sets by part count (`sort_values('num_parts', ascending=False)`).

### Aggregation & Trends Over Time
- Uses `.groupby('year').count()` to track how many sets were released each year, comparing early years (1955) to recent ones (2019), and plots this as a line chart — slicing off the last two incomplete years of data.
- Uses `.groupby('year').agg({'theme_id': pd.Series.nunique})` to count *unique* themes released per year (not just total sets), renaming the resulting column for clarity.
- Plots sets-per-year and themes-per-year on **two separate y-axes sharing the same x-axis** (`ax1.twinx()`), since their scales differ — styled with distinct colors per axis for readability.
- Uses `.groupby('year').agg({'num_parts': pd.Series.mean})` to compute the average number of parts per set by year, then visualizes this as a **scatter plot** to spot the trend of increasing set complexity over time.

### Merging DataFrames
- Counts sets per `theme_id` with `.value_counts()`, converts the result into a proper DataFrame, then **merges** it with `themes.csv` on the shared `id` column to attach human-readable theme names to the counts — a classic foreign-key join.
- Visualizes the top 10 most prolific themes as a bar chart, refining it from a rough first pass into a properly labeled, resized, and rotated-label chart.

## 🧠 Concepts Practiced

- Counting unique values (`.nunique()`) and value distributions (`.value_counts()`)
- Filtering and sorting DataFrames to answer specific questions
- `.groupby()` combined with `.agg()` for custom aggregations (not just default sum/count)
- Dual-axis line charts for comparing two differently-scaled trends
- Scatter plots for spotting trends over time
- Merging DataFrames on a shared key (foreign-key-style joins), mirroring real relational database schemas
- Iteratively improving a chart from a rough first draft to a properly styled, readable visualization

## 🚀 Run It

```bash
pip install pandas matplotlib jupyter
jupyter notebook lego_analysis.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
