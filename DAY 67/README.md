<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2067/day67banner.png" alt="Day 67 - Blog Capstone Part 3 Banner" width="100%">
</p>

# Day 67 - Blog Capstone Project (Part 3: RESTful Routing) 🌐📝

The blog capstone evolves from a static JSON-backed site into a fully database-driven CMS — with rich-text editing, and complete Create/Read/Update/Delete routes for managing posts through the browser.

## 🗂️ Project Structure

```
DAY 67/
├── main.py
├── posts.db          # created automatically on first run
├── static/
│   ├── assets
│   ├── css
│   ├── js
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── make-post.html
│   ├── about.html
│   └── contact.html
└── README.md
```

## ⚙️ How It Works

- **`BlogPost` model:** stores title (unique), subtitle, date, body (`Text` — for longer rich content), author, and image URL.
- **`CreatePostForm`:** a WTForms form used for both creating *and* editing posts, with `title`/`subtitle`/`author`/`img_url` as validated string fields (with a `URL()` check on the image field), and `body` as a **`CKEditorField`** — a rich-text WYSIWYG editor integrated via `flask-ckeditor` instead of a plain textarea.
- **`/` (list):** queries all posts and renders them in `index.html`.
- **`/post/<int:post_id>` (read):** looks up a single post by ID with `db.get_or_404` (auto-404s if not found), rendering the full post.
- **`/new-post` (create):** shows/handles `CreatePostForm`; on successful submission, creates a `BlogPost` with today's date auto-formatted (`"%B %d, %Y"`) and redirects back to the post list.
- **`/edit-post/<int:post_id>` (update):** pre-fills `CreatePostForm` with the existing post's data, letting the same form/template double as both the "new post" and "edit post" UI (distinguished via an `is_edit=True` flag passed to the template).
- **`/delete/<int:post_id>` (delete):** removes a post and redirects back to the list.
- **`/about`, `/contact`:** carried over unchanged from earlier days.

## 🧠 Concepts Practiced

- Full RESTful CRUD (`GET`/`POST` combined logically as Create, Read, Update, Delete) over a database-backed resource
- Reusing a single WTForms form for both create and edit flows
- Rich-text content editing with `flask-ckeditor`
- Auto-formatting dates for display (`date.today().strftime(...)`)
- `db.get_or_404()` for clean not-found handling
- Structuring a capstone project that evolves across multiple days (JSON → CSV-like → full database CMS)

## 🚀 Run It

```bash
pip install flask flask-sqlalchemy flask-bootstrap flask-wtf flask-ckeditor
python main.py
```

Then open `http://127.0.0.1:5002/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
