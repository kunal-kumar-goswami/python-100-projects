<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2023/day23banner.png" alt="Day 23 - Turtle Crossing Banner" width="100%">
</p>

# Day 23  — Turtle Crossing 🐢🚗

A **Frogger-style capstone project** built with Python's `turtle` module. The player must cross a road full of moving cars without getting hit — reaching the top resets the player and increases the difficulty level.

## 📌 Overview

- A player turtle moves upward across the screen.
- Cars spawn randomly and move from right to left, speeding up as the level increases.
- Colliding with a car ends the game.
- Successfully reaching the top of the screen levels up the game and resets the player's position.

## 🗂️ Project Structure

```
DAY 23/
├── main.py         # Game loop, screen setup, event listener
├── player.py       # Player class (movement, reset, collision distance)
├── car.py          # CarManager class (car creation, movement, level speed-up)
├── scoreboard.py   # Scoreboard class (level display, game over)
└── README.md
```

## 🎮 Controls

| Action      | Key  |
|-------------|------|
| Move Up     | `Up` |

## ⚙️ How It Works

- `Screen` is set up as a 600x600 light-blue canvas with `tracer(0)` for manual frame updates.
- Each loop iteration: cars are spawned (`create_car()`), moved (`move_cars()`), and the screen is redrawn.
- Collision is detected each frame by checking the `distance()` between the player and every car in `car_manager.cars`; if any distance is under `20`, it's game over.
- When the player's y-coordinate passes `290` (reaches the top), the player resets to the starting position, and both the `CarManager` (via `level_up()`) and `Scoreboard` (via `increase_level()`) advance to the next level, increasing car speed.

## 🧠 Concepts Practiced

- Object-Oriented Programming (separate classes per game entity)
- Managing a dynamic list of objects (`car_manager.cars`)
- Event-driven input handling (`onkey`)
- Manual screen refresh loops (`tracer(0)` + `screen.update()`)
- Collision detection using distance calculations
- Progressive difficulty / level scaling

## 🚀 Run It

```bash
python main.py
```

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
