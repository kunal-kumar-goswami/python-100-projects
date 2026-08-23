<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2059/day59banner.png" alt="Day 59 - Blog Capstone Part 2 Banner" width="100%">
</p>

# Day 59 - Blog Capstone Project (Part 2: Adding Styling) 🎨📝

Continuing the multi-page Flask blog from earlier days — now with a full route structure (home, about, contact, individual post pages) and ready for CSS styling to turn it into a polished, presentable site.

## 🗂️ Project Structure

```
DAY 59/
├── BLOG/bootstrap-clean-blog
├── main.py
├── static/
│   └── css/ (or similar, for styling)
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── about.html
│   └── contact.html
└── README.md
```

## ⚙️ How It Works

- **Fetching posts:** all blog posts are fetched once at startup from a hosted npoint.io JSON endpoint via `requests`.
- **`/` (home):** renders `index.html`, passing the full list of posts (`all_posts=posts`) so the template can loop through and display a preview/list of every post.
- **`/about`** and **`/contact`:** simple static-content routes rendering their own templates — rounding out the site into a real multi-page blog rather than just a single feed.
- **`/post/<int:index>`:** looks up a specific post by matching its `id` field against the URL's `index` parameter, then renders `post.html` with that single post's full content.
- **Port 5001:** the app runs on port `5001` instead of Flask's default `5000` — useful if another Flask app (like a different day's project) is already running on 5000.

## 🧠 Concepts Practiced

- Multi-page Flask site structure (home, about, contact, dynamic detail page)
- Fetching and caching external API data at app startup
- Jinja templating with looped and single-item data
- URL-based lookups by matching a field (`id`) rather than list index
- Preparing a Flask app's templates for CSS styling via `static/`

## 🚀 Run It

```bash
pip install flask requests
python main.py
```

Then open `http://127.0.0.1:5001/` in a browser.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
