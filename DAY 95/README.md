<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2095/day95banner.png" alt="Day 95 - Game Development Banner" width="100%">
</p>

# Day 95 - Professional Portfolio: Game Development — Space Invaders 👾🚀

A full arcade-style Space Invaders clone built with `pygame` — complete with a scrolling starfield, animated enemy sprites, destructible barriers, a bonus UFO, particle explosions, persistent high scores, and a title/pause/game-over flow, all running in a single self-contained script.

## 🗂️ Project Structure

```
DAY 95/
├── space_invaders.py
└── high_score.txt   (auto-created on first run)
```

## ⚙️ How It Works

- **Class-based architecture:** the game is organized into clear entity classes — `Player`, `Enemy`, `Bullet`, `Barrier`, `UFO`, `Particle`, and `Star` — each owning its own `update()` and `draw()` methods, coordinated by a central `Game` class that owns all game state and the main loop logic.
- **Enemy formation movement:** `Game.update()` recreates the classic side-step-and-drop pattern — the whole enemy grid steps sideways at an interval tied to `enemy_speed`, and reverses direction and drops down a row whenever any alive enemy touches the screen edge.
- **Difficulty scaling:** `enemy_speed` increases with `self.level` on every `spawn_enemies()` call, and `shoot_interval` shrinks as level increases, so both enemy movement and enemy fire rate ramp up as the player survives longer.
- **Destructible barriers:** `Barrier` stores its shape as a set of `(col, row)` block coordinates built from an ASCII art template; `hit()` finds the struck block and removes a 3×3 cluster around it for a chunky "chip damage" effect whenever a bullet collides with it.
- **Collision handling:** `handle_collisions()` checks player bullets against enemies, the UFO, and barriers in priority order, and enemy bullets against barriers and the player, removing bullets and awarding score/lives changes as needed — each hit also spawns a `Particle` burst via `spawn_explosion()`.
- **Persistent high score:** `load_high_score()`/`save_high_score()` read and write a plain `high_score.txt` file next to the script, so the best score survives between runs.
- **Game flow:** `title_screen()` runs its own mini event loop before `main()` starts the real game loop; state transitions between `"playing"`, `"paused"`, and `"gameover"` are handled centrally in `Game.state`, with `draw_center_text()` rendering the paused/game-over overlays.

## 🐛 Notes on the current code

- **Enemies never fire more than one bullet type:** `enemy_shoot_timer` picks a single random alive enemy to fire each interval, but there's no cap on simultaneous enemy bullets on screen, so at high levels with a fast `shoot_interval` the bullet list could grow largely unbounded between screen-clears.
- **Barrier collision is checked before player collision:** in `handle_collisions()`, enemy bullets are tested against barriers first and only checked against the player if they didn't hit a barrier — correct for gameplay, but the `break` inside the barrier loop means a bullet only ever damages the first barrier it overlaps, even if it geometrically overlaps two at once.
- **`pygame.mixer.init()` is called but never used:** the mixer is initialized at the top of the file, but no sound effects or music are loaded or played anywhere in the game — likely a placeholder for a planned audio pass.
- **Unused `win_forever` state:** `Game.draw()` has a branch for a `"win_forever"` state that's never actually set anywhere else in the code — dead code left over from an earlier design idea (e.g. an infinite-level "win" condition).
- **No delta-time movement:** all movement and timers are frame-based (tied to the fixed `FPS = 60` via `clock.tick(FPS)`) rather than using delta-time, so gameplay speed would change if run on a system that can't sustain 60 FPS.

## 🧠 Concepts Practiced

- Building a complete game loop with `pygame` (event handling, update, draw, `clock.tick()`)
- Object-oriented game architecture with multiple interacting entity classes
- Rect-based collision detection between bullets, enemies, barriers, and the player
- Procedural sprite drawing with primitive shapes (no external image assets)
- Simple particle effects for explosions
- Game state management (title screen, playing, paused, game over)
- Persisting data between runs with basic file I/O (high score tracking)
- Progressive difficulty scaling tied to player progress

## 🚀 Run It

```bash
pip install pygame
python space_invaders.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
