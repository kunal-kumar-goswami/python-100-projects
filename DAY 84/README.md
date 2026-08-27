<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2084/day84banner.png" alt="Day 84 - Tic Tac Toe Banner" width="100%">
</p>

# Day 84 - Professional Portfolio: Python Scripting — Tic Tac Toe ⭕❌

A polished, dark-themed two-player Tic Tac Toe game built with `tkinter` — with hover states, win-highlighting, a persistent scoreboard, and a proper menu bar, going well beyond a bare-bones console version.

## 🗂️ Project Structure

```
DAY 84/
└── tic_tac_toe.py
└── README.md
```

## ⚙️ How It Works

- **Dark theme palette:** a full set of named color constants (`BG`, `CELL_BG`, `CELL_HOVER`, `BLUE` for X, `YELLOW` for O, `GREEN` for a win) applied consistently across the whole UI.
- **Board state:** a flat 9-element list (`board`) tracks each cell's mark, alongside `current_player`, `game_over`, and a `scores` dict tracking X wins, O wins, and ties.
- **`draw_mark(i, mark)`:** draws an X (two diagonal lines) or O (an oval) directly onto that cell's `Canvas` using `create_line()`/`create_oval()`, rather than using text characters.
- **`check_winner()`:** checks the board against all 8 winning combinations (`WIN_COMBOS`) and returns the matching triple of indices, or `None`.
- **`on_click(i)`:** the core game loop — ignores clicks on filled cells or after game over, places the current player's mark, checks for a win or a tie, and either ends the round or swaps turns.
- **`on_hover(i, entering)`:** highlights a cell on mouse-enter (only if it's empty and the game isn't over) and reverts on mouse-leave — a nice UX touch.
- **`end_game(winner, combo)`:** highlights the winning combo in green, updates the scoreboard label for the winner (or ties), and reveals a "play again" button.
- **`reset_board()` / `reset_scores()`:** separate reset functions — one for starting a new round (keeping scores), one for wiping the scoreboard entirely.
- **Menu bar:** a native `Menu` widget with "New Round," "Reset Scores," and "Quit" options, giving the game a proper desktop-app feel.

## 🧠 Concepts Practiced

- Building a complete, styled `tkinter` GUI (Canvas drawing, Frames, Labels, a Menu bar)
- Event binding for click and hover interactions (`<Button-1>`, `<Enter>`, `<Leave>`)
- Managing game state cleanly across multiple global variables and functions
- Separating "new round" vs. "full reset" logic
- UI/UX polish: hover feedback, win highlighting, conditional widget visibility (`pack()`/`pack_forget()`)
- Using closures correctly in a loop (`lambda event, i=i: ...` to capture the right index per cell)

## 🚀 Run It

```bash
python tic_tac_toe.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
