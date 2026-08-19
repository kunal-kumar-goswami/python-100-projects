from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_LENGTH = 5     # stretch factor -> 100px wide
SCREEN_EDGE = 380      # keeps the paddle from sliding off either side
PADDLE_COLOR = "#5b9bd5"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_LENGTH)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < SCREEN_EDGE:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -SCREEN_EDGE:
            self.goto(new_x, self.ycor())