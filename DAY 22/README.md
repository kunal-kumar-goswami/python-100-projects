<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2022/day22banner.png" alt="Day 22 - Pong Game Banner" width="100%">
</p>

# Day 22 / 100 — Pong 🏓

A classic implementation of the arcade game **Pong**, built with Python's `turtle` module, split into clean, reusable modules using OOP principles.

## 📌 Overview

This project recreates the original Pong game:
- Two paddles controlled by separate players
- A ball that bounces off the top/bottom walls and paddles
- A live scoreboard
- Game ends when either player reaches **3 points**

## 🗂️ Project Structure

```
DAY 22/
├── main.py       # Game loop, screen setup, controls
├── paddle.py     # Paddle class (movement, position)
├── ball.py       # Ball class (movement, bouncing, speed, reset)
├── score.py      # Scoreboard class (score display, game over)
└── README.md
```

## 🎮 Controls

| Player      | Move Up | Move Down |
|-------------|---------|-----------|
| Left Paddle | `w`     | `s`       |
| Right Paddle| `Up`    | `Down`    |

## ⚙️ How It Works

- `Screen` is set up as an 800x600 black canvas with `tracer(0)` for manual, smooth frame updates.
- Two `Paddle` instances are created at the left (`-350, 0`) and right (`350, 0`) edges.
- A `Ball` instance moves each frame at `ball.mov_speed`, bouncing off the top/bottom edges of the screen.
- Collision with a paddle is detected using `distance()` combined with an x-coordinate boundary check, and triggers `bounce_x()`.
- If the ball passes a paddle (goes beyond `x = 380` or `x = -380`), it resets to the center and a point is awarded via the `Scoreboard`.
- The game loop ends once either score reaches `3`, calling `score.game_over()`.

## 🧠 Concepts Practiced

- Object-Oriented Programming (separate classes per game entity)
- Event-driven input handling (`onkeypress`)
- Manual screen refresh loops (`tracer(0)` + `screen.update()`)
- Collision detection using distance calculations
- Game state management (score tracking, game-over condition)

## 🚀 Run It

```bash
python main.py
```

---
⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
