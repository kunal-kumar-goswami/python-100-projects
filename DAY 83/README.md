<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2083/day83banner.png" alt="Day 83 - Web Development Banner" width="100%">
</p>

# Day 83 - Professional Portfolio: Python Web Development 🌐

The start of a personal portfolio website — a minimal Flask app serving a single templated home page, forming the foundation to build out into a full professional portfolio site.

## 🗂️ Project Structure

```
DAY 83/
├── main.py
├── static/
│   └── assets/
│   └── image/
├── templates/
│   └── index.html
└── README.md
```

## ⚙️ How It Works

- **App setup:** a standard `Flask(__name__)` instance.
- **`/` route:** renders `index.html` via Jinja's `render_template()` — the entry point for the portfolio's home page.
- **Custom port:** runs on port `8080` instead of Flask's default `5000`, with `debug=True` for live-reload during development.

## 🧠 Concepts Practiced

- Setting up a Flask app as the foundation for a larger project
- Serving templated HTML via `render_template()`
- Running the development server on a custom port

## 🚀 Run It

```bash
pip install flask
python main.py
```

Then open `http://127.0.0.1:8080/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
