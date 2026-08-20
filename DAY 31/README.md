<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2031/day31banner.png" alt="Day 31 - Flash Card App Banner" width="100%">
</p>

# Day 31 — Flash Card App 🃏

A `tkinter` flashcard app ("Flashy") for learning French vocabulary. Cards flip automatically from French to English after a delay, and known words are removed from the deck and persisted to disk.

## 🗂️ Project Structure

```
DAY 31/
├── main.py
├── data/
│   ├── french_words.csv
│   └── words_missed.csv   (created/updated at runtime)
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── README.md
```

## ⚙️ How It Works

- **Data loading:** On startup, tries to load `words_missed.csv` (previously unlearned words). If it doesn't exist yet, falls back to the full `french_words.csv` deck. Both are converted to a list of dicts with `to_dict(orient="records")`.
- **Showing a card:** `next_card()` picks a random word with `random.choice()`, updates the canvas to show the French word on the card-front image, and schedules an automatic flip after 3 seconds via `window.after()`.
- **Flipping:** `flip_card()` swaps the canvas text/image to show the English translation on the card-back image.
- **Marking as known:** `is_known()` removes the current word from `to_learn`, saves the remaining words back to `words_missed.csv` via a `DataFrame`, and immediately shows the next card.
- **Marking as unknown:** The ❌ button just calls `next_card()` directly, leaving the word in the deck so it can appear again.
- `window.after_cancel(flip_timer)` in `next_card()` prevents old flip timers from stacking up when a new card is shown early.

## 🧠 Concepts Practiced

- GUI programming with `tkinter` (`Canvas`, `PhotoImage`, `Button`)
- Scheduling and cancelling delayed actions (`window.after()`, `after_cancel()`)
- Reading/writing CSV data with `pandas` (`read_csv`, `to_dict`, `DataFrame`, `to_csv`)
- Exception handling (`try`/`except FileNotFoundError`) to support resuming progress across sessions
- Randomized selection (`random.choice`)

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
