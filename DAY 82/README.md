<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2082/day82banner.png" alt="Day 82 - Morse Code Encoder Banner" width="100%">
</p>

# Day 82 - Professional Portfolio: Python Scripting — Morse Code Encoder 📡

The start of the **Professional Portfolio** section — a polished command-line Morse code encoder, cleanly structured with a single dictionary lookup, input validation, and a proper program loop.

## 🗂️ Project Structure

```
DAY 82/
└── morse_code.py
```

## ⚙️ How It Works

- **`BOOK` dictionary:** a single dictionary mapping every letter and digit to its Morse code equivalent, built once at the top of `main()` — giving O(1) lookup per character instead of scanning a list of tuples.
- **`get_morse(text)`:** uppercases and splits the input into words, converts each word's letters into Morse symbols (skipping unknown characters silently), joins letters within a word using `MINOR_SPACE`, and joins words using `MAJOR_SPACE`.
- **`get_user_input()`:** prompts for a string to convert.
- **`wants_to_continue()`:** validates the user's Y/N response in a loop, only accepting `y` or `n` (case-insensitive) and re-prompting on anything else.
- **Main loop:** prints a stylised ASCII welcome banner, repeatedly encodes user input and prints the result, and exits cleanly with a goodbye banner when the user opts out.
- Everything (constants, dictionary, helper functions) is scoped inside `main()`, keeping the module's top-level namespace clean — with the classic `if __name__ == '__main__':` guard.

## 🧠 Concepts Practiced

- Dictionary-based lookup tables for O(1) character mapping
- String manipulation: `.upper()`, `.split()`, `.join()`
- List comprehension with a conditional filter (`if char in BOOK`)
- Input validation loops with clear re-prompting
- Clean CLI program structure: welcome/goodbye messaging, a controlled main loop, and an exit condition
- Encapsulating program logic inside `main()` for a clean module namespace

## 🚀 Run It

```bash
python morse_code.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
