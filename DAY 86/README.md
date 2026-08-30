<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2086/day86banner.png" alt="Day 86 - Speed Typing Test Banner" width="100%">
</p>

# Day 86 - Professional Portfolio: GUI — Speed Typing Test ⌨️⏱️

A 60-second typing speed test with a dark-themed `tkinter` GUI — highlighting the current word to type, tracking correct/incorrect words, and calculating WPM and CPM at the end, with words pulled from a CSV word bank via `pandas`.

## 🗂️ Project Structure

```
DAY 86/
├── speed_typing.py
└── common_english_words.csv
```

## ⚙️ How It Works

- **Loading words:** `load_words()` reads a CSV of common English words with `pandas`, randomly samples `WORD_COUNT` (150) of them, and inserts them into the text widget as one long string.
- **Highlighting the current word:** `highlight_current_word()` finds the first word (up to the next space) at the start of the text box and applies a tag to visually highlight it in blue.
- **Checking input:** `check_word(event)` fires on every key release, but only actually processes input when the space bar is pressed — comparing the typed word against the target word, logging it as correct or wrong, then deleting that word from the text box and re-highlighting the new first word.
- **Timer:** `start_timer()` recursively schedules itself every second via `window.after(1000, start_timer)`, counting down from `TOTAL_TIME` (60s) and updating the displayed `MM:SS`. When time runs out, it calls `show_results()`.
- **Results:** `show_results()` calculates total characters typed correctly, derives WPM using the standard formula (characters ÷ 5, valid here since the test duration is exactly 1 minute), and displays WPM/CPM/error count both in the stat labels and as a summary message in the text box.
- **Restart:** `restart_test()` resets all state (scores, timer, labels) and starts a fresh round.

## 🐛 Notes on the current code

- **Hardcoded absolute file path:** `pandas.read_csv("./common_english_words.csv")` is a Windows-specific absolute path — this will fail to run on any other machine (or even the same machine if the folder moves). Using a relative path (e.g. `"common_english_words.csv"`, assuming the script and CSV live in the same folder) would make this portable.
- **Potential double-timer bug on restart:** `start_timer()` recursively reschedules itself via `window.after()` regardless of whether the test has ended, and `restart_test()` calls `start_timer()` again without cancelling any previously scheduled `after()` callback. If "Restart" is clicked while a previous timer is still counting down, two timer chains could end up running simultaneously, making the countdown tick twice as fast. Storing the `after()` ID and calling `window.after_cancel()` before starting a new timer would fix this.

## 🧠 Concepts Practiced

- Text widget manipulation and tagging in `tkinter` (`Text`, `.tag_add()`, `.tag_config()`, `.search()`)
- Reading structured data from CSV with `pandas` for dynamic content generation
- Key event handling (`<KeyRelease>`) with conditional logic based on `event.keysym`
- Recursive timers with `window.after()`
- Real-time stats calculation (WPM/CPM) using a standard typing-test formula
- Clean state reset for a "play again" flow

## 🚀 Run It

```bash
pip install pandas
python speed_typing.py
```

> Note: update the CSV file path in `load_words()` to a relative path before running on a different machine.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
