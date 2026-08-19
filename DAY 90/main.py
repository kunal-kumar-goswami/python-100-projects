from tkinter import *
import time
import tkinter.messagebox


BACKGROUND_COLOR = "#0B1220"
CARD_COLOR = "#111C2E"
TEXT_COLOR = "#F8FAFC"
SECONDARY_TEXT = "#94A3B8"
ACCENT_COLOR = "#38BDF8"
ACCENT_HOVER = "#0EA5E9"
SUCCESS_COLOR = "#22C55E"
DANGER_COLOR = "#EF4444"
BORDER_COLOR = "#1E293B"
TEXT_AREA_COLOR = "#0F172A"


MAX_LINE_LENGTH = 35

instructions = "Don't stop writing or your text will disappear!"
countdown_time = 10


def countdown():
    global timer_running, popup_shown

    time_elapse = int(check_elapsed_time())
    if time_elapse > 5:

        remaining_time = countdown_time - time_elapse

        if remaining_time >= 0:
            time_label.config(
                text=f"TIME LEFT :  {remaining_time:02d}",
                fg=ACCENT_COLOR
            )

        else:

            if not popup_shown:
                popup_shown = True
                prompt_save_or_delete()

            time_label.config(
                text="TIME'S UP!",
                fg=DANGER_COLOR
            )

            timer_running = False
            return

    else:

        time_label.config(
            text="●  KEEP WRITING...",
            fg=SUCCESS_COLOR
        )

    window.after(1000, countdown)


def on_key_release(event):
    """Record the time when a key is released and start the timer."""

    global last_key_release_time
    global timer_running
    global popup_shown

    last_key_release_time = time.time()

    if not timer_running:
        timer_running = True
        popup_shown = False
        countdown()


def on_key_press(event):
    global timer_running

    # Stop the timer when a key is pressed
    timer_running = False


def check_elapsed_time():

    global last_key_release_time

    elapsed_time = time.time() - last_key_release_time

    return elapsed_time


def prompt_save_or_delete():

    text = text_widget.get("1.0", "end-1c")

    text_widget.delete("1.0", END)

    if tkinter.messagebox.askyesno(
            "Time's Up!",
            "Your text is about to disappear.\n\n"
            "Do you want to save it?"
    ):
        save_text(text)

    else:
        delete_text()


def save_text(text):

    with open("test.txt", "w") as text_file:
        text_file.write(text)


def delete_text():

    with open("test.txt", "w") as text_file:
        text_file.write("")


def restart():

    global last_key_release_time
    global timer_running
    global popup_shown

    text_widget.delete("1.0", END)

    time_label.config(
        text="READY  •  START WRITING",
        fg=SECONDARY_TEXT
    )

    last_key_release_time = 0
    timer_running = False
    popup_shown = False

    delete_text()



window = Tk()

window.title(" Disappearing Text")

window.geometry("850x600")

window.minsize(700, 520)

window.config(
    padx=45,
    pady=25,
    bg=BACKGROUND_COLOR
)


last_key_release_time = 0

timer_running = False

popup_shown = False



header_label = Label(
    window,
    text="Disappearing Text",
    font=("Segoe UI", 34, "bold"),
    fg=TEXT_COLOR,
    bg=BACKGROUND_COLOR
)

header_label.grid(
    column=0,
    row=0,
    pady=(10, 5)
)


# Subtitle

instructions_label = Label(
    window,
    text=instructions,
    font=("Segoe UI", 14),
    fg=SECONDARY_TEXT,
    bg=BACKGROUND_COLOR
)

instructions_label.grid(
    column=0,
    row=1,
    pady=(0, 20)
)



editor_frame = Frame(
    window,
    bg=CARD_COLOR,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)

editor_frame.grid(
    column=0,
    row=2,
    padx=10,
    pady=10,
    sticky="nsew"
)


# Editor title

editor_title = Label(
    editor_frame,
    text="WRITE SOMETHING",
    font=("Segoe UI", 11, "bold"),
    fg=ACCENT_COLOR,
    bg=CARD_COLOR
)

editor_title.pack(
    anchor="w",
    padx=25,
    pady=(20, 5)
)


text_widget = Text(
    editor_frame,
    height=12,
    width=50,
    wrap="word",

    font=("Segoe UI", 19),

    bg=TEXT_AREA_COLOR,

    fg=TEXT_COLOR,

    insertbackground=ACCENT_COLOR,

    selectbackground=ACCENT_COLOR,

    selectforeground=BACKGROUND_COLOR,

    bd=0,

    relief="flat",

    padx=20,

    pady=20
)

text_widget.pack(
    padx=20,
    pady=(5, 20),
    fill="both",
    expand=True
)


# Bind keyboard events

text_widget.bind(
    "<KeyRelease>",
    on_key_release
)

text_widget.bind(
    "<KeyPress>",
    on_key_press
)


time_label = Label(
    window,

    text="READY  •  START WRITING",

    font=("Segoe UI", 12, "bold"),

    fg=SECONDARY_TEXT,

    bg=BACKGROUND_COLOR
)

time_label.grid(
    column=0,
    row=3,
    pady=(10, 20)
)


button_frame = Frame(
    window,
    bg=BACKGROUND_COLOR
)

button_frame.grid(
    column=0,
    row=4,
    pady=(0, 20)
)


save = Button(
    button_frame,

    text="SAVE FILE",

    font=("Segoe UI", 11, "bold"),

    fg=TEXT_COLOR,

    bg=ACCENT_COLOR,

    activebackground=ACCENT_HOVER,

    activeforeground=TEXT_COLOR,

    relief="flat",

    bd=0,

    cursor="hand2",

    padx=30,

    pady=12,

    command=lambda: save_text(
        text_widget.get("1.0", "end-1c")
    )
)

save.pack(
    side=LEFT,
    padx=8
)


restart_button = Button(
    button_frame,

    text="RESTART",

    font=("Segoe UI", 11, "bold"),

    fg=TEXT_COLOR,

    bg=BORDER_COLOR,

    activebackground="#334155",

    activeforeground=TEXT_COLOR,

    relief="flat",

    bd=0,

    cursor="hand2",

    padx=30,

    pady=12,

    command=restart
)

restart_button.pack(
    side=LEFT,
    padx=8
)


footer_label = Label(
    window,

    text="Focus • Write • Don't Stop",

    font=("Segoe UI", 10),

    fg="#64748B",

    bg=BACKGROUND_COLOR
)

footer_label.grid(
    column=0,
    row=5,
    pady=(5, 0)
)


window.grid_columnconfigure(
    0,
    weight=1
)

window.grid_rowconfigure(
    2,
    weight=1
)

window.mainloop()