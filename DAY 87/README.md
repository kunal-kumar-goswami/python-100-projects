<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2087/day87banner.png" alt="Day 87 - Breakout Game Banner" width="100%">
</p>

# Day 87 - Professional Portfolio: Game — Breakout 🧱🕹️

A classic Breakout clone built with Python's `turtle` module, cleanly split across multiple files for the paddle, ball, brick wall, and scoreboard — with lives, score tracking, and a proper win/lose condition.

## 🗂️ Project Structure

```
DAY 87/
├── main.py
├── paddle.py
├── ball.py
├── wall.py
└── scoreboard.py
```

## ⚙️ How It Works

- **Screen setup:** an 800×600 black-background window with `tracer(0)` for manual frame control, giving smooth animation via the main game loop.
- **Game objects:** `Scoreboard`, `Paddle`, `Ball`, and `Wall` (which builds and holds the grid of brick objects) are each their own class in a separate module.
- **Controls:** left/right arrow keys move the paddle via `screen.onkey()`.
- **Main game loop:** each frame, the ball moves, then checks for:
  - **Wall bounces:** off the left/right screen edges and the top wall.
  - **Paddle bounces:** using a distance check (`ball.distance(paddle) < PADDLE_HIT_DISTANCE`) combined with a y-position check, so the ball only bounces when genuinely near the paddle at the right height.
  - **Brick collisions:** loops over a **copy** of the brick list (`all_bricks[:]`) so bricks can be safely removed mid-iteration — hiding the hit brick, removing it from the list, bouncing the ball, and awarding a point.
  - **Win condition:** if `all_bricks` becomes empty, the game ends in a win.
  - **Lost ball:** if the ball falls below `OUT_OF_BOUNDS_Y`, it resets to the starting position and a life is lost.
  - **Lose condition:** if `lives` reaches 0, the game ends.

## 🧠 Concepts Practiced

- Multi-file OOP project structure (separating paddle, ball, wall, and scoreboard into their own classes)
- Manual screen refresh with `tracer(0)` + `screen.update()` for a controlled game loop
- Distance-based collision detection
- Safe iteration and removal from a list during a loop (iterating over a copy)
- Win/lose condition tracking via game state (`lives`, remaining bricks)
- Named constants for screen boundaries and collision thresholds, improving readability over "magic numbers"

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
