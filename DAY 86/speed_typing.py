from tkinter import *
import pandas
import random

# ---------- Colors (dark theme, matches the other apps) ----------
BG = "#0d1117"
BG_ELEV = "#121926"
TEXT = "#dbe4ee"
MUTED = "#7c8aa0"
BLUE = "#5b9bd5"
YELLOW = "#f4c430"
GREEN = "#5cb98a"
RED = "#e5534b"

FONT_NAME = "Courier New"
TOTAL_TIME = 60          # seconds on the clock
WORD_COUNT = 150          # how many words to load in

# ---------- Game state ----------
correct_words = []
wrong_words = []
time_left = TOTAL_TIME
timer_running = False


def load_words():
    """Read the CSV and drop a random batch of words into the text box."""
    data = pandas.read_csv("c:/coding-programming/100 Days of Code/DAY 86/common_english_words.csv")
    word_list = data["Common Words"].tolist()
    words_to_type = [random.choice(word_list) for _ in range(WORD_COUNT)]

    text_widget.delete("1.0", END)
    text_widget.insert("1.0", " ".join(words_to_type))
    highlight_current_word()


def highlight_current_word():
    """Highlight the word sitting at the very start of the text box."""
    text_widget.tag_remove("current", "1.0", END)
    end_of_word = text_widget.search(" ", "1.0", stopindex="end")
    if end_of_word:
        text_widget.tag_add("current", "1.0", end_of_word)
        text_widget.tag_config("current", background=BLUE, foreground=BG)


def check_word(event):
    global timer_running

    if not timer_running:
        return

    if event.keysym != "space":
        return

    typed_word = user_entry.get().strip()
    content = text_widget.get("1.0", "end-1c")
    target_word = content.split()[0] if content.split() else ""

    if typed_word == target_word:
        correct_words.append(typed_word)
    else:
        wrong_words.append(typed_word)

    # remove the word (plus its trailing space) we just checked
    text_widget.delete("1.0", f"1.{len(target_word) + 1}")
    highlight_current_word()
    user_entry.delete(0, END)


def start_timer():
    global time_left, timer_running
    timer_running = True

    if time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        time_label.config(text=f"Time Left: {minutes:02d}:{seconds:02d}")
        time_left -= 1
        window.after(1000, start_timer)
    else:
        timer_running = False
        show_results()


def show_results():
    total_chars = sum(len(word) for word in correct_words)
    words_per_minute = total_chars / 5   # standard WPM formula, TOTAL_TIME is 1 minute

    cpm_label.config(text=f"Characters Per Minute: {total_chars}")
    wpm_label.config(text=f"Words Per Minute: {words_per_minute:.0f}")
    errors_label.config(text=f"Total Errors: {len(wrong_words)}")

    text_widget.delete("1.0", END)
    text_widget.insert(
        "1.0",
        f"Time's up!\n\n"
        f"Words Per Minute: {words_per_minute:.0f}\n"
        f"Characters Per Minute: {total_chars}\n"
        f"Total Errors: {len(wrong_words)}",
    )


def restart_test():
    global correct_words, wrong_words, time_left, timer_running

    correct_words = []
    wrong_words = []
    time_left = TOTAL_TIME
    timer_running = False

    user_entry.delete(0, END)
    time_label.config(text=f"Time Left: 01:00")
    cpm_label.config(text="Characters Per Minute: 0")
    wpm_label.config(text="Words Per Minute: 0")
    errors_label.config(text="Total Errors: 0")

    load_words()
    start_timer()


# ---------- Window ----------
window = Tk()
window.title("Speed Typing Test")
window.config(bg=BG, padx=24, pady=18)
window.resizable(False, False)

Label(window, text="SPEED · TYPING · TEST", font=(FONT_NAME, 18, "bold"),
      fg=TEXT, bg=BG).grid(row=0, column=0, columnspan=2, pady=(0, 4))
Label(window, text="type each highlighted word, then press space", font=(FONT_NAME, 9),
      fg=MUTED, bg=BG).grid(row=1, column=0, columnspan=2, pady=(0, 12))

text_widget = Text(window, height=6, width=40, wrap="word", font=(FONT_NAME, 13),
                    bg=BG_ELEV, fg=TEXT, insertbackground=TEXT, relief="flat",
                    padx=12, pady=12)
text_widget.grid(row=2, column=0, pady=(0, 12))

stats = Frame(window, bg=BG)
stats.grid(row=2, column=1, sticky="n", padx=(16, 0))

time_label = Label(stats, text="Time Left: 01:00", font=(FONT_NAME, 11), fg=BLUE, bg=BG)
time_label.pack(anchor="w", pady=4)

cpm_label = Label(stats, text="Characters Per Minute: 0", font=(FONT_NAME, 10), fg=MUTED, bg=BG)
cpm_label.pack(anchor="w", pady=4)

wpm_label = Label(stats, text="Words Per Minute: 0", font=(FONT_NAME, 10), fg=MUTED, bg=BG)
wpm_label.pack(anchor="w", pady=4)

errors_label = Label(stats, text="Total Errors: 0", font=(FONT_NAME, 10), fg=RED, bg=BG)
errors_label.pack(anchor="w", pady=4)

user_entry = Entry(window, width=40, font=(FONT_NAME, 12), bg=BG_ELEV, fg=TEXT,
                    insertbackground=TEXT, relief="flat")
user_entry.grid(row=3, column=0, pady=6, ipady=6)
user_entry.bind("<KeyRelease>", check_word)
user_entry.focus()

restart_btn = Button(window, text="Restart", font=(FONT_NAME, 10, "bold"), fg="#0d1117",
                      bg=YELLOW, relief="flat", padx=14, pady=6, command=restart_test)
restart_btn.grid(row=3, column=1, pady=6, sticky="e")

load_words()
start_timer()

window.mainloop()