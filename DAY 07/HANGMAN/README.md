# Day 07 — 🎯 Hangman

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

A classic Hangman game built up in stages — starting from checking a single guessed letter, through to a fully playable game with a life counter and ASCII art that updates as the player makes mistakes.

## 💡 What it does

The program picks a random word from a word bank, displays it as a row of blanks, and lets the player guess one letter at a time. Correct guesses reveal their position in the word; wrong guesses cost a life and update the hangman ASCII art. The game ends when the word is fully guessed (win) or all 6 lives run out (lose).

**Example:**
```
**************************** 6/6 LIVES LEFT ****************************
Guess a letter: a
Word to guess: a_____a__

**************************** 6/6 LIVES LEFT ****************************
Guess a letter: z
You guessed z, that's not in the word. You lose a life.
Word to guess: a_____a__

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
```

## 🧱 Build Process

This project was built incrementally across 5 stages:

1. **Random word + single letter check** — pick a random word and check if one guessed letter matches
2. **Blanks + reveal** — display the word as underscores and reveal a guessed letter in its correct position
3. **Repeated guessing** — wrap guessing in a `while` loop so the player can keep guessing until the word is complete
4. **Lives + ASCII art** — add a life counter and hangman ASCII art that updates as lives are lost
5. **Final polish** — split the word list and ASCII art into separate files, add duplicate-guess detection, and a live lives counter

## 🎯 Concepts Practiced

- `while` loops for repeated guessing
- Lists and `random.choice()`
- String building with a loop (`placeholder`/`display`)
- Importing variables from separate `.py` files (modularizing code)
- Tracking game state across loop iterations (`lives`, `correct_letters`, `game_over`)

## 🔑 Key Takeaways

- Splitting a large project into separate files (`main.py`, `hangman_words.py`, `hangman_art.py`) keeps the game logic readable and separates data from behavior
- Rebuilding the `display` string from scratch every guess — checking each letter against both the new guess and all previously correct letters — is simpler and less error-prone than trying to update it in place
- A `while not game_over` loop combined with a boolean flag is a clean way to control a game loop with multiple possible end conditions (win or lose)
- Tracking guessed letters in a list prevents the same letter from being penalized twice

## 🛠️ Tech Stack

`Python 3` · `random` module

