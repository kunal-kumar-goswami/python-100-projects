<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2063/day63banner.png" alt="Day 63 - SQLite and SQLAlchemy Banner" width="100%">
</p>

# Day 63 - Databases with SQLite & SQLAlchemy 📚🗄️

A full CRUD book-library app built on a real SQLite database using Flask-SQLAlchemy's modern typed ORM style — moving beyond CSV files into proper relational data storage.

## 🗂️ Project Structure

```
DAY 63/
├── main.py
├── books.db          # created automatically on first run
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit_rating.html
└── README.md
```

## ⚙️ How It Works

- **Modern typed model:** `Book` is defined using SQLAlchemy's newer `Mapped`/`mapped_column` style (rather than the older `db.Column` syntax) — `id` (primary key), `title` (unique, required), `author` (required), and `rating` (float, required).
- **Database setup:** `SQLALCHEMY_DATABASE_URI` points to a local `books.db` SQLite file; `db.create_all()` runs inside an app context to create the table schema on startup if it doesn't already exist.
- **`/` (Read):** queries all books ordered alphabetically by title using `db.select(Book).order_by(Book.title)`, then `.scalars().all()` to get clean `Book` objects (not raw row tuples).
- **`/add` (Create):** on `POST`, builds a new `Book` from form data, adds it to the session, and commits — a classic Create operation with the Post/Redirect/Get pattern.
- **`/edit` (Update):** on `GET`, looks up a book by ID (via `db.get_or_404`) and shows a form to update just its rating; on `POST`, applies the new rating and commits.
- **`/delete` (Delete):** looks up a book by ID and removes it from the database — the code even shows a commented-out alternative lookup method (`db.select().where()`) for comparison.

## 🧠 Concepts Practiced

- Setting up Flask-SQLAlchemy with the modern `DeclarativeBase`/`Mapped` typed model style
- Full CRUD operations against a real relational database
- SQLAlchemy 2.0-style querying (`db.select()`, `.scalars()`, `db.get_or_404()`)
- Application context (`with app.app_context()`) for database setup
- The Post/Redirect/Get pattern across multiple routes
- Structuring a Flask app around persistent, structured data instead of files

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy
python main.py
```

Then open `http://127.0.0.1:5000/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
