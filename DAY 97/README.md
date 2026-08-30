<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2097/day97banner.png" alt="Day 97 - Web Development Banner" width="100%">
</p>

# Day 97 - Professional Portfolio: Web Development — Flask Shopping Cart 🛒💻

A small e-commerce demo built with Flask — browsable product listing and detail pages backed by an in-memory product catalog, plus a persistent shopping cart backed by SQLite that supports adding, viewing, and removing items.

## 🗂️ Project Structure

```
DAY 97/
├── app.py
├── database.db          (auto-created on first run)
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── product.html
│   └── cart.html
└── static/
    └── style.css
    └── pictures/
        ├── headphones.png
        ├── keyboard.png
        ├── mouse.png
        └── monitor.png
 
```

## ⚙️ How It Works

- **Product catalog:** `products` is a simple in-memory list of dictionaries (id, name, price, image path) — no database needed for the catalog itself since it's static demo data.
- **Database helper:** `get_db_connection()` opens a SQLite connection with `row_factory = sqlite3.Row`, so query results can be accessed like dictionaries (`item["product_id"]`) instead of plain index-based tuples.
- **Schema setup on startup:** `init_db()` runs `CREATE TABLE IF NOT EXISTS cart` once when the app starts, ensuring the `cart` table (an auto-incrementing id paired with a `product_id`) always exists before any route tries to use it.
- **Browsing routes:** `/` renders the full product grid from the `products` list, and `/product/<int:pid>` looks up a single product by id using `next()` with a generator expression, passing it to a dedicated detail template.
- **Adding to cart:** `/add_to_cart/<int:pid>` simply inserts a new row into the `cart` table with the given `product_id` — each row represents one unit of one product in the cart — then redirects to the cart view.
- **Viewing the cart:** `/cart` fetches every row from the `cart` table, joins each row back to its full product info from the in-memory `products` list, tags each with its own `cart_id` (the cart table's row id, needed for removal), and computes the running `total` price.
- **Removing from cart:** `/remove_from_cart/<int:cart_id>` deletes a specific row from the `cart` table by its own id, letting the user remove exactly one item without affecting others.

## 🐛 Notes on the current code

- **`GET` requests perform state-changing actions:** `add_to_cart` and `remove_from_cart` are defined with the default `GET` method but modify the database — this means simply visiting or refreshing those URLs (or a search engine/browser prefetching a link) can add or remove cart items unintentionally. These should be `POST` routes triggered by a form or button.
- **No per-user cart isolation:** the `cart` table has no concept of a session, user, or cart ID — every visitor to the app shares the exact same cart, so one person's additions or removals affect everyone using the app.
- **No quantity field:** adding the same product twice creates two separate rows rather than incrementing a quantity — functionally correct for the total, but the cart page would show duplicate line items instead of "Headphones x2."
- **Missing 404 handling for unknown product IDs:** `product_detail()` passes `None` to the template if no product matches `pid`, which would either crash the template (if it assumes `product` always has data) or render a broken/empty detail page rather than a proper "not found" response.
- **Debug mode left on:** `app.run(debug=True)` is fine for local development but should never be used in production, since Flask's debugger can expose a remote code execution vector if the app is ever deployed publicly as-is.

## 🧠 Concepts Practiced

- Building multi-route Flask applications with dynamic URL parameters
- Combining static in-memory data with a persistent SQLite-backed feature
- Using `sqlite3.Row` for dictionary-style access to query results
- Basic CRUD operations (Create/Read/Delete) against a database table
- Redirecting after state-changing requests (POST/Redirect/GET-style flow, partially applied)
- Rendering dynamic data into Jinja templates across multiple linked pages
- Structuring a simple full-stack app: routes, templates, and a database layer

## 🚀 Run It

```bash
python app.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
