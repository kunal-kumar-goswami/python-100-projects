from turtle import *

class Scoreboard:
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.display = Turtle()  
        self.display.color("white")
        self.display.penup()
        self.display.goto(0, 260)
        self.display.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.display.clear()  
        self.display.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0  
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def set_high_score(self, score):
        self.high_score = score
        self.update_scoreboard()

    def set_current_score(self, score):
        self.score = score
        self.update_scoreboard()

    def game_over(self):
        """Display the Game Over message."""
        self.display.goto(0, 0)  
        self.display.clear()  
        self.display.write("GAME OVER", align="center", font=("Arial", 36, "normal"))
        self.display.goto(0, -40) 
        self.display.write(f"Final Score: {self.score}\nHigh Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))