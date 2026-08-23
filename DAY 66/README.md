<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2066/day66banner.png" alt="Day 66 - Building Your Own API Banner" width="100%">
</p>

# Day 66 - Building Your Own API with RESTful Routing 🔌📡

A full RESTful API for a cafe database — covering all major HTTP verbs (`GET`, `POST`, `PATCH`, `DELETE`), JSON responses, query parameters, and basic API-key authorization, tested via Postman.

## 🗂️ Project Structure

```
DAY 66/
├── main.py
├── cafes.db          # created automatically on first run
├── templates/
│   └── index.html
└── README.md
```

## ⚙️ How It Works

- **`Cafe` model:** stores name, map/image URLs, location, seats, and boolean amenities (toilet, wifi, sockets, calls), plus an optional coffee price. A `to_dict()` method converts any `Cafe` instance into a JSON-serializable dictionary by iterating over the table's columns.
- **`GET /random`:** picks a random cafe from the database and returns it as JSON.
- **`GET /all`:** returns every cafe, ordered alphabetically by name, as a JSON list.
- **`GET /search?loc=<location>`:** filters cafes by exact location match; returns a `404` with a JSON error if none are found.
- **`POST /add`:** creates a new cafe from form-encoded data (designed to be tested via Postman with `x-www-form-urlencoded` body), returning a JSON success message.
- **`PATCH /update-price/<int:cafe_id>`:** updates just the `coffee_price` of a specific cafe via a query parameter, returning `200` on success or `404` if the ID doesn't exist.
- **`DELETE /report-closed/<int:cafe_id>`:** deletes a cafe, but only if the request includes a matching `api-key` query parameter — otherwise returns a `403 Forbidden`.

## 🐛 Notes on the current code

- **Bug in the `DELETE` route:** `cafe = db.get(Cafe, cafe_id)` should be `db.session.get(Cafe, cafe_id)` — `db.get()` isn't a valid Flask-SQLAlchemy method (the working version, `db.session.get()`, is correctly used in the `PATCH` route just above it). This would raise an `AttributeError` before ever reaching the `except AttributeError` handler meant to catch a missing cafe, since the error actually happens on the `db.get` call itself, not on a `None` cafe.
- **Boolean fields parsed incorrectly:** `has_sockets=bool(request.form.get("sockets"))` (and similarly for toilet/wifi/calls) will evaluate to `True` for *any* non-empty string, including `"false"` or `"0"` — since `bool("false")` is `True` in Python. A proper check like `request.form.get("sockets") == "true"` would be needed for this to behave correctly.
- **Hardcoded API key:** `"TopSecretAPIKey"` is a hardcoded literal used for the delete authorization check — fine for a learning exercise, but in a real API this would come from a securely stored, rotatable secret rather than a string literal in the code.

## 🧠 Concepts Practiced

- Designing RESTful routes around HTTP verbs (`GET`, `POST`, `PATCH`, `DELETE`)
- Returning JSON responses with `jsonify()`
- Query parameters vs. form data vs. URL path parameters
- Basic API authorization via a shared secret key
- Proper HTTP status codes for success/not-found/forbidden responses
- Serializing SQLAlchemy model instances to dictionaries/JSON

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy
python main.py
```

Test the endpoints with Postman or `curl` — e.g. `GET http://127.0.0.1:5000/random`.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
