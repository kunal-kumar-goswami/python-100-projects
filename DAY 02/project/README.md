# Day 02 — 🧮 Tip Calculator

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

Python program that splits a restaurant bill — tip included — evenly between any number of people.

## 💡 What it does

The program asks for the total bill amount, the tip percentage to leave, and the number of people splitting the bill. It then calculates exactly how much each person owes, rounded to two decimal places.

**Example:**
```
Welcome to the tip calculator!.🧮
What's your total bill? $150
What % of tip you will give ? 10 12 15: 12
How many people are you spliting the bill? 3
Each person should pay: $56.0
```

## 🎯 Concepts Practiced

- `input()` combined with `float()` and `int()` for type conversion
- Arithmetic operators for calculating percentages and splitting values
- `round()` to format currency to two decimal places
- f-strings for clean output formatting

## 🔑 Key Takeaways

- User input must be explicitly converted to `float` or `int` before it can be used in calculations — `input()` always returns a string
- A percentage tip can be applied directly with `bill * (1 + tip / 100)` instead of calculating and adding the tip separately
- `round(value, 2)` is the standard way to format money so it always shows two decimal places
- Chaining a few simple calculations (apply tip → split by people → round) is enough to solve a genuinely useful everyday problem

## 🛠️ Tech Stack

`Python 3`

---

