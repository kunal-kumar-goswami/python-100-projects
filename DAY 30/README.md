<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2030/day30banner.png" alt="Day 30 - Errors, Exceptions & JSON Banner" width="100%">
</p>

# Day 30 / 100 — Errors, Exceptions & JSON Data 🧯

Focused on error/exception handling and working with JSON data — revisited the NATO phonetic alphabet converter and significantly upgraded the Password Manager from Day 29 with proper JSON read/update/write logic and a working search feature.

## 🗂️ Project Structure

```
DAY 30/
├── Nato project/
│   ├── main.py
│   └── nato_phonetic_alphabet.csv
├── password manager/
│   ├── main.py
│   ├── logo.png
│   └── data.json   (created at runtime)
└── README.md
```

---

## 1️⃣ NATO Phonetic Alphabet Converter 🔤

Same core project as Day 26 — converts a typed word into its NATO phonetic alphabet equivalent, using a dictionary built from `nato_phonetic_alphabet.csv` via dictionary comprehension, with `try`/`except KeyError` handling for non-letter input and a recursive retry on error.

---

## 2️⃣ Password Manager v2 🔐

A significantly improved rebuild of the Day 29 password manager, now using proper JSON persistence and exception handling instead of naive appending.

**Password generation:** Builds a randomized password from separate pools of letters, symbols, and numbers (`random.choice` on each pool with `randint`-based counts), shuffles them together with `random.shuffle`, and copies the result to the clipboard via `pyperclip`.

**Saving (`save()`):**
- Validates that Website and Password aren't empty before proceeding.
- Uses `try`/`except FileNotFoundError`/`else`/`finally` to safely handle two cases: no `data.json` exists yet (create it), or it exists (load existing data with `json.load`, merge in the new entry with `dict.update()`, and rewrite the whole file with `json.dump`) — this fixes the "multiple JSON objects appended" issue from Day 29.

**Searching (`find_password()`):** New in this version — looks up a website in `data.json` and displays the saved email/password in a `messagebox`, or an appropriate error if the file or website entry doesn't exist.

## 🧠 Concepts Practiced

- Exception handling (`try` / `except` / `else` / `finally`)
- Reading and safely updating structured JSON data (`json.load`, `json.dump`, `dict.update()`)
- Clipboard integration (`pyperclip`)
- Building a more robust "find" feature on top of an existing GUI app
- Recognizing and fixing a data-persistence bug from a previous project

## 🚀 Run It

```bash
# NATO Alphabet Converter
python "Nato project/main.py"

# Password Manager
python "password manager/main.py"
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
