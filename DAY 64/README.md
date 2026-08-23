<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2064/day64banner.png" alt="Day 64 - Top 10 Movies Banner" width="100%">
</p>

# Day 64 - My Top 10 Movies Website 🎬🏆

A personal movie-ranking site: search for a movie via TMDB, add it to a local database, rate and review it, and see the collection auto-ranked by rating — combining Flask, SQLAlchemy, WTForms, Bootstrap, and an external API all in one project.

## 🗂️ Project Structure

```
DAY 64/
├── main.py
├── static/css 
├── movies.db          # created automatically on first run
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── select.html
│   └── edit.html
└── README.md
```

## ⚙️ How It Works

- **`Movie` model:** stores title, year, description, rating, ranking, review, and poster image URL — `rating`, `ranking`, and `review` are nullable since a newly-added movie won't have them yet.
- **`FindMovieForm`** and **`RateMovieForm`:** two separate WTForms forms — one for searching by title, one for entering a rating/review.
- **`/` (home):** queries all movies ordered by rating, then computes each movie's `ranking` on the fly (highest rating = rank 1) and saves it back to the database before rendering.
- **`/add` (search):** takes a movie title, searches the TMDB API (`MOVIE_DB_SEARCH_URL`), and shows a list of matching results for the user to pick from (`select.html`).
- **`/find` (fetch details & save):** given a selected TMDB movie ID, fetches full details (title, release year, poster, overview) from TMDB, creates a new `Movie` record with just that data (no rating yet), and redirects straight into the rating/edit page.
- **`/edit` (rate/review):** lets the user set the movie's rating and review, then commits and returns to the home page.
- **`/delete`:** removes a movie from the collection by ID.

## 🐛 Notes on the current code

- **Placeholder API key:** `MOVIE_DB_API_KEY = "USE_YOUR_OWN_CODE"` needs to be replaced with a real TMDB API key before the search/add features will work — and once filled in, it should come from an environment variable rather than being hardcoded, especially for a public repo.
- **Real secret key exposed:** `app.config['SECRET_KEY']` uses the same hardcoded value seen in the Day 62 Coffee & Wifi project — worth generating a fresh, unique secret per project and loading it from an environment variable.
- **Ranking recalculated on every home page load:** since `/` recomputes and commits `ranking` for every movie on every visit, this adds a database write on every page load rather than only when the collection actually changes (e.g. after adding or rating a movie) — functionally fine for a small personal project, but not ideal for scale.

## 🧠 Concepts Practiced

- Combining a database (SQLAlchemy/SQLite), an external REST API (TMDB), and validated forms (WTForms) in one cohesive app
- Multi-step user flow: search → select from results → fetch full details → rate/review
- Dynamic ranking computation based on stored data
- Bootstrap-styled forms and layout
- Full CRUD over a real-world, richer data model (multiple fields, some optional)

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy flask-bootstrap flask-wtf requests
python main.py
```

> Note: requires a real TMDB API key (`MOVIE_DB_API_KEY`) to search for and add movies.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
