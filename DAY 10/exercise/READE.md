# Day 10 — 📝 Exercises

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

Exercises practicing functions with default/keyword arguments, docstrings, function composition, nested conditionals, and basic input validation.

## 📂 Exercises

### 1️⃣ Name Formatter (Basics)
A function that takes a first and last name and returns them in title case, with a docstring explaining what the function does.

**Concepts:** Functions with parameters, `.title()`, docstrings, return values

### 2️⃣ Keyword Arguments & Function Composition
Calling the name formatter using keyword arguments instead of positional ones, then chaining two smaller functions together — one that duplicates text and one that title-cases it — by passing the output of one directly into the other.

**Concepts:** Keyword arguments, function composition (nesting function calls), `len()`

### 3️⃣ Leap Year Checker
Determines whether a given year is a leap year using nested conditionals to apply the divisible-by-4, divisible-by-100, and divisible-by-400 rules.

**Concepts:** Nested `if`/`else` statements, modulo operator, boolean return values

### 4️⃣ Name Formatter with Input Validation
Extends the name formatter to take live user input and check for empty fields before formatting, returning an error message if either name is missing.

**Concepts:** Input validation, `input()`, conditional early return, function composition

## 🎯 Key Takeaways

- A docstring (`""" ... """` right after the function definition) documents what a function does, which is useful once a project has many functions
- Keyword arguments (`formate_name(f_name="...", l_name="...")`) make a function call more explicit and order-independent
- Functions can be composed by passing one function's return value directly as another function's argument — e.g. `operator_01(operator_02(text))`
- The leap year rule needs three nested checks (divisible by 4, then not by 100 unless also by 400) — nested conditionals map directly onto multi-step rules like this
- Validating input early (checking for empty strings before processing) prevents a function from producing a confusing or broken result

## 🛠️ Tech Stack

`Python 3`

---

