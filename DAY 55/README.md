<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2055/day55banner.png" alt="Day 55 - HTML and URL Parsing Banner" width="100%">
</p>

# Day 55 - HTML & URL Parsing in Flask + Higher/Lower Game 🔢🌶️

Deeper into Flask — returning styled HTML directly from routes, stacking custom decorators to wrap responses in HTML tags, parsing dynamic values straight from the URL, and putting it all together in a playable number-guessing game.

## 🗂️ Project Structure

```
DAY 55/
├── main.py            # Primary reference: decorators + HTML + URL parsing
├── hello.py            # Earlier draft version (see note below)
├── number_guessing.py  # Higher/Lower guessing game
└── README.md
```

---

## 1️⃣ `main.py` — Decorators, HTML Rendering & URL Parsing

- **Returning HTML directly:** the `/` route returns a full HTML string (heading, paragraph, image) straight from the view function — Flask sends it back as the page's HTML.
- **Custom decorators:** `make_bold`, `make_emphasis`, and `make_underlined` are hand-written decorators that wrap a route's returned text in `<b>`, `<em>`, and `<u>` tags respectively. The `/bye` route stacks all three (`@make_bold @make_emphasis @make_underlined`), demonstrating how decorators compose from the innermost outward.
- **Dynamic URL parameters:** `/username/<name>/<int:number>` shows Flask's URL converters in action — `<name>` captures any string, while `<int:number>` captures and auto-converts a URL segment to an integer, both passed as arguments to the `greet()` view function.

## `hello.py` — Earlier Draft (kept for reference)

An earlier, rougher version of the same ideas — only applies one decorator (`@make_bold`) to `/bye`, and the `/` route's `<img>` tag is malformed (a nested/broken `<img>`/`<a>` tag string). `main.py` supersedes this version.

---

## 2️⃣ `number_guessing.py` — Higher/Lower Game

A playable browser game built entirely with URL-based routing:
- A random number between 0–9 is generated once when the app starts.
- The home page (`/`) prompts the player to guess.
- Guesses are made by visiting `/<int:guess>` directly in the URL — Flask parses the number from the path and compares it against the hidden target, returning a styled "Too high", "Too low", or "You found me!" HTML response (each with its own color and reaction GIF).

**Concepts:** Using URL path segments as direct game input, conditional HTML responses, integrating external images/GIFs into rendered HTML.

## 🧠 Concepts Practiced (Overall)

- Returning raw HTML from Flask view functions
- Writing and stacking custom Python decorators
- Dynamic URL routing with type converters (`<int:...>`)
- Building simple interactive behavior purely through URL navigation
- Conditional logic driving different HTML responses

## 🚀 Run It

```bash
pip install flask
python main.py              # decorators + HTML + URL parsing demo
python number_guessing.py    # higher/lower game
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
