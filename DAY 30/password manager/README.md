# Password Manager v2 🔐

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

An upgraded **Password Manager** built with Python and Tkinter. This version improves the Day 29 project by introducing proper **JSON data persistence**, exception handling, password searching, and clipboard integration.

## 📂 Project Structure

```text
password manager/
├── main.py        # Main GUI, password generation, saving, and searching
├── logo.png       # Password Manager logo
└── data.json      # Stored website, email, and password data
```

> `data.json` is created automatically at runtime when the first password is saved.

## 🔐 Features

### 🎲 Password Generator

* Generates randomized passwords
* Uses letters, numbers, and symbols
* Randomizes the generated characters
* Automatically copies the password to the clipboard

### 💾 Save Password

* Validates that Website and Password fields are not empty
* Stores password information in `data.json`
* Loads existing JSON data before adding a new entry
* Updates the dictionary with the new website entry
* Writes the updated data back to the JSON file

### 🔎 Search Password

* Searches saved credentials by website
* Displays the saved email and password in a message box
* Handles missing websites gracefully
* Handles the case where `data.json` does not exist

## ⚙️ How It Works

The project uses JSON instead of simply appending multiple objects to a file.

```text
User Input
    ↓
Validate Website & Password
    ↓
Load existing JSON data
    ↓
Update dictionary
    ↓
Write updated data to data.json
    ↓
Password Saved
```

For searching:

```text
Enter Website
    ↓
Read data.json
    ↓
Find Website
    ↓
Display Email & Password
```

## 🧯 Exception Handling

The project uses:

* `try` to execute file operations safely
* `except FileNotFoundError` when `data.json` doesn't exist
* `else` when JSON data is successfully loaded
* `finally` to complete the file-handling process safely

This prevents the application from crashing when the JSON file has not yet been created.

## 🧠 Concepts Practiced

* Tkinter GUI development
* Exception handling with `try` / `except` / `else` / `finally`
* Reading JSON using `json.load()`
* Writing JSON using `json.dump()`
* Updating dictionaries with `dict.update()`
* File handling
* Password generation with `random`
* Clipboard integration with `pyperclip`
* Searching structured data
* Building on and improving an existing project
* Debugging and fixing data-persistence problems

## 🛠️ Tech Stack

`Python 3` · `Tkinter` · `JSON` · `Random` · `Pyperclip`

## 🚀 Run It

```bash
python main.py
```
<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2030/password%20manager/password.png" alt="Password Manager" width="600">
</p>


---

➡️ [Back to Day 30](../) · [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
