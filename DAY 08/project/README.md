# Day 08 — 🔐 Caesar Cipher

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

A Caesar Cipher tool that encodes or decodes a message by shifting each letter through the alphabet by a chosen number of places — with support for spaces, numbers, and symbols, invalid input handling, and the ability to run again without restarting the program.

## 💡 What it does

The program asks whether to encode or decode, takes a message, and takes a shift number. It then shifts every letter in the message forward (encode) or backward (decode) through the alphabet by that amount, printing the result. Non-letter characters (spaces, punctuation, numbers) are left untouched, invalid shift input is caught instead of crashing the program, and the user can choose to run the cipher again without restarting.

**Example:**
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
meet me at midnight
Type the shift number:
4
This is the encoded result: qievduiadwmndsmklx
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye
```

## 🧱 Build Process

This project was built incrementally across 4 files/stages:

1. **`art.py`** — ASCII art logo, printed at the start of the program
2. **Encrypt only** — a single `encrypt()` function that shifts letters forward by a fixed amount, using `%` to wrap around the end of the alphabet
3. **Encrypt + decrypt combined** — added a matching `decrypt()` function, then merged both into one `caesar()` function that branches on the user's chosen direction
4. **Final polish** — imports the logo from `art.py`, handles non-letter characters (spaces/numbers/symbols) by leaving them unchanged, validates the shift number with a `try`/`except` loop, and lets the user restart the cipher without rerunning the program

## 🎯 Concepts Practiced

- Functions with multiple parameters
- List indexing and the modulo operator (`%`) to wrap around the end of a list
- Combining two similar functions into one using a conditional branch
- `try`/`except` for input validation
- `while` loops for a repeatable, restartable program
- Splitting code across multiple files with `import`

## 🔑 Key Takeaways

- `shift_amount % len(alphabet)` is what makes the shift "wrap around" — without it, shifting `z` forward would throw an index error
- Encoding and decoding are really the same operation in opposite directions — decoding is just encoding with the shift amount negated, which is why both fit inside one `caesar()` function
- Checking `if letter not in alphabet` before shifting is what allows the cipher to handle spaces, numbers, and punctuation without crashing
- Wrapping `int(input(...))` in a `try`/`except` loop stops invalid input (like text where a number is expected) from crashing the whole program
- A `while should_continue` loop with a restart prompt turns a single-run script into a small, reusable tool

## 🛠️ Tech Stack

`Python 3`
