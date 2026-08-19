<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2011/day11-banner.png" alt="Day 10 — Calculator banner" width="100%" />
</p>


# Day 11 — 🃏 Blackjack Capstone

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A command-line Blackjack game against a computer dealer, with Ace handling, Blackjack detection, and a replayable game loop.

## 💡 What it does

The program deals two cards each to the player and the computer. The player can keep hitting or stand; once they stop, the computer draws until it reaches at least 17. Scores are calculated with automatic Ace adjustment (11 → 1 when needed to avoid busting), and the winner is determined by comparing final scores — including instant wins/losses for Blackjack.

**Example:**
```
Your cards: [10, 8], current score: 18
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 8], final score: 18
Computer's final hand: [6, 9, 5], final score: 20
You Lose 😢

Do you want to play a game of Blackjack? Type 'y' or 'n':
```

## 🎯 Concepts Practiced

- Functions with parameters and return values
- Lists for tracking each hand
- `while` loops for both the player's turn and the replay loop
- Conditional chains for comparing outcomes
- Importing the ASCII art logo from a separate `art.py` file

## 🔑 Key Takeaways

- Detecting Blackjack early (`sum(cards) == 21 and len(cards) == 2`) has to happen before any Ace adjustment, since a natural Blackjack is a special case with its own scoring rule
- Converting an Ace from 11 to 1 only when the hand would otherwise bust (`while 11 in cards and sum(cards) > 21`) mirrors how Blackjack actually treats Aces as flexible
- Centralizing the win/lose/draw logic in one `compare()` function keeps `play_game()` focused on the flow of the game rather than the rules for who wins
- Wrapping the whole game in an outer `while` loop driven by user input turns a single round into a replayable program

## 🛠️ Tech Stack

`Python 3` · `random` module


