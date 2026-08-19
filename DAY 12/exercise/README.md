# Day 12 — 📝 Exercises

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/100_days_of_python) journey — Angela Yu's Python Pro Bootcamp

Warm-up exercises practicing scope — block scope, global vs. local variables, namespaces — plus a prime number checker.

## 📂 Exercises

### 1️⃣ Prime Number Checker
A function that checks whether a given number is prime, using an early return for numbers ≤ 1, a shortcut for 2, an even-number check, and a loop that only tests odd divisors up to the square root of the number.

**Concepts:** Functions, early returns, the modulo operator, loop optimization with `range()` and `**0.5`

### 2️⃣ Global Variables
Demonstrates that a function can *read* a global variable directly, but reassigning the variable requires passing it in and returning the new value — since assignment inside a function creates a local variable instead of modifying the global one.

**Concepts:** Global scope, function parameters and return values

### 3️⃣ Block Scope
Shows that variables created inside an `if` block are still accessible outside the block within the same function — Python doesn't have block-level scope the way some other languages do.

**Concepts:** Block scope (or lack of it) inside `if` statements, functions

### 4️⃣ Namespaces & Scope
A closer look at local vs. global scope: a variable defined inside a function (`enemies = 2`) creates a separate local variable that doesn't affect the global one of the same name, while a function can freely *read* a global variable if it doesn't try to reassign it.

**Concepts:** Local scope, global scope, variable shadowing

## 🎯 Key Takeaways

- A function can read a global variable directly, but assigning to a variable of the same name inside the function creates a new **local** variable instead of modifying the global one
- Python doesn't enforce block-level scope inside `if`/`for`/`while` — a variable created inside a block is still visible for the rest of the enclosing function
- When a function needs to update a global value, the clearer pattern is to pass it in as a parameter and return the new value, rather than relying on the `global` keyword
- Optimizing a prime check by only testing odd numbers up to `√num` avoids unnecessary work compared to checking every number up to `num`

## 🛠️ Tech Stack

`Python 3`

---

