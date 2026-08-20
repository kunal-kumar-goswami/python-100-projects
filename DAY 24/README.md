<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2024/day24banner.png" alt="Day 24 - Mail Merge Banner" width="100%">
</p>

# Day 24 — Mail Merge ✉️

A file-handling automation project that generates personalized letters by replacing a placeholder in a template file with each name from a list — a classic "mail merge" workflow.

## 📌 Overview

- Reads a list of invitee names from `invited_names.txt`.
- Reads a template letter from `starting_letter.txt` containing a `[name]` placeholder.
- For each name, replaces the placeholder with that person's name to generate a personalized letter.


## ⚙️ How It Works

- `invited_names.txt` is opened and read line by line into a `names` list.
- `starting_letter.txt` is opened and its full content loaded as a template string.
- For each name in the list, the `[name]` placeholder in the template is replaced with the actual name to build a personalized letter.

## 🐛 Note on the current code

`name.strip()` is stored in `striped_name`, but the `.replace()` call currently uses the raw `name` (which still has a trailing newline `\n`) instead of `striped_name`. This means the generated letters may end up with an extra newline right after the name. Swapping in `striped_name` for the replace call fixes it:

```python
new_letter = letter_content.replace(PLACEHOLDER, striped_name)
```

Also worth adding: writing each `new_letter` out to its own file in `Output/ReadyToSend/` (e.g. `Output/ReadyToSend/letter_for_{striped_name}.txt`) instead of just printing it, so the merged letters are actually saved.

## 🧠 Concepts Practiced

- Reading and writing files (`open`, `readlines`, `read`)
- String manipulation (`.strip()`, `.replace()`)
- Looping over file-derived data
- Basic automation / templating workflow

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
