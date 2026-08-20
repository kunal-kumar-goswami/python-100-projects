# NATO Phonetic Alphabet Converter 🔤

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A Python program that converts each letter of a typed word into its corresponding **NATO phonetic alphabet code word**. The project uses a CSV file to build the phonetic alphabet dictionary and includes exception handling for invalid input.

## 📂 Project Structure

```text
Nato project/
├── main.py                         # Main program and conversion logic
└── nato_phonetic_alphabet.csv      # NATO phonetic alphabet data
```

## ⚙️ How It Works

* Reads the NATO phonetic alphabet from `nato_phonetic_alphabet.csv`
* Creates a dictionary using dictionary comprehension
* Takes a word as input from the user
* Converts each character into its corresponding NATO code word
* Uses `try` / `except KeyError` to handle characters that are not present in the alphabet
* Asks the user to enter the word again when invalid input is provided

## 💡 Example

```text
Enter a word: HELLO

['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## 🎯 What I Learned

* Reading CSV files using `pandas`
* Creating dictionaries with dictionary comprehension
* Working with dictionaries and key-value pairs
* Iterating through strings using loops
* Handling exceptions with `try` and `except`
* Handling `KeyError` when a dictionary key doesn't exist
* Using functions to organize program logic
* Validating user input

## 🛠️ Tech Stack

`Python 3` · `Pandas` · `CSV`

---

➡️ [Back to Day 30](https://github.com/kunal-kumar-goswami/python-100-projects/tree/main/DAY%2030) · [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
