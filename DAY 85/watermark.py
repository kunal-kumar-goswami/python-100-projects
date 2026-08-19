from tkinter import *
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# ---------- Colors (dark theme) ----------
BG = "#0d1117"
BG_ELEV = "#121926"
CANVAS_BG = "#161f2e"
RULE = "#212b3a"
TEXT = "#dbe4ee"
MUTED = "#7c8aa0"
YELLOW = "#f4c430"

FONT_NAME = "Courier New"
CANVAS_SIZE = 300

# a few common font files to try, in order, so it works on most computers
FONT_FILES = ["arial.ttf", "DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
FONT_SIZES = [20, 28, 36, 48, 64, 80, 100]
STEP = 5   # how many pixels each arrow button nudges the text

# ---------- Game... I mean app state ----------
original_image = None
scale = 1.0
watermark_x = CANVAS_SIZE // 2
watermark_y = CANVAS_SIZE // 2
selected_color = "#ffffff"


def select_image():
    global original_image
    path = filedialog.askopenfilename()
    if not path:
        return
    original_image = Image.open(path).convert("RGB")
    show_preview()


def show_preview():
    global scale
    canvas.delete("all")

    if original_image is None:
        canvas.create_text(CANVAS_SIZE / 2, CANVAS_SIZE / 2,
                            text="select an image to begin", fill=MUTED)
        return

    small = original_image.copy()
    small.thumbnail((CANVAS_SIZE, CANVAS_SIZE))
    scale = small.width / original_image.width

    canvas.image = ImageTk.PhotoImage(small)   # keep a reference so it isn't garbage collected
    canvas.create_image(0, 0, anchor=NW, image=canvas.image)
    draw_watermark_preview()


def draw_watermark_preview():
    if original_image is None:
        return
    canvas.delete("watermark")
    text = watermark_entry.get() or "your text here"
    canvas.create_text(watermark_x, watermark_y, text=text, fill=selected_color,
                        font=(FONT_NAME, int(font_size_var.get())), tags="watermark")


def move_watermark(event):
    global watermark_x, watermark_y
    if original_image is None:
        return
    watermark_x = event.x
    watermark_y = event.y
    draw_watermark_preview()


def move_up():
    global watermark_y
    watermark_y -= STEP
    draw_watermark_preview()


def move_down():
    global watermark_y
    watermark_y += STEP
    draw_watermark_preview()


def move_left():
    global watermark_x
    watermark_x -= STEP
    draw_watermark_preview()


def move_right():
    global watermark_x
    watermark_x += STEP
    draw_watermark_preview()


def choose_color():
    global selected_color
    color = colorchooser.askcolor()
    if color[1]:
        selected_color = color[1]
        color_swatch.config(bg=selected_color)
        draw_watermark_preview()


def get_font(size):
    for file_name in FONT_FILES:
        try:
            return ImageFont.truetype(file_name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def save_image():
    if original_image is None:
        messagebox.showerror("No image found", "Please select an image first.")
        return

    text = watermark_entry.get().strip()
    if text == "":
        messagebox.showerror("No text found", "Please enter watermark text.")
        return

    # convert the position/size we see on the small preview back to the
    # position/size that matches the full-size original image
    real_x = watermark_x / scale
    real_y = watermark_y / scale
    real_size = int(int(font_size_var.get()) / scale)
    font = get_font(real_size)

    result = original_image.copy()
    draw = ImageDraw.Draw(result)
    draw.text((real_x, real_y), text, font=font, fill=selected_color, anchor="mm")

    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        result.save(save_path)
        messagebox.showinfo("Complete", "Successfully watermarked!")


# ---------- Window ----------
window = Tk()
window.title("IMG Watermark")
window.config(bg=BG, padx=16, pady=10)
window.resizable(False, False)

Label(window, text="IMG · WATERMARK", font=(FONT_NAME, 15, "bold"), fg=TEXT, bg=BG).pack()
Label(window, text="click the image to place your text", font=(FONT_NAME, 8), fg=MUTED, bg=BG).pack(pady=(0, 6))

# canvas + arrow pad sit side by side to save vertical space
preview_row = Frame(window, bg=BG)
preview_row.pack()

canvas = Canvas(preview_row, width=CANVAS_SIZE, height=CANVAS_SIZE, bg=CANVAS_BG,
                 highlightthickness=1, highlightbackground=RULE)
canvas.pack(side="left")
canvas.bind("<Button-1>", move_watermark)
canvas.bind("<B1-Motion>", move_watermark)
show_preview()


def arrow_button(parent, text, command):
    return Button(parent, text=text, font=(FONT_NAME, 10), width=2,
                   fg=TEXT, bg=BG_ELEV, relief="flat", command=command)


arrow_pad = Frame(preview_row, bg=BG)
arrow_pad.pack(side="left", padx=(8, 0))
arrow_button(arrow_pad, "↑", move_up).grid(row=0, column=1)
arrow_button(arrow_pad, "←", move_left).grid(row=1, column=0)
arrow_button(arrow_pad, "→", move_right).grid(row=1, column=2)
arrow_button(arrow_pad, "↓", move_down).grid(row=2, column=1)

controls = Frame(window, bg=BG)
controls.pack(pady=(8, 0))

select_btn = Button(controls, text="1. Select Image", font=(FONT_NAME, 9), width=13,
                     fg=TEXT, bg=BG_ELEV, relief="flat", command=select_image)
select_btn.grid(row=0, column=0, padx=3, pady=3)

watermark_entry = Entry(controls, width=16, font=(FONT_NAME, 9))
watermark_entry.insert(0, "your text here")
watermark_entry.grid(row=0, column=1, padx=3, pady=3)

font_size_var = StringVar(value="36")
size_menu = OptionMenu(controls, font_size_var, *FONT_SIZES)
size_menu.config(font=(FONT_NAME, 8), width=3)
size_menu.grid(row=0, column=2, padx=3, pady=3)

color_btn = Button(controls, text="Color", font=(FONT_NAME, 9), width=7,
                    fg=TEXT, bg=BG_ELEV, relief="flat", command=choose_color)
color_btn.grid(row=1, column=0, padx=3, pady=3)

color_swatch = Label(controls, bg=selected_color, width=3,
                      highlightthickness=1, highlightbackground=RULE)
color_swatch.grid(row=1, column=1, padx=3, pady=3, sticky="w")

save_btn = Button(controls, text="2. Save Image", font=(FONT_NAME, 9, "bold"),
                   fg="#0d1117", bg=YELLOW, relief="flat", command=save_image)
save_btn.grid(row=1, column=2, padx=3, pady=3, sticky="we")

window.mainloop()