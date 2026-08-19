from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-75, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(75, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
