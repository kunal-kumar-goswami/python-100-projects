# Day 05 — 📝 Exercises

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

This  exercises completed before the Day 05 project (Password Generator). These cover `for` loops — iterating over lists, accumulating totals, using `range()`, and combining loops with conditionals.

## 📂 Exercises

### 1️⃣ Looping Through a List
A basic `for` loop that iterates over a list of names, printing each one and a personalized greeting.

**Concepts:** `for` loops, iterating over a list

### 2️⃣ Summing & Finding the Maximum
Calculating the total of a list of bill amounts two ways — with the built-in `sum()` function and by manually accumulating a total inside a loop — then finding the highest value both with the built-in `max()` function and by manually tracking the largest value seen so far.

**Concepts:** `sum()`, `max()`, accumulator pattern, comparison inside a loop

### 3️⃣ Looping with `range()`
Using `range()` to loop through a sequence of numbers, stepping through the range in increments, and accumulating a running total while printing it at each step.

**Concepts:** `range(start, stop)`, `range(start, stop, step)`, accumulator pattern

### 4️⃣ FizzBuzz
The classic FizzBuzz challenge — looping from 1 to 100 and printing "FizzBuzz" for multiples of both 3 and 5, "Fizz" for multiples of 3, "Bizz" for multiples of 5, and the number itself otherwise.

**Concepts:** `for` loops, modulo operator, combined conditionals with `and`

## 🎯 Key Takeaways

- A `for` loop can iterate directly over a list's items, without needing an index
- The same result (a sum or a maximum) can often be reached with a built-in function (`sum()`, `max()`) or manually with an accumulator — knowing both helps understand what the built-ins are doing internally
- `range(start, stop, step)` gives full control over which numbers a loop visits, not just a simple 1-by-1 count
- In a FizzBuzz-style problem, the combined condition (divisible by both 3 and 5) must be checked **before** the individual conditions, otherwise it gets caught by the first matching `elif` and never reached

## 🛠️ Tech Stack

`Python 3`

---
