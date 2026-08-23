<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2062/day62banner.png" alt="Day 62 - Coffee and Wifi Banner" width="100%">
</p>

# Day 62 - Coffee & Wifi: Flask + WTForms + Bootstrap + CSV ☕📶

A crowd-sourced cafe directory: users submit info about a cafe (location, hours, coffee/wifi/power ratings) via a validated WTForms form, which gets appended to a CSV file, and the full list is displayed back as a browsable table.

## 🗂️ Project Structure

```
DAY 62/
├── main.py
├── cafe-data.csv
├── templates/
│   ├── index.html
│   ├── add.html
│   └── cafes.html
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

- **`CafeForm` class:** a `FlaskForm` with a mix of field types —
  - `StringField`s for cafe name, opening/closing time (all `DataRequired`).
  - A `location` field validated with both `DataRequired()` **and** `URL()`, ensuring it's a properly formatted Google Maps link.
  - `SelectField` dropdowns for coffee rating, wifi rating, and power socket availability, each using emoji-based choice scales (e.g. `"☕☕☕"`, `"💪💪💪💪"`, `"🔌🔌"`).
- **`/` (home):** a simple landing page.
- **`/add` (GET/POST):** shows the `CafeForm`; on successful validation, appends a new comma-separated row to `cafe-data.csv` and redirects to `/cafes` (the Post/Redirect/Get pattern, preventing duplicate submissions on refresh).
- **`/cafes`:** reads the entire CSV file with Python's built-in `csv` module, collects every row into a list, and renders `cafes.html` to display them (likely as a table).

## 🐛 Notes on the current code

- **CSV writing bypasses the `csv` module:** `/add` writes rows manually with an f-string (`csv_file.write(f"\n{...},{...}")`) instead of using `csv.writer()`. This works for simple data, but if a cafe name or location ever contained a comma, it would silently corrupt the CSV structure — using `csv.writer().writerow([...])` would handle quoting/escaping automatically and be more robust.
- **Real secret key exposed:** `app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'` is a real-looking generated secret hardcoded directly in the file. Since this is going to a public repo, it's worth regenerating a new secret key and loading it from an environment variable instead.
- **No duplicate-entry protection:** a user could submit the same cafe multiple times with no check against existing rows.

## 🧠 Concepts Practiced

- Building forms with mixed field types (`StringField`, `SelectField`) and validators (`DataRequired`, `URL`)
- Bootstrap-styled form rendering via `bootstrap-flask`
- Reading and appending to CSV files as a lightweight data store
- The Post/Redirect/Get pattern (`redirect(url_for(...))` after a successful form submission)
- Rendering tabular data dynamically from a file

## 🚀 Run It

```bash
pip install -r requirements.txt
python main.py
```

Then open `http://127.0.0.1:5002/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
