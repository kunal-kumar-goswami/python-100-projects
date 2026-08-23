<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2057/day57banner.png" alt="Day 57 - Jinja Templating Banner" width="100%">
</p>

# Day 57 - Templating with Jinja in Flask 🧩🌶️

Two Flask apps exploring Jinja2 templating — rendering dynamic HTML from Python data, pulling blog content from a hosted JSON API, and combining multiple external APIs to build a fun "guess the age/gender from a name" page.

## 🗂️ Project Structure

```
DAY 57/
├── blog/
│   ├── main.py
│   ├── post.py
│   ├── static/
│   └── templates/
│       ├── index.html
│       └── post.html
├── server.py
└── README.md
```

---

## 1️⃣ `blog/main.py` — Blog with Individual Post Pages

- **`get_blogs()`:** fetches a list of blog posts from a hosted JSON endpoint (npoint.io) via `requests`.
- **`/` (home):** renders `index.html` via Jinja, passing in the full list of posts (`posts=get_blogs()`) so the template can loop through and display them.
- **`/post/<blog_id>`:** looks up a single post by its 1-based ID (`get_blogs()[int(blog_id) - 1]`), pulls out its title/subtitle/body, and renders `post.html` with those values injected — a classic "list page → detail page" pattern.

## 2️⃣ `server.py` — Randomizer + Name Guesser + Blog

- **`/` (home):** generates a random number (1–11) and the current year, passing both into `index.html` — a common Jinja pattern for showing dynamic content like "Copyright © {{ year }}".
- **`/guess/<name>`:** chains two external APIs — `genderize.io` to predict the gender for a given name, and `agify.io` to predict the age — then renders `guess.html` with the name, gender, and age.
- **`/blog/<num>`:** fetches a hosted blog JSON feed and renders it via `blog.html`.

## 🐛 Notes on the current code

- **Bug in `server.py`'s `/guess/<name>` route:** `age = age_data[" age"]` has a leading space in the dictionary key (`" age"` instead of `"age"`) — since the Agify API actually returns the key as `"age"` (no space), this line would raise a `KeyError` when run. Removing the stray space fixes it.
- **Unused `print(num)` debug line** in `server.py`'s `/blog/<num>` route — harmless but worth removing for a cleaner final version.
- **Two separate Flask apps in one day's folder:** `blog/main.py` and `server.py` aren't connected — they're two independent mini-projects exploring different Jinja/API combinations, so they should be run separately.

## 🧠 Concepts Practiced

- Jinja2 templating with `render_template()` and passing dynamic variables into HTML
- Structuring a Flask project with separate `static/` and `templates/` folders
- List/detail page patterns (blog index → individual post)
- Consuming and combining multiple external REST APIs in one route
- Passing computed values (random numbers, current year) into templates

## 🚀 Run It

```bash
pip install flask requests

# Blog app
cd blog
python main.py

# Randomizer / name guesser / blog server
python server.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
