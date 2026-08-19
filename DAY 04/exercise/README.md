# Day 04 — 📝 Exercises

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

Exercises completed before the Day 04 project (Rock, Paper, Scissors). These cover the `random` module and an introduction to lists.

## 📂 Exercises

### 1️⃣ The `random` Module
Exploring Python's built-in `random` module — generating a random whole number, a random decimal between 0 and 1, a random float within a custom range, and simulating a coin flip.

**Concepts:** `import`, `random.randint()`, `random.random()`, `random.uniform()`

### 2️⃣ Lists — Modifying, Appending & Extending
Working with a list of country names: updating an item by its index, adding a single new item with `.append()`, and adding multiple items at once with `.extend()`.

**Concepts:** Lists, indexing, `.append()`, `.extend()`

### 3️⃣ Picking a Random Item from a List
Comparing two different ways to select a random name from a list — using `random.choice()` directly, versus generating a random index with `random.randint()` and using it to access the list.

**Concepts:** `random.choice()`, list indexing, `random.randint()`

## 🎯 Key Takeaways

- A module must be imported before its functions can be used — `import random` unlocks tools like `randint()`, `random()`, `uniform()`, and `choice()`
- `random.randint(a, b)` includes both endpoints, while `random.random()` and `random.uniform()` generate decimals
- List items are changed by assigning to their index (`list[i] = value`); `.append()` adds one item to the end, `.extend()` adds multiple items at once
- `random.choice(list)` is a more direct way to pick a random item than generating a random index and indexing into the list manually

## 🛠️ Tech Stack

`Python 3` · `random` module

---

