<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2088/day88banner.png" alt="Day 88 - Cafe Directory Banner" width="100%">
</p>

# Day 88 - Professional Portfolio: Web Development — Cafe Directory ☕🗺️

A full-featured Flask cafe directory app with a real SQLite database — complete CRUD operations, location-based search, a random cafe picker, and Bootstrap-styled WTForms for adding and editing entries.

## 🗂️ Project Structure

```
DAY 88/
├── main.py
├── forms.py
├── static/
│   ├── style.css
├── cafes.db
├── templates/
│   ├── index.html
│   ├── cafes.html
│   ├── search.html
│   ├── add.html
│   └── update.html
└── README.md
```

## ⚙️ How It Works

- **`Cafe` model:** name (unique), map/image URLs, location, boolean amenities (sockets, toilet, wifi, calls), seats, and optional coffee price.
- **`/` :** simple home page.
- **`/cafes`:** lists every cafe in the database.
- **`/random`:** picks one random cafe (`random.choice()`) and reuses the `cafes.html` template by wrapping it in a single-item list.
- **`/search` (GET/POST):** a `Search` form filters cafes by location (title-cased for consistency), returning matching results — or an empty list if no results are found (note: results aren't explicitly checked for emptiness in the route, that's left to the template).
- **`/add` (GET/POST):** an `Add` form collects all cafe details, converting the emoji checkbox-style inputs (`'✅'`) into proper booleans, then creates and commits a new `Cafe` row, redirecting to `/cafes`.
- **`/update` (GET/POST/PATCH):** looks up a cafe by ID, pre-fills an `Update` form with its current seats/price, and on submission updates the amenities, seats, and price fields in place.
- **`/delete` (GET/DELETE):** removes a cafe by ID and redirects back to `/cafes`.

## 🐛 Notes on the current code

- **Boolean conversion pattern is a bit verbose:** `bool(1 if form.x.data == '✅' else 0)` could be simplified to `form.x.data == '✅'` directly (which already evaluates to a boolean) — functionally identical, just less code for the same result.
- **Same hardcoded `SECRET_KEY`:** `'YOUR KEY'` is the same key used in multiple earlier projects (Days 62, 64, 67) — still worth generating a unique one per project and loading it from an environment variable.
- **`Update` route allows `PATCH` but doesn't distinguish it from `POST`:** both are treated identically via `form.validate_on_submit()`, so the `PATCH` method declaration doesn't add any real behavior difference here — it's a minor semantic nod to REST conventions rather than functional routing.
- **No validation on `cafe_id`:** `Cafe.query.get(cafe_id)` in both `/update` and `/delete` will return `None` if the ID doesn't exist, which would then raise an `AttributeError` when the code tries to access `selected_cafe.seats` etc. — a `get_or_404()` (as used in some earlier Flask-SQLAlchemy projects) would fail more gracefully here.

## 🧠 Concepts Practiced

- Full CRUD with Flask-SQLAlchemy over a real cafe dataset
- Bootstrap-styled forms via `Flask-Bootstrap` and `Flask-WTF`
- Location-based filtering with `.filter()`
- Random selection from a database query
- Reusing a single template across multiple routes (`cafes.html` for both the full list and the random pick)
- Pre-filling a form with existing database values for an edit flow

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy flask-bootstrap flask-wtf
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
