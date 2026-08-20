<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2027/day27banner.png" alt="Day 27 - Miles to Km GUI Banner" width="100%">
</p>

# Day 27  — Miles to Kilometers Converter (Tkinter GUI) 🖥️

A simple desktop GUI app built with `tkinter` that converts miles to kilometers using `Entry`, `Label`, and `Button` widgets laid out with the `grid()` system.

## 🗂️ Project Structure

```
DAY 27/
├── distance_converter.py
├── miles_to_km.py
└── README.md
```

## ⚙️ How It Works

- A `Tk()` window is created with padding, an `Entry` widget for input, and `Label` widgets to display the "Miles", "Is equal to", and "Km" text.
- Widgets are positioned using `grid(column=, row=)`.
- Clicking **Calculate** reads the entered miles value, converts it, and updates the result `Label` with `.config(text=...)`.

## 📄 Two Versions

| File | Conversion Factor | Output Formatting |
|------|-------------------|--------------------|
| `distance_converter.py` | `1.689` | Raw float |
| `miles_to_km.py` | `1.60934` | Rounded to 2 decimals (`:.2f`) |

`miles_to_km.py` is the more refined version — it uses the **correct** miles-to-km conversion factor (`1.60934`; 1 mile ≈ 1.60934 km) and formats the result to 2 decimal places for a cleaner display. `distance_converter.py` looks like an earlier draft with an incorrect factor (`1.689`) and no rounding.

## 🧠 Concepts Practiced

- GUI programming with `tkinter`
- Widgets: `Entry`, `Label`, `Button`
- Layout management with `grid()`
- Event handling via the `command` parameter
- Reading and updating widget text dynamically
- String formatting (`:.2f`)

## 🚀 Run It

```bash
python miles_to_km.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
