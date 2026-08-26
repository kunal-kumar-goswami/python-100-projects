<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2071/day71banner.png" alt="Day 71 - Deploying Your App Banner" width="100%">
</p>

# Day 71 - Deploying Your Web Application 🚀🌍

## 🗂️ Project Structure

```
DAY 71/
├── main.py
├── forms.py
├── static/
├── templates/
├── requirements.txt
└── README.md
```

## 📌 What Deployment Typically Involves (from this stage of the course)

- **WSGI server:** swapping Flask's development server (`app.run(debug=True)`) for a production-grade WSGI server like **Gunicorn**, since the built-in server isn't designed for real traffic or security.
- **Environment variables for secrets:** `SECRET_KEY`, database URIs, and email credentials should all move out of the code and into environment variables set on the hosting platform, never committed to the repo.
- **Production database:** SQLite (a single local file) is fine for development, but a hosted app typically switches to a managed database like **PostgreSQL**, since most cloud platforms don't persist local files between deploys.
- **Debug mode off:** `debug=True` must be turned off (or conditionally set) before going live — debug mode exposes an interactive traceback/console that's a serious security risk in production.
- **Hosting platform:** deploying to a platform like Render, Railway, Heroku, or similar, which builds and runs the app from the GitHub repo automatically.


## 🧠 Concepts Practiced

- Preparing a Flask app for production deployment
- Environment variables for secrets management
- Understanding the gap between a development server and a production WSGI server
- Recognizing what needs to change (debug mode, database choice, secret handling) before going live

## 🚀 Run It (Locally, for Development)

```bash
pip install -r requirements.txt
python main.py
```

> For actual deployment: set environment variables for all secrets, disable debug mode, and run via a WSGI server (e.g. `gunicorn main:app`) on your chosen hosting platform.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
