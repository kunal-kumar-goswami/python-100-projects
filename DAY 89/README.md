<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2089/day89banner.png" alt="Day 89 - Todo App Banner" width="100%">
</p>

# Day 89 - Professional Portfolio: Web Development — Todo App ✅📝

A full multi-user todo list application built with Flask — each user has their own private set of todos (with due dates, time slots, and status), gated behind real authentication.

## 🗂️ Project Structure

```
DAY 89/
├── main.py
├── forms.py
├── static/
│   ├── css/
│   ├── image/
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── todo.html
│   └── edit_todo.html
└── README.md
```

## ⚙️ How It Works

- **`Todo` and `User` models:** linked via a `owner_id` foreign key and a SQLAlchemy `relationship()` (one user → many todos). Each `Todo` stores the task text, due date, start/end time, and status.
- **Authentication:** standard `flask-login` setup — `register()` hashes passwords with `werkzeug.security`, checks for duplicate emails, and logs the new user in immediately; `login()` verifies email/password and redirects to the todo list; `logout()` ends the session.
- **`/mytodo` (protected, `@login_required`):** shows only the **current user's own todos** via `get_all_todos()`, which filters `Todo.query.filter_by(owner_id=current_user.id)` — ensuring users can't see each other's tasks. On form submission, parses date/time strings into proper `date`/`time` objects before creating a new `Todo` linked to `current_user`.
- **Duplicate handling:** wraps the todo creation in a `try`/`except IntegrityError` block, rolling back and flashing an error if a duplicate entry violates a database constraint.
- **`/edit/<int:todo_id>` and `/delete/<int:todo_id>`:** use `db.get_or_404()` for safe lookups (a nice contrast to the Day 88 cafe app, which didn't use this pattern), pre-filling the edit form with the todo's existing values.

## 🐛 Notes on the current code

- **Placeholder secret key:** `app.config['SECRET_KEY'] = 'add-secret-key-here'` is a literal placeholder string — this needs to be replaced with a real random secret (ideally loaded from an environment variable) before the app can properly support sessions/CSRF protection.
- **No ownership check on `/edit` and `/delete`:** unlike `/mytodo`, which correctly filters todos by the logged-in user, the `edit_todo()` and `delete_todo()` routes don't verify that `todo_to_edit.owner_id == current_user.id` — meaning, if a user knows or guesses another user's todo ID, they could currently edit or delete someone else's task. Adding an ownership check (and neither route has `@login_required` either, which compounds this) would close this gap.
- **Leftover debug `print(todo_id)`** in `edit_todo()` — harmless but worth removing before a public deploy.

## 🧠 Concepts Practiced

- Multi-user data isolation via foreign keys and filtered queries
- Full authentication flow with `flask-login` and hashed passwords
- Parsing date/time strings from form input into proper Python `date`/`time` objects
- Handling database integrity errors gracefully with `try`/`except`/rollback
- Safe record lookups with `db.get_or_404()`
- Pre-filling forms for an edit workflow

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy flask-bootstrap flask-wtf flask-login
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
