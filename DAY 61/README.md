<p align="center">
  <img src="day61banner.png" alt="Day 61 - WTForms Banner" width="100%">
</p>

# Day 61 - Advanced Forms with Flask-WTF (WTForms) 📋✅

A login page built with `Flask-WTF` and `WTForms` instead of raw HTML forms — bringing built-in validation, CSRF protection, and Bootstrap-styled rendering to Flask forms.

## 🗂️ Project Structure

```
DAY 61/
├── main.py
├── templates/
│   ├── index.html
│   ├── base.html
│   ├── login.html
│   ├── success.html
│   └── denied.html
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

- **`LoginForm` class:** defines the form declaratively as a `FlaskForm` subclass — an `email` field (`StringField`), a `password` field (`PasswordField`), and a `submit` button (`SubmitField`), each with a `DataRequired()` validator ensuring the field can't be left empty.
- **CSRF protection:** `app.secret_key` enables Flask-WTF's built-in CSRF token generation/validation for the form automatically.
- **Bootstrap styling:** `Bootstrap5(app)` integrates `bootstrap-flask`, so the form can be rendered with Bootstrap's styling via Jinja helpers in the template, without hand-writing Bootstrap classes on every field.
- **`/login` route:** handles both `GET` (shows the empty/invalid form) and `POST` (via `login_form.validate_on_submit()`, which combines "was it submitted" and "did it pass all field validators" into one check). On successful validation, it checks the submitted email/password against hardcoded correct values, rendering `success.html` or `denied.html` accordingly.

## 🐛 Notes on the current code

- **Hardcoded login credentials:** `admin@email.com` / `12345678` are hardcoded directly in the route logic — fine for a learning exercise, but in a real app these would come from a database with hashed passwords, not a plaintext comparison in code.
- **`secret_key` is a placeholder string:** `"any-string-you-want-just-keep-it-secret"` should be replaced with an actual random secret value (e.g. `secrets.token_hex(16)`) and, for anything beyond local practice, loaded from an environment variable rather than committed to the repo.

## 🧠 Concepts Practiced

- Declarative form definitions with `Flask-WTF` / `WTForms`
- Field-level validation (`DataRequired`)
- CSRF protection via Flask's `secret_key`
- Bootstrap-styled form rendering with `bootstrap-flask`
- Handling form submission and validation in one method call (`validate_on_submit()`)

## 🚀 Run It

```bash
pip install -r requirements.txt
python main.py
```

Then open `http://127.0.0.1:5001/login` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
