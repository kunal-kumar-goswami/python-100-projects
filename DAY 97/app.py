from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"

# Product list
products = [
    {"id": 1, "name": "Headphones", "price": 49.99, 
     "img": "/static/pictures/headphones.png"},
    {"id": 2, "name": "Keyboard",   "price": 89.99, 
     "img": "/static/pictures/keyboard.png"},
    {"id": 3, "name": "Mouse",      "price": 29.99, 
     "img": "/static/pictures/mouse.png"},
    {"id": 4, "name": "Monitor",    "price": 199.99,
     "img": "/static/pictures/monitor.png"},
]

# DB helper
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Init DB
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Routes
@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/product/<int:pid>")
def product_detail(pid):
    product = next((p for p in products if p["id"] == pid), None)
    return render_template("product.html", product=product)

@app.route("/add_to_cart/<int:pid>")
def add_to_cart(pid):
    conn = get_db_connection()
    conn.execute('INSERT INTO cart (product_id) VALUES (?)', (pid,))
    conn.commit()
    conn.close()
    return redirect(url_for("cart_view"))

@app.route("/cart")
def cart_view():
    conn = get_db_connection()
    cart_items_raw = conn.execute('SELECT * FROM cart').fetchall()
    conn.close()

    cart_items = []
    for item in cart_items_raw:
        prod = next((p for p in products if p["id"] == item["product_id"]), None)
        if prod:
            cart_items.append({"cart_id": item["id"], **prod})

    total = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/remove_from_cart/<int:cart_id>")
def remove_from_cart(cart_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM cart WHERE id = ?', (cart_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("cart_view"))

if __name__ == "__main__":
    app.run(debug=True)
