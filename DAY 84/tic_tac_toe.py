from tkinter import *

# ---------- Colors (dark theme) ----------
BG = "#0d1117"
BG_ELEV = "#121926"
CELL_BG = "#161f2e"
CELL_HOVER = "#1c2740"
RULE = "#212b3a"
TEXT = "#dbe4ee"
MUTED = "#7c8aa0"
BLUE = "#5b9bd5"    # X
YELLOW = "#f4c430"  # O
GREEN = "#5cb98a"   # win highlight

# ---------- Constants ----------
CELL_SIZE = 100
PAD = 22

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]

# ---------- Game state ----------
board = ["" for _ in range(9)]
cells = []
current_player = "X"
game_over = False
scores = {"X": 0, "O": 0, "Ties": 0}


def draw_mark(i, mark):
    canvas = cells[i]
    canvas.config(bg=CELL_BG)
    p = PAD
    s = CELL_SIZE

    if mark == "X":
        canvas.create_line(p, p, s - p, s - p, fill=BLUE, width=6, capstyle="round")
        canvas.create_line(s - p, p, p, s - p, fill=BLUE, width=6, capstyle="round")
    else:
        canvas.create_oval(p, p, s - p, s - p, outline=YELLOW, width=6)


def check_winner():
    for a, b, c in WIN_COMBOS:
        if board[a] and board[a] == board[b] == board[c]:
            return (a, b, c)
    return None


def end_game(winner, combo):
    global game_over
    game_over = True

    if winner:
        for i in combo:
            cells[i].config(bg=GREEN)
        scores[winner] += 1
        status_label.config(text=f"{winner} wins!", fg=GREEN if winner == "X" else YELLOW)
        score_labels[winner].config(text=str(scores[winner]))
    else:
        scores["Ties"] += 1
        status_label.config(text="it's a tie", fg=MUTED)
        score_labels["Ties"].config(text=str(scores["Ties"]))

    replay_button.pack(pady=(0, 16))


def update_turn_label():
    turn_label.config(
        text=f"turn:  {current_player}",
        fg=BLUE if current_player == "X" else YELLOW,
    )


def on_click(i):
    global current_player

    if game_over or board[i]:
        return

    board[i] = current_player
    draw_mark(i, current_player)

    combo = check_winner()
    if combo:
        end_game(winner=current_player, combo=combo)
    elif "" not in board:
        end_game(winner=None, combo=None)
    else:
        current_player = "O" if current_player == "X" else "X"
        update_turn_label()


def on_hover(i, entering):
    if board[i] or game_over:
        return
    cells[i].config(bg=CELL_HOVER if entering else CELL_BG)


def reset_board():
    global board, current_player, game_over

    board = ["" for _ in range(9)]
    current_player = "X"
    game_over = False

    status_label.config(text=" ")
    replay_button.pack_forget()

    for canvas in cells:
        canvas.delete("all")
        canvas.config(bg=CELL_BG)

    update_turn_label()


def reset_scores():
    scores["X"] = 0
    scores["O"] = 0
    scores["Ties"] = 0
    for key in score_labels:
        score_labels[key].config(text="0")
    reset_board()


# ---------- Window ----------
window = Tk()
window.title("Tic Tac Toe")
window.config(bg=BG, padx=20, pady=14)
window.resizable(False, False)

# ---------- Header ----------
Label(window, text="TIC · TAC · TOE", font=("Courier New", 18, "bold"), fg=TEXT, bg=BG).pack()
Label(window, text="two players, one board", font=("Courier New", 9), fg=MUTED, bg=BG).pack(pady=(0, 10))

# ---------- Scoreboard ----------
score_bar = Frame(window, bg=BG_ELEV, highlightbackground=RULE, highlightthickness=1)
score_bar.pack(fill="x", pady=(0, 8))

score_labels = {}
for key, color in (("X", BLUE), ("Ties", MUTED), ("O", YELLOW)):
    cell = Frame(score_bar, bg=BG_ELEV)
    cell.pack(side="left", expand=True, fill="both", pady=6)
    Label(cell, text=key, font=("Courier New", 9), fg=MUTED, bg=BG_ELEV).pack()
    lbl = Label(cell, text="0", font=("Courier New", 14, "bold"), fg=color, bg=BG_ELEV)
    lbl.pack()
    score_labels[key] = lbl

turn_label = Label(window, font=("Courier New", 10), fg=BLUE, bg=BG)
turn_label.pack(pady=(0, 6))
update_turn_label()

# ---------- Grid ----------
grid_frame = Frame(window, bg=RULE)
grid_frame.pack()

for i in range(9):
    row, col = divmod(i, 3)
    canvas = Canvas(grid_frame, width=CELL_SIZE, height=CELL_SIZE, bg=CELL_BG,
                     highlightthickness=1, highlightbackground=RULE, bd=0)
    canvas.grid(row=row, column=col, padx=1, pady=1)
    canvas.bind("<Button-1>", lambda event, i=i: on_click(i))
    canvas.bind("<Enter>", lambda event, i=i: on_hover(i, True))
    canvas.bind("<Leave>", lambda event, i=i: on_hover(i, False))
    cells.append(canvas)

# ---------- Status + replay ----------
status_label = Label(window, text=" ", font=("Courier New", 11, "bold"), fg=GREEN, bg=BG)
status_label.pack(pady=(10, 0))

replay_button = Button(window, text="play again", font=("Courier New", 9), fg=TEXT,
                        bg=BG_ELEV, activebackground=RULE, activeforeground=TEXT,
                        relief="flat", padx=12, pady=4, command=reset_board)
# not packed yet - only shown once a round ends

# ---------- Menu ----------
menu_bar = Menu(window)
window.config(menu=menu_bar)

game_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Game", menu=game_menu)
game_menu.add_command(label="New Round", command=reset_board)
game_menu.add_command(label="Reset Scores", command=reset_scores)
game_menu.add_separator()
game_menu.add_command(label="Quit", command=window.destroy)

window.mainloop()