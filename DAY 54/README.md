<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2054/day54banner.png" alt="Day 54 - Intro to Flask Banner" width="100%">
</p>

# Day 54 - Introduction to Web Development with Flask 🌶️🌐

The first step into backend web development — a minimal Flask app with a single route that returns a "Hello, World!" response, run in debug mode for live-reloading during development.

## 🗂️ Project Structure

```
DAY 54/
└── app.py
```

## ⚙️ How It Works

- **App initialization:** `Flask(__name__)` creates the Flask application instance.
- **Routing:** The `@app.route("/")` decorator maps the root URL (`/`) to the `hello()` function — whenever a browser requests `/`, Flask calls this function and returns its result as the HTTP response.
- **Running the server:** `app.run(debug=True)` starts Flask's built-in development server, with `debug=True` enabling auto-reload on code changes and detailed error pages in the browser if something goes wrong.
- **`if __name__ == '__main__':`** ensures the server only starts when the script is run directly (not when imported as a module elsewhere).

## 🧠 Concepts Practiced

- Setting up a minimal Flask application
- URL routing with `@app.route()`
- Returning HTTP responses from view functions
- Flask's development server and debug mode

## 🚀 Run It

```bash
pip install flask
python app.py
```

Then open `http://127.0.0.1:5000/` in a browser to see "Hello, World!".

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
