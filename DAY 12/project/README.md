# Day 12 — 🎯 Number Guessing Game

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A number guessing game where the player has a limited number of attempts — set by difficulty level — to guess a randomly generated number between 1 and 100.

## 💡 What it does

The program picks a random number and asks the player to choose "easy" (10 attempts) or "hard" (5 attempts). On each guess, it tells the player whether their guess was too high or too low, invalid input is caught without ending the game, and the game ends when the player guesses correctly or runs out of attempts.

**Example:**
```
[ ________                                _______               ___.                 
 /  _____/ __ __   ____   ______ ______   \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/           \/            \/    \/     \/       
        ]
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a level. Type 'easy' or 'hard': easy

You have 10 attempts remaining.
Guess a number between 1 and 100: 50
Too low.

You have 9 attempts remaining.
Guess a number between 1 and 100: 75
Correct! You guessed it right 👍. The number was 75.
```

## 🎯 Concepts Practiced

- Functions with parameters and return values
- `random.randint()` for generating the target number
- `while` loops for repeated guessing with a turn limit
- `try`/`except` for input validation
- Constants (`EASY_LEVEL_TURNS`, `HARD_LEVEL_TURN`) for readable, adjustable difficulty settings

## 🔑 Key Takeaways

- Naming difficulty settings as constants (`EASY_LEVEL_TURNS = 10`) makes the game easier to tune later than hardcoding the numbers inline
- Separating concerns into functions — `difficulty_level()`, `check_answer()`, `game()` — keeps each piece of logic focused and easy to follow
- Wrapping the guess input in `try`/`except ValueError` lets the game recover from non-numeric input instead of crashing
- Using `turns -= 1` inside a `while turns > 0` loop naturally ends the game once attempts run out, without needing a separate "game over" flag

## 🛠️ Tech Stack

`Python 3` · `random` module

