<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2092/day92banner.png" alt="Day 92 - Image Processing & Data Science Banner" width="100%">
</p>

# Day 92 - Professional Portfolio: Image Processing & Data Science — Image Color Palette Extractor 🎨🖼️

A Flask web app that takes an uploaded image and extracts its most dominant colors, returning them as a ranked list of hex codes — combining `Pillow` for image/palette processing with `pandas` for sorting and formatting the color data.

## 🗂️ Project Structure

```
DAY 92/
├── main.py
├── templates/
│   └── index.html
└── static/assets/
    └── css/
    │   └── style.css
    └── image/
    │   └── foodplatter.png
        
```

## ⚙️ How It Works

- **`get_RGB()`:** opens the image with `Pillow` and converts it to a web-safe palette (`Image.Palette.WEB`), then reads back the palette's RGB triplets. `getcolors()` returns each palette index's pixel count, which is paired with its RGB value and loaded into a `pandas` DataFrame.
- **Sorting by dominance:** the DataFrame is sorted by pixel `count` (descending) and sliced down to the requested number of colors, giving the N most dominant colors in the image.
- **Sorting by brightness:** a `Total` column (`r + g + b`) is computed and used to re-sort the final colors from darkest to lightest, so the palette displays in a visually logical gradient rather than by raw frequency.
- **`rgb_to_hex()`:** converts each `(r, g, b)` triplet into a `#rrggbb` hex string using Python's f-string zero-padded hex formatting.
- **`get_hex_list()`:** ties it together — runs `get_RGB()`, applies `rgb_to_hex()` across every row of the DataFrame with `.apply()`, and returns the final list of hex codes ready for the template.
- **Two routes:** `/` loads a default sample image (`foodplatter.png`) with a preset palette size of 10 colors, while `/upload` (`POST`) handles user-submitted images and a user-chosen number of colors from a form field.

## 🐛 Notes on the current code

- **Web-safe palette limits color accuracy:** converting to `Image.Palette.WEB` snaps every pixel to the nearest of only 216 web-safe colors before counting, so the extracted palette is an approximation of the image's true dominant colors rather than the exact original RGB values.
- **No error feedback on failed uploads:** the `try/except` in `/upload` catches exceptions and redirects back to `/` on failure, but doesn't flash a message explaining what went wrong — the user just sees the page reset with no clear indication of the issue.
- **No file-type validation:** like the upload route in Day 91, `display_colors()` trusts the incoming file is a valid image; a non-image upload would raise an exception inside `Image.open()` deep in `get_RGB()`.
- **`color_number` isn't bounds-checked:** requesting more colors than exist in the image's palette (or a negative/zero value) isn't validated before slicing the DataFrame, which could silently return fewer colors than expected instead of a clear error.

## 🧠 Concepts Practiced

- Building a Flask app with separate `GET` and `POST` routes for display vs. upload
- Image palette extraction and pixel-frequency analysis with `Pillow`
- Structuring and sorting extracted data using `pandas` DataFrames
- Converting RGB values to hex color codes
- Passing dynamic image and color data from Flask into Jinja templates
- Basic error handling around file uploads and image processing

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
