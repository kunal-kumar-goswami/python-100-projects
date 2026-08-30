<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2090/day90banner.png" alt="Day 90 - Disappearing Text Banner" width="100%">
</p>

# Day 90 - Professional Portfolio: GUI Desktop App — Disappearing Text ✍️⏳

A "focus writing" desktop app inspired by tools like The Most Dangerous Writing App — your text starts to vanish if you stop typing for too long, forcing continuous, distraction-free writing. Built with a polished dark-themed `tkinter` interface.

## 🗂️ Project Structure

```
DAY 90/
└── main.py
```

## ⚙️ How It Works

- **Dark, modern UI:** a full custom color palette (background, card, accent blue, success green, danger red) applied across labels, buttons, and the text editor for a cohesive dark-mode look.
- **Key event tracking:** `on_key_release()` records the timestamp of the last keystroke and starts the countdown loop if it isn't already running; `on_key_press()` stops the timer the moment a new key is pressed (so it only counts idle time, not typing time).
- **`countdown()`:** checks elapsed idle time each second via `window.after(1000, countdown)`. If idle time is under 5 seconds, it shows an encouraging "KEEP WRITING..." message in green. Once idle time crosses the 10-second `countdown_time` threshold, it displays "TIME'S UP!" in red and triggers a save-or-delete prompt — but only once per idle period (`popup_shown` flag prevents repeat popups).
- **`prompt_save_or_delete()`:** clears the text widget immediately (so the "disappearing" effect is real), then asks via a `messagebox.askyesno()` dialog whether to save the just-cleared text to `test.txt` or discard it.
- **Manual controls:** a "SAVE FILE" button lets the user save their current text at any time without waiting for the timer, and a "RESTART" button resets the whole session (clearing text, resetting the timer state, and wiping the saved file).

## 🐛 Notes on the current code

- **Countdown display logic has a subtle quirk:** the "KEEP WRITING..." message only shows while elapsed idle time is `<= 5` seconds, meaning there's roughly a 5-second window between "keep writing" and the numeric countdown appearing where the label transitions abruptly — this is a minor UX polish opportunity rather than a functional bug.
- **`last_key_release_time = 0` on restart:** since `time.time()` returns a large real-world timestamp, setting this to `0` means `check_elapsed_time()` will compute an enormous elapsed time immediately after a restart if the countdown loop happens to run before the next keystroke — though since `timer_running` is also set to `False` on restart, the countdown loop isn't actively running at that point, so this isn't currently a live bug, just worth being aware of if the reset logic is ever modified.
- **Global state:** the app manages `timer_running`, `popup_shown`, and `last_key_release_time` as module-level globals modified across many functions — functional here for a single-window app, but wrapping this in a class (as later apps in this portfolio do) would make the state easier to reason about as the app grows.

## 🧠 Concepts Practiced

- Building a polished, dark-themed `tkinter` desktop application
- Idle-time detection via keypress/keyrelease event timing
- Recursive timers with `window.after()` for a live countdown
- Conditional UI state changes based on elapsed time
- File I/O for saving/clearing text
- Dialog-based user prompts (`messagebox.askyesno`)
- Designing UX around a "forcing function" (fear of losing work) to encourage a specific behavior

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
