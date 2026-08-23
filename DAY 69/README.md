<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2069/day69banner.png" alt="Day 69 - Blog Capstone Part 4 Banner" width="100%">
</p>

# Day 69 - Blog Capstone Project (Part 4: Adding Users) 👥💬

The blog capstone reaches full multi-user functionality: real authentication tied to post authorship, an admin-only role, and a threaded comment system with Gravatar profile pictures — combining everything from Days 67–68 into one cohesive app.

## 🗂️ Project Structure

```
DAY 69/
├── main.py
├── forms.py
├── posts.db          # created automatically on first run
├── static/
│   ├── css
│   ├── assets
│   ├── js
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── footer.html
│   ├── header.html
│   ├── make-post.html
│   ├── register.html
│   ├── login.html
│   ├── about.html
│   └── contact.html
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

- **`forms.py`:** all WTForms form classes live here, separated from `main.py` for cleanliness — `CreatePostForm`, `RegisterForm`, `LoginForm`, and a new `CommentForm` (rich-text via `CKEditorField`).
- **Relational database design:** three linked tables —
  - `User` ↔ `BlogPost`: one-to-many via `author_id` foreign key; each post has one author, each user can have many posts (`relationship(..., back_populates=...)` on both sides).
  - `User` ↔ `Comment`: one-to-many, tracking who wrote each comment.
  - `BlogPost` ↔ `Comment`: one-to-many, tracking which post each comment belongs to.
- **`admin_only` decorator:** a custom decorator (built with `functools.wraps`) that checks `current_user.id != 1` and aborts with a `403 Forbidden` if the current user isn't the first registered user — gating post creation and deletion to a single admin account.
- **Gravatar integration:** `flask_gravatar` auto-generates profile images for comment authors based on their email, with a "retro" default style for users without a registered Gravatar.
- **Comments:** `/post/<int:post_id>` now accepts `POST` too — logged-in users can submit a `CommentForm`; if a non-logged-in user tries to comment, they're redirected to `/login` with a flash message.
- **Post authorship:** new posts are now linked to `current_user` as the `author` (instead of a plain text field), and `current_user=current_user` is passed to every template so the UI can conditionally show admin-only controls (edit/delete buttons, "new post" link).


## 🧠 Concepts Practiced

- Relational database modeling with SQLAlchemy (`relationship()`, `ForeignKey`, `back_populates`)
- Custom route decorators for role-based access control
- Linking authenticated users to the content they create (real authorship, not just a name field)
- Threaded comments tied to both a user and a post
- Gravatar integration for user profile images
- Separating form definitions into their own module (`forms.py`) for cleaner project structure

## 🚀 Run It

```bash
pip install -r requirements.txt
python main.py
```

Then open `http://127.0.0.1:5001/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
