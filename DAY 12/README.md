<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2012/day12-banner.png" alt="Day 12 — Number Guessing Game banner" width="100%" />
</p>

# Day 12 — Scope & the Number Guessing Game

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

Day twelve covers scope — global variables, block scope, and namespaces — plus a prime number checker, put into practice with a Number Guessing Game that adjusts difficulty by limiting the player's attempts.

## 📂 Contents

| Folder | Description |
|---|---|
| [`exercises/`](https://github.com/kunal-kumar-goswami/python-100-projects/tree/main/DAY%2012/exercise) | 4 warm-up exercises — prime number checker, global variables, block scope, namespaces & scope |
| [`project/`](https://github.com/kunal-kumar-goswami/python-100-projects/tree/main/DAY%2012/project) | 🎯 **Number Guessing Game** — guess a random number within a limited number of attempts, set by difficulty |

## 🎯 What I Learned

- A function can read a global variable, but assigning to it inside the function creates a separate local variable instead
- Python doesn't enforce block-level scope inside `if`/`for`/`while` — variables from a block remain visible in the rest of the function
- The pattern of passing a value in and returning a new one is a cleaner way to update global state than relying on the `global` keyword
- Optimizing a prime check by testing only odd divisors up to `√num`
- `try`/`except` for validating numeric input without crashing the program

## 🛠️ Tech Stack

`Python 3` · `random` module

---

➡️ [Exercises](https://github.com/kunal-kumar-goswami/python-100-projects/tree/main/DAY%2012/exercise) · [Project](https://github.com/kunal-kumar-goswami/python-100-projects/tree/main/DAY%2012/project) · [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
