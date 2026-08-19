# Day 13 — 🐞 Debugging Practice

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/100_days_of_python) journey — Angela Yu's Python Pro Bootcamp

A set of classic debugging exercises — fixing broken logic in an odd/even checker, a leap year checker, and a FizzBuzz implementation. Day 13 has no standalone project; it's entirely focused on reading, testing, and fixing existing code.

## 📂 Exercises

### 1️⃣ Odd or Even Checker
A function that checks whether a number is odd or even using the modulo operator and returns a descriptive message.

**Concepts:** Functions, modulo operator, return values

### 2️⃣ Leap Year Checker
Determines whether a given year is a leap year using nested conditionals to apply the divisible-by-4, divisible-by-100, and divisible-by-400 rules.

**Concepts:** Nested `if`/`else` statements, modulo operator, boolean return values

### 3️⃣ FizzBuzz
Loops from 1 to a given target number, printing "FizzBuzz" for multiples of both 3 and 5, "Fizz" for multiples of 3, "Buzz" for multiples of 5, and the number itself otherwise.

**Concepts:** `for` loops, `range()`, modulo operator, combined conditionals with `and`

## 🎯 Key Takeaways

- Debugging is largely about tracing what a function actually does step by step, rather than what it was intended to do
- The combined condition (divisible by both 3 and 5) must be checked before the individual `elif` branches, otherwise it never gets reached
- The leap year rule needs three nested checks in the right order — divisible by 4, then not by 100 unless also by 400 — getting the order wrong silently breaks edge cases like the year 2000
- Testing a function against known edge cases (e.g. a century year for leap year, or a multiple of 15 for FizzBuzz) is the fastest way to catch a logic bug

## 🛠️ Tech Stack

`Python 3`

---

