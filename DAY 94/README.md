<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2094/day94banner.png" alt="Day 94 - GUI Automation Banner" width="100%">
</p>

# Day 94 - Professional Portfolio: GUI Automation — Chrome Dinosaur Game Bot 🦖🤖

A screen-automation bot that plays the Chrome Dinosaur Game for you — it locates the game window, watches a detection zone just ahead of the dinosaur for obstacles using pixel-difference comparison, and presses "jump" automatically until the game ends.

## 🗂️ Project Structure

```
DAY 94/
├── main.py
└── images/
    ├── dinosaur.png
    ├── dinosaur2.png
    └── game_over.png
```

## ⚙️ How It Works

- **Window targeting:** `pyautogui.getWindowsWithTitle()` finds and activates the specific browser window running the Dinosaur Game, so keypresses and screenshots are aimed at the right place on screen.
- **Template matching for setup:** `pyautogui.locateOnScreen('./images/dinosaur.png', ...)` confirms the dinosaur is visible before starting, and a separate `dinosaur2.png` match was used during development to manually work out the coordinates for the fixed obstacle-detection region (`right_region`) just to the right of the dinosaur.
- **Starting the run:** `pyautogui.press('space')` starts the game, then a 2-second pause lets the game stabilize before the bot takes its `initial_screenshot` baseline of the detection zone.
- **Obstacle detection loop:** on each loop iteration, a fresh screenshot of `right_region` is compared against the baseline using `ImageChops.difference()`. If the difference image has a non-empty bounding box, the code counts how many pixels actually changed — a change above the `500`-pixel threshold is treated as an incoming obstacle, triggering `pyautogui.press('up')` to jump.
- **Game-over detection:** each loop also screenshots a separate fixed region (`game_over_region`) and tries to locate `game_over.png` inside it; a successful match flips `game_over = True` and ends the `while` loop.

## 🐛 Notes on the current code

- **Static baseline never updates:** `initial_screenshot` is captured once before the loop and reused for every comparison afterward — as obstacles pass through and background elements shift (score counter, clouds, ground scroll), the diff accumulates unrelated changes over time rather than comparing against the true "just before this obstacle" state.
- **Hardcoded pixel regions:** `left`, `top`, `width`, `height`, and `game_over_region` are all fixed numbers tuned to one specific screen resolution and browser window position — moving the window, changing browser zoom, or running on a different display would silently break detection with no error raised.
- **Fixed jump-only response:** the bot only ever presses `up` to jump; it has no logic for ducking under flying obstacles (pterodactyls), which the real game introduces as difficulty increases.
- **No speed scaling:** the Dinosaur Game accelerates over time, but the `500`-pixel-difference threshold and loop timing stay constant throughout, so the same detection sensitivity that works early in a run may become too slow or too twitchy as obstacles move faster later on.
- **`locate_dinosaur` result unused:** the return value of the first `locateOnScreen()` call is only checked for `None` and never otherwise used, aside from a commented-out debug print.

## 🧠 Concepts Practiced

- Screen automation and keypress simulation with `pyautogui`
- Locating UI elements on screen via image template matching
- Capturing and comparing screenshots with `PIL.ImageChops`
- Pixel-level image difference analysis to detect visual changes
- Building a real-time detection loop with conditional actions
- Automating a browser-based game as a practical computer-vision exercise

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
