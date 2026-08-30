<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2085/day85banner.png" alt="Day 85 - Image Watermarker Banner" width="100%">
</p>

# Day 85 - Professional Portfolio: GUI — Image Watermarker 🖼️✍️

A real, usable desktop tool: a `tkinter` GUI app for adding a custom text watermark to any image — with a live drag-to-position preview, color picker, adjustable font size, and export to a full-resolution result.

## 🗂️ Project Structure

```
DAY 85/
└── watermark.py
```

## ⚙️ How It Works

- **Image selection:** `select_image()` opens a native file dialog (`filedialog.askopenfilename`) and loads the chosen image with `PIL.Image`.
- **Live preview at reduced size:** `show_preview()` creates a thumbnail-sized copy of the image for the canvas (`CANVAS_SIZE` = 300px) and records the `scale` factor between the preview and the full-resolution original — critical for later converting preview coordinates back to real image coordinates.
- **Positioning the watermark:** clicking or dragging on the canvas (`<Button-1>`, `<B1-Motion>`) updates `watermark_x`/`watermark_y` in real time via `move_watermark()`. A directional arrow pad (`↑ ← → ↓`) offers fine-grained nudging in `STEP`-pixel increments as an alternative to dragging.
- **Live text preview:** `draw_watermark_preview()` redraws the watermark text on the canvas at the current position, color, and font size every time something changes.
- **Color picker:** `choose_color()` opens the native `colorchooser` dialog and updates both the preview text color and a visual swatch.
- **Font handling:** `get_font(size)` tries a list of common font file paths in order (`arial.ttf`, `DejaVuSans.ttf`, a Linux-specific path) and falls back to Pillow's default font if none are found — making the app more portable across operating systems.
- **Saving the final image:** `save_image()` validates that an image and watermark text exist, converts the preview's position and font size back to full-resolution coordinates using the stored `scale`, draws the watermark directly onto a copy of the **original, full-size** image with `ImageDraw`, and saves it via another native file dialog — with clear error/success message boxes throughout.

## 🐛 Notes on the current code

- **Preview-to-full-size scaling is the trickiest part, and it's handled correctly:** since the canvas shows a shrunk thumbnail, naively saving at the preview's pixel coordinates and font size would place the watermark in the wrong spot at the wrong size on the real image. Dividing both position and font size by `scale` before drawing on the full-size copy is exactly right — worth calling out since it's a common bug source in similar tools.
- **Font file paths are somewhat fragile:** the `FONT_FILES` list assumes specific paths that may not exist on every system (especially `arial.ttf`, which isn't present by default on Linux/macOS) — the fallback to `ImageFont.load_default()` handles this gracefully, though the default font is quite small/basic compared to a proper TrueType font.

## 🧠 Concepts Practiced

- Building a full-featured `tkinter` GUI with Canvas-based interactivity
- Working with `Pillow` for image loading, drawing, and saving
- Native file dialogs (`filedialog`) and color picker (`colorchooser`)
- Coordinate/scale conversion between a preview and the underlying full-resolution data
- Mouse event binding for click-and-drag interaction
- Font fallback handling for cross-platform compatibility
- Clear user feedback via `messagebox` for error and success states

## 🚀 Run It

```bash
pip install pillow
python watermark.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
