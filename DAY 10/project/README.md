# Day 10 — 🧮 Calculator

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

A calculator that supports addition, subtraction, multiplication, and division, and lets the user keep calculating with the running result or start a fresh calculation.

## 💡 What it does

The program prints an ASCII art logo, asks for a starting number, then repeatedly lets the user pick an operator, enter a second number, and see the result. The user can either continue calculating using the answer as the new starting number, or reset and start over from scratch.

**Example:**
```
[calculator logo]
What's the first number?: 10
+
-
*
/
Pick an operation: +
What's the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y
+
-
*
/
Pick an operation: *
What's the next number?: 2
15.0 * 2.0 = 30.0
```

## 🎯 Concepts Practiced

- Functions with parameters and return values (`add`, `subtract`, `multiply`, `divide`)
- A dictionary mapping operator symbols to their corresponding functions
- `dict.get()` for safely handling an invalid operator without crashing
- Recursion — restarting the calculator by calling `calculator()` from inside itself
- Importing and reusing ASCII art from a separate `art.py` file

## 🔑 Key Takeaways

- Mapping operator symbols to functions in a dictionary (`operators = {"+": add, ...}`) avoids a long `if`/`elif` chain and makes it easy to add new operators later
- `dict.get()` returns `None` for a missing key instead of raising an error, which makes it simple to catch and handle an invalid operator symbol gracefully
- Calling a function from inside itself (`calculator()` calling `calculator()`) is a simple way to "restart" a program's logic without needing an outer loop wrapping everything
- Splitting the ASCII art into its own `art.py` file keeps `calculator_project.py` focused purely on the calculator logic

## 🛠️ Tech Stack

`Python 3`
