# Day 08 — 📝 Exercises

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

Exercises practicing functions with parameters and return values, using letter counting and simple arithmetic to produce a calculated result.

## 📂 Exercises

### 1️⃣ Life in Weeks
A function that takes a person's current age and calculates roughly how many weeks they have left, assuming a lifespan of 90 years.

**Concepts:** Functions with parameters, arithmetic operations, f-strings

### 2️⃣ Love Calculator
A function that takes two names, combines and lowercases them, then counts the occurrences of the letters in "TRUE" and "LOVE" to generate a two-digit love score — a playful twist on letter counting and string manipulation, inspired by the "FLAMES" game.

**Concepts:** Functions with multiple parameters, `.lower()`, `.count()`, string-to-int conversion

## 🎯 Key Takeaways

- A function's parameters let the same logic run for any input, instead of hardcoding a single value
- `.count()` is a quick way to tally how many times a character appears in a string, without writing a manual loop
- Combining two counted digits into one score (`int(str(a) + str(b))`) is a simple trick for merging two separate numbers into a single two-digit result
- Renaming variables that would otherwise collide (like two different `e` counts) keeps the code readable and avoids silent bugs

## 🛠️ Tech Stack

`Python 3`

---
