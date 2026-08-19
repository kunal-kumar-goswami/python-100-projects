from turtle import Turtle

FONT = ("Courier New", 16, "normal")
GAME_OVER_FONT = ("Courier New", 26, "bold")
STARTING_LIVES = 3
SCORE_POSITION = (-380, 260)
TEXT_COLOR = "#dbe4ee"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = STARTING_LIVES

        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Score: {self.score}    Lives: {self.lives}",
                    align="left", font=FONT)

    def get_point(self, brick):
        self.score += 1
        self.update_display()

    def lose_life(self):
        self.lives -= 1
        self.update_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)