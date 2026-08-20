<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2025/day25banner.png" alt="Day 25 - Pandas & CSV Banner" width="100%">
</p>

# Day 25  — Working with CSV Data & Pandas 🐼

Three separate mini-projects exploring `pandas` for reading, filtering, and aggregating real-world CSV datasets.

## 🗂️ Project Structure

```
DAY 25/
├── us_state_game/
│   ├── main.py
│   ├── 50_states.csv
│   └── states.gif
├── central_park_squirrel_census/
│   ├── main.py
│   └── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
├── weather_data/
│   ├── main.py
│   └── weather_data.csv
└── README.md
```

---

## 1️⃣ U.S. States Game 🗺️

An interactive `turtle`-based quiz game. It loads all 50 state names and coordinates from `50_states.csv` and lets the player type state names one at a time.

- Correctly guessed states are written onto a blank US map outline at their proper `(x, y)` coordinates.
- Typing `Exit` ends the game early and exports any states the player missed to `state_you_missed.csv` using a `DataFrame`.
- On completing all 50 (or exiting), a summary screen shows the final score.

**Concepts:** `pandas.read_csv`, `DataFrame` column access (`.state.to_list()`), row filtering (`states_data[states_data.state == answer_state]`), exporting a `DataFrame` back to CSV, combining `turtle` graphics with data lookups.

---

## 2️⃣ Central Park Squirrel Census 🐿️

Analyzes the 2018 Central Park Squirrel Census dataset to count squirrels by fur color.

- Filters the dataset for `"Primary Fur Color"` equal to `"Gray"`, `"Cinnamon"`, and `"Black"`, counting each with `len()`.
- Builds a summary dictionary of color → count and converts it into a new `DataFrame`.
- Exports the result to `squirrel_count.csv`.

**Concepts:** Boolean filtering on a column, `len()` on a filtered `DataFrame`, building a `DataFrame` from a dictionary, `to_csv()` export.

---

## 3️⃣ Weather Data ☀️

Explores basic statistics on a weather dataset.

- Reads `weather_data.csv` and inspects the data types of the `DataFrame` and a single column.
- Converts the data to a dictionary (`to_dict()`) and to a list (`to_list()`) for the `temp` column.
- Calculates the average temperature manually (`sum()/len()`) and compares it with pandas' built-in `.mean()` and `.max()`.
- Filters rows by condition, e.g. pulling out the row where `day == "Monday"`.

**Concepts:** `DataFrame` → `dict`/`list` conversions, aggregate functions (`.mean()`, `.max()`), row filtering by condition.

---

## 🧠 Concepts Practiced (Overall)

- Reading CSVs into `DataFrame`s with `pandas.read_csv`
- Column selection and conversion to Python lists/dicts
- Boolean filtering and conditional row selection
- Aggregations (`sum`, `mean`, `max`, `len`)
- Building new `DataFrame`s and exporting to CSV
- Combining `pandas` with other libraries (`turtle`) in a real project

## 🚀 Run It

```bash
# US States Game
python us_state_game/main.py

# Squirrel Census
python central_park_squirrel_census/main.py

# Weather Data
python weather_data/main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
