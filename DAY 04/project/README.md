# Day 04 — ✊✋✌️ Rock, Paper, Scissors

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

 Rock, Paper, Scissors game where the player competes against a computer opponent that picks randomly.

## 💡 What it does

The player types a number (0 for Rock, 1 for Paper, 2 for Scissors), the computer randomly picks its own choice, and the program prints ASCII art for both choices before declaring the winner.

**Example:**
```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors
0/1/2: 0
You chose: Rock
The computer chose: Paper
You lose, Paper wins against rock.
```

## 🎯 Concepts Practiced

- The `random` module (`random.randint()`) for computer decision-making
- Multi-line strings for ASCII art
- Input validation with `.isdigit()`
- Nested `if`/`elif`/`else` statements to compare two choices

## 🔑 Key Takeaways

- `.isdigit()` is a simple way to check that user input is a valid number before converting it with `int()`
- `random.randint(0, 2)` gives the computer a fair, unpredictable choice each round
- Comparing two choices (player vs. computer) needs a nested conditional for every possible matchup
- Validating input before using it prevents the program from crashing on unexpected values

## 🛠️ Tech Stack

`Python 3` · `random` module

---