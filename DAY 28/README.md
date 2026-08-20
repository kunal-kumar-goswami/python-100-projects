<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2028/day28banner.png" alt="Day 28 - Pomodoro Timer Banner" width="100%">
</p>

# Day 28  — Pomodoro Timer GUI 🍅

A desktop Pomodoro productivity timer built with `tkinter`, cycling through work sessions and short/long breaks, with a tomato graphic and checkmark progress tracker.

## 🗂️ Project Structure

```
DAY 28/
├── main.py
├── tomato.png
└── README.md
```

## ⚙️ How It Works

- **Work/Break cycle:** Each call to `start_timer()` increments a `reps` counter. Every 2nd rep is a short break, every 8th rep is a long break, and all other reps are work sessions — implemented with `reps % 2` and `reps % 8`.
- **Countdown:** `count_down()` recursively schedules itself every second using `window.after(1000, count_down, count - 1)`, updating the canvas text with the remaining `MM:SS`.
- **Auto-chain:** When a countdown hits 0, it automatically calls `start_timer()` again to begin the next session (work → break → work...).
- **Progress marks:** After each cycle, a checkmark is added to `check_mark` based on completed work sessions.
- **Reset:** `reset_timer()` cancels the pending `after()` call, resets the display, title, and checkmarks, and zeroes out `reps`.
- The tomato image and timer text are layered on a `Canvas` widget, with `Start`/`Reset` buttons below.

## 🐛 Notes on the current code

- `marks = "✔️"` **overwrites** the string each cycle instead of appending — should be `marks += "✔️"` so completed check marks accumulate visually instead of only ever showing one.
- `WORK_MIN = 1` is currently set for quick testing; for real Pomodoro use it'd typically be `25`.

## 🧠 Concepts Practiced

- GUI programming with `tkinter` (`Canvas`, `Label`, `Button`, `PhotoImage`)
- Recursion for countdown logic
- Scheduling repeated calls with `window.after()` and cancelling with `after_cancel()`
- Modulo-based cycle logic (work vs. short break vs. long break)
- Dynamic widget/text updates

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
