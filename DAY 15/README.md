<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2015/day15-banner.png" alt="Day 15 — Coffee Machine banner" width="100%" />
</p>

# Day 15 — ☕ Coffee Machine

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A command-line coffee machine simulator that takes drink orders, checks resources, processes coin payments, tracks profit, and reports its current stock — modeling a real vending machine's logic with nested dictionaries and functions.

## 💡 What it does

The program offers espresso, latte, and cappuccino from a menu, each with its own ingredient requirements and cost. Before making a drink it checks whether there's enough water, milk, and coffee; takes payment as quarters/dimes/nickels/pennies; gives change if overpaid or refunds if underpaid; and updates resources and profit accordingly. A `report` command shows current stock and total money made, and `off` shuts the machine down.

**Example:**
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte☕.

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

## 🎯 Concepts Practiced

- Nested dictionaries for modeling a menu with multiple attributes per item
- Functions with parameters and return values
- The `global` keyword for updating a variable (`profit`) from inside a function
- Looping over a dictionary to check and deduct multiple resources at once
- A `while` loop with multiple command branches (`off`, `report`, and drink orders)

## 🔑 Key Takeaways

- Structuring the menu as a dictionary of dictionaries (`MENU[drink]["ingredients"][item]`) keeps all the data for each drink together and easy to extend with new drinks or ingredients
- Checking resource sufficiency and processing payment as separate functions (`is_resource_sufficient()`, `is_transaction_successful()`) keeps each piece of business logic isolated and easy to test on its own
- The `global` keyword is needed here because `profit` is being reassigned inside a function, not just read — without it, Python would treat `profit` as a new local variable
- Looping through `order_ingredients` to check and later deduct from `resources` avoids repeating the same check three times for water, milk, and coffee individually

## 🛠️ Tech Stack

`Python 3`

## 📁 Files

```
day15/
├── main.py       # Coffee machine logic — run this
├── banner.png
└── README.md
```

## 🏃 How to Run

```bash
git clone https://github.com/kunal-kumar-goswami/python-100-projects.git
cd 100-days-of-python/day15
python main.py
```

No external libraries required.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
