# Day 05 — 🔐 PyPassword Generator

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

A password generator that creates a random, shuffled password made up of a custom number of letters, symbols, and numbers.

## 💡 What it does

The program asks how many letters, symbols, and numbers the user wants in their password, randomly picks that many characters from each category, combines and shuffles them, then joins everything into a single unpredictable password string.

**Example:**
```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
2
Here is your password: kD#tRz8!fq2A
```

## 🎯 Concepts Practiced

- Lists of characters (letters, numbers, symbols)
- List comprehensions with `random.choice()`
- Combining lists with `+`
- `random.shuffle()` to randomize order
- `''.join()` to convert a list of characters into a string

## 🔑 Key Takeaways

- A list comprehension (`[random.choice(a) for _ in range(a1)]`) is a concise way to generate multiple random picks without writing a manual loop
- Building the password in separate chunks (letters, symbols, numbers) and only shuffling afterward keeps the required counts of each type accurate while still making the final order unpredictable
- `random.shuffle()` shuffles a list in place, so it doesn't need to be reassigned
- `''.join(list)` is the standard way to turn a list of individual characters back into one string

## 🛠️ Tech Stack

`Python 3` · `random` module

---

