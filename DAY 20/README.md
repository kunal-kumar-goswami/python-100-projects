<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2020/day20-banner.png" alt="Day 20 — Snake Game banner" width="100%" />
</p>

# Day 20 — 🐍 Snake Game

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A full, object-oriented Snake game — the classic arcade game built with the `turtle` module, split cleanly across four classes: the snake, the food, the scoreboard, and the main game loop.

## 💡 What it does

A green snake moves continuously around a black game screen, controlled with the arrow keys. Eating the red food makes the snake grow by one segment and increases the score. The game resets (score, snake, and food) if the snake hits the screen border or collides with its own body, and the high score persists across resets within the same session.

## 🧱 Class Overview

- **`Snake`** — manages the snake's segments, movement, growth, direction changes, and reset
- **`Food`** — a single turtle that repositions itself randomly on the screen each time it's eaten
- **`Scoreboard`** — displays the current score and high score, and shows a Game Over message
- **`main.py`** — sets up the screen, wires up keyboard controls, and runs the game loop (move → check food collision → check wall/self collision)

## 🎯 Concepts Practiced

- Object-Oriented Programming — 3 cooperating classes, each managing its own state
- `screen.onkey()` for arrow-key controls, with heading checks to prevent 180° reversals
- List manipulation for growing the snake and moving each segment to follow the one ahead of it
- Distance-based collision detection (`turtle.distance()`) for both food and self-collision
- A `while` loop game cycle combined with `screen.tracer()` and `time.sleep()` for smooth, controlled animation

## 🔑 Key Takeaways

- Preventing the snake from reversing directly into itself (`if self.head.heading() != 270: setheading(90)`) is what stops an instant, unfair collision when pressing the opposite direction key
- Moving the snake by updating each segment to the position of the one in front of it — working backwards through the list — is what creates the classic "following" movement without needing to store a movement history
- `turtle.distance()` is a simple, effective way to detect both "did the snake eat the food" and "did the snake hit itself," just with different threshold distances
- Separating the scoreboard's display logic from the snake's movement logic means the score can be updated independently without the snake class needing to know anything about scoring

## 🛠️ Tech Stack

`Python 3` · `turtle` module

## 📁 Files

```
day20/
├── main.py       # Game loop — run this
├── snake.py      # Snake class
├── food.py       # Food class
├── score.py      # Scoreboard class
├── banner.png
└── README.md
```

## 🏃 How to Run

```bash
git clone https://github.com/kunal-kumar-goswami/python-100-projects.git
cd 100-days-of-python/day20
python main.py
```

No external libraries required.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
