# Day 09 — 📝 Exercises

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

Exercises practicing dictionaries — reading, adding, editing, and looping through key-value pairs, plus working with nested lists and nested dictionaries.

## 📂 Exercises

### 1️⃣ Grading Program
Takes a dictionary of student names and their scores, then builds a new dictionary mapping each student to a letter grade based on which score range they fall into.

**Concepts:** Dictionaries, iterating over dictionary keys, conditional logic, building a new dictionary from existing data

### 2️⃣ Dictionary Basics
Practicing the core dictionary operations: reading a value by key, adding a new key-value pair, creating an empty dictionary, editing an existing value, and looping through all keys and values.

**Concepts:** Dictionary creation, adding/editing entries, `for key in dictionary` loops

### 3️⃣ Nested Lists & Nested Dictionaries
Working with more complex data structures — indexing into a nested list, accessing values inside a dictionary of lists, and reading from a dictionary where each value is itself a dictionary.

**Concepts:** Nested lists, nested dictionaries, chained indexing/key access

## 🎯 Key Takeaways

- Looping over a dictionary with `for key in dictionary` gives access to each key, and `dictionary[key]` retrieves its value
- A second, empty dictionary can be built up inside a loop by assigning new key-value pairs one at a time (`new_dict[key] = value`)
- Chained range conditions (`91 <= score <= 100`) are a clean way to check whether a value falls within a specific bracket
- Separating the raw data (`student_scores`) from the derived data (`student_grades`) keeps the original dictionary untouched and the transformation logic clear
- Nested data structures (a list inside a list, a dictionary inside a dictionary) are accessed by chaining indexes/keys one level at a time, e.g. `travel["India"]["cities_visited"][2]`

## 🛠️ Tech Stack

`Python 3`

---
