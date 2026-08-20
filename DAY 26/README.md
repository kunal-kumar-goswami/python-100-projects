<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2026/day26banner.png" alt="Day 26 - NATO Alphabet Banner" width="100%">
</p>

# Day 26 / 100 — Dictionary Comprehension & NATO Alphabet 📡

Practicing dictionary comprehension through short exercises, then applying it in a NATO phonetic alphabet converter, plus a small standalone pandas `DataFrame` looping exercise.

## 🗂️ Project Structure

```
DAY 26/
├── exercise/
│   └── (squaring numbers, filtering evens, dict overlap, dict comprehension)
├── NATO alphabet project/
│   ├── main.py
│   └── nato_phonetic_alphabet.csv
├── panda_dataframe.py
└── README.md
```

---

## 1️⃣ Exercises 🧮

Short warm-up exercises practicing:
- Squaring numbers in a list using list comprehension
- Filtering even numbers from a list
- Finding overlap between two data collections
- Building dictionaries using dictionary comprehension

**Concepts:** List comprehension, dictionary comprehension, conditional filtering.

---

## 2️⃣ NATO Phonetic Alphabet Converter 🔤

Converts any word typed by the user into its NATO phonetic alphabet equivalent (e.g. `A → Alfa`, `B → Bravo`).

- Loads `nato_phonetic_alphabet.csv` into a `DataFrame` using `pandas.read_csv`.
- Builds a `letter → code` dictionary using **dictionary comprehension** combined with `DataFrame.iterrows()`.
- Takes user input, uppercases it, and looks up each letter's phonetic code via list comprehension.
- If the input contains a non-letter character, a `KeyError` is caught and the user is prompted to try again (recursively).

**Concepts:** `pandas.read_csv`, `DataFrame.iterrows()`, dictionary comprehension, list comprehension, exception handling (`try`/`except`), recursion for retry logic.

---

## 3️⃣ Pandas DataFrame Practice 🐼

A small standalone script exploring how to loop through rows of a `DataFrame`.

- Builds a `DataFrame` from a dictionary of student names and scores.
- Loops through rows with `iterrows()` and prints the score for the student named `"Angel"`.

**Concepts:** Creating a `DataFrame` from a dict, iterating over `DataFrame` rows, conditional row lookup.

## 🧠 Concepts Practiced (Overall)

- List & dictionary comprehension
- Iterating over `DataFrame` rows with `iterrows()`
- Building dictionaries from CSV data
- Exception handling with recursion for input validation

## 🚀 Run It

```bash
# NATO Alphabet Converter
python "NATO alphabet project/main.py"

# Pandas DataFrame practice
python panda_dataframe.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
