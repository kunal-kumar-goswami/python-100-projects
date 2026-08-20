<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2037/habit_tracker/day37banner.png" alt="Day 37 - Habit Tracker Banner" width="100%">
</p>

# Day 37 - Habit Tracker 🚴📊

A habit-tracking script built on the [Pixela](https://pixe.la/) API, which turns daily habit data into a GitHub-style contribution graph. This version logs daily cycling distance (in km).

## 🗂️ Project Structure

```
DAY 37/
└── main.py
```

## ⚙️ How It Works

- **User creation (commented out):** `POST` to `pixela_endpoint` with username/token to register a Pixela account — a one-time setup step, now disabled since the account already exists.
- **Graph creation (commented out):** `POST` to create a new graph (`Cycling Graph`, unit `km`, type `float`, color `ajisai`) under the `X-USER-TOKEN` header — also a one-time setup step.
- **Logging today's entry (active):** Prompts for how many kilometers were cycled today, then `POST`s a pixel (a single day's data point) to the graph with today's date (`YYYYMMDD`) and the entered quantity.
- **Updating an entry (commented out):** Shows how to `PUT` a new quantity for an existing date, in case a logged value needs correcting.
- **Deleting an entry (commented out):** Shows how to `DELETE` a pixel for a given date.

This structure demonstrates the full CRUD cycle (Create/Read via POST, Update via PUT, Delete via DELETE) against a real REST API, with only the "create today's pixel" step left active for daily use.

## 🐛 Notes on the current code

- **Typo in comment:** `"How many kilometers did you cyclr today?"` — small spelling slip in the prompt text (`cyclr` → `cycle`).
- **Stray `>` in the delete endpoint:** `delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}>"` has an extra `>` character at the end of the URL, which would break the delete request if it were ever uncommented and used.
- **Hardcoded credentials:** `USERNAME` and `TOKEN` are hardcoded in the script. Since your Pixela token is now visible in this conversation, it'd be worth regenerating it and moving both values to environment variables before pushing to GitHub.

## 🧠 Concepts Practiced

- Making `POST`, `PUT`, and `DELETE` requests with `requests`
- Sending JSON payloads and custom headers (`X-USER-TOKEN`)
- Building dynamic endpoint URLs with f-strings
- Working with dates (`datetime.now().strftime()`)
- Understanding a full CRUD workflow against a real third-party API

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
