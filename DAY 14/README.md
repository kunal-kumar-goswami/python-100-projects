<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2014/day14-banner.png" alt="Day 12 — Number Guessing Game banner" width="100%" />
</p>


# Day 14 — 📈 Higher Lower Game

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A command-line "Higher Lower" game where the player compares two Instagram-style accounts and guesses which one has more followers — keeping score until they get one wrong.

## 💡 What it does

The program shows two randomly picked accounts (with a description and country) and asks the player to guess which one (1 or 2) has more followers. Correct guesses increase the score and the game continues with a new account; a wrong guess ends the game and shows the final score. Input is validated so only '1' or '2' is accepted.

**Example:**
```
Compare 1: John Doe, a fitness influencer, from USA.
[vs art]
Against 2: Jane Smith, a travel blogger, from Canada.
Who has more followers? Type '1' or '2': 1

***** You are Right! Your score is 1. *****
```

## 🎯 Concepts Practiced

- Functions with parameters and return values
- `random.choice()` for picking accounts, with a check to avoid repeating the same one twice in a row
- A `while` loop for input validation (only accepting '1' or '2')
- Formatting dictionary data into a readable string
- Splitting a project across multiple files (`main.py`, `art.py`, `data.py`)

## 🔑 Key Takeaways

- Keeping the account data in its own `data.py` file separates content from game logic, making it easy to add more accounts later without touching the game code
- Comparing `account_1 == account_2` after picking a new random account is a simple way to guarantee two different accounts are shown each round
- Centralizing the win condition in `check_answer()` keeps the comparison logic (who has more followers) separate from the game loop that manages score and continuation
- A dedicated validation loop (`while not valid_input`) is a reusable pattern for making sure user input matches one of a fixed set of accepted values before moving on

## 🛠️ Tech Stack

`Python 3` · `random` module


