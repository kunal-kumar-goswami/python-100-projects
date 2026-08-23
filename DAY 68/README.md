<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2068/day68banner.png" alt="Day 68 - Flask Authentication Banner" width="100%">
</p>

# Day 68 - Authentication with Flask 🔐👤

A complete user authentication system — registration, login, logout, and a protected route — using `flask-login` for session management and `werkzeug.security` for safe password hashing.

## 🗂️ Project Structure

```
DAY 68/
├── main.py
├── users.db          # created automatically on first run
├── static/
│   └── files/
│       └── cheat_sheet.pdf
├── templates/
│   ├── index.html
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   └── secrets.html
└── README.md
```

## ⚙️ How It Works

- **`User` model:** built with `UserMixin` (from `flask-login`) mixed into the SQLAlchemy model, giving it the properties `flask-login` needs (`is_authenticated`, `get_id()`, etc.) automatically. Stores email (unique), hashed password, and name.
- **`login_manager.user_loader`:** tells `flask-login` how to reload a user object from the ID stored in the session on each request.
- **`/register`:** checks if the email already exists (redirecting to login with a flash message if so); otherwise hashes the password with `generate_password_hash()` (PBKDF2-SHA256, salted), creates the user, logs them in immediately via `login_user()`, and redirects to the protected page.
- **`/login`:** looks up the user by email, and uses `check_password_hash()` to verify the submitted password against the stored hash — never comparing plaintext passwords directly. Flashes appropriate error messages for a missing email or wrong password.
- **`/secrets` (protected):** decorated with `@login_required`, so only authenticated users can reach it; displays the logged-in user's name.
- **`/logout`:** ends the session via `logout_user()`.
- **`/download` (protected):** also gated by `@login_required`, serving a PDF file via `send_from_directory()` — a practical example of protecting a downloadable resource, not just a page.
- **`flash()` messages:** used throughout to give users feedback (e.g. "email already registered", "password incorrect") without needing custom error-handling templates.

## 🐛 Notes on the current code

- **Weak/placeholder secret key:** `app.config['SECRET_KEY'] = 'secret-key-goes-here'` is a literal placeholder — this needs to be a real random secret (e.g. `secrets.token_hex(16)`) loaded from an environment variable, especially since Flask's session cookies and CSRF protection depend on this being unguessable.
- **`load_user` uses `db.get_or_404`:** this is a slightly unusual choice inside a `user_loader` callback — `flask-login` expects this function to return `None` if the user isn't found (e.g. after a stale session), but `get_or_404` will raise an HTTP 404 instead, which could produce a confusing error page rather than a clean "please log in again" flow. Using `db.session.get(User, user_id)` (which returns `None` if missing) would be more aligned with `flask-login`'s expected behavior.

## 🧠 Concepts Practiced

- User registration and login with hashed, salted passwords (`werkzeug.security`)
- Session-based authentication with `flask-login` (`UserMixin`, `login_user`, `login_required`, `current_user`, `logout_user`)
- Protecting both pages and file downloads behind authentication
- Using `flash()` for user-facing feedback messages
- Preventing duplicate account registration by checking for an existing email

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy flask-login werkzeug
python main.py
```

Then open `http://127.0.0.1:5000/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
