<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2029/day29banner.png" alt="Day 29 - Password Manager Banner" width="100%">
</p>

# Day 29 / 100 — Password Manager GUI 🔐

A `tkinter` desktop app that generates strong random passwords and saves website/email/password entries to a local file.

## 🗂️ Project Structure

```
DAY 29/
├── main.py
├── logo.png
├── day29banner.png
└── README.md
```

## ⚙️ How It Works

- **Password generation:** `generate_password()` builds a random 12-character password from letters, digits, and punctuation using `random.choice()`, then inserts it into the password field.
- **Saving entries:** `save_password()` reads the Website, Email, and Password fields, packages them into a dict keyed by website, validates that Website and Password aren't empty, and appends the entry to `passwords.txt` using `json.dump()`. All three fields are cleared and a success popup is shown afterward.
- **UI:** Built with `Canvas` (logo), `Label`/`Entry` widgets (Website, Email, Password), and `Button` widgets (Search, Generate Password, Add), laid out with `grid()`.

## 🐛 Notes on the current code

- **Validation doesn't stop the save:** when a field is empty, `messagebox.showwarning()` fires, but the code falls through and still saves/clears the fields — an `else` (or `return`) after the warning check is needed to actually prevent saving invalid entries.
- **`passwords.txt` isn't valid JSON overall:** since each `save_password()` call does a fresh `json.dump()` append, the file ends up as multiple back-to-back JSON objects rather than one valid JSON structure — reading it back later would need extra handling (or switching to load-update-dump-whole-file logic).
- **Search button has no functionality yet** — `search_button` is created but has no `command` attached.

## 🧠 Concepts Practiced

- GUI programming with `tkinter` (`Canvas`, `Entry`, `Label`, `Button`, `messagebox`)
- Random password generation (`random.choice`, `string.ascii_letters/digits/punctuation`)
- Reading/writing structured data with `json`
- Basic input validation

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
