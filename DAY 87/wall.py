from turtle import Turtle

COLORS = ["green", "yellow",  "red"]
ROWS_PER_COLOR = 2
BRICK_LENGTH = 3     # stretch factor -> 60px wide

START_X = -265
END_X = 300
X_GAP = 65
START_Y = 100
Y_GAP = 25


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()
        self.create_bricks()

    def create_bricks(self):
        y = START_Y

        for color in COLORS:
            for row in range(ROWS_PER_COLOR):
                x = START_X
                y += Y_GAP

                while x < END_X:
                    new_brick = Turtle("square")
                    new_brick.penup()
                    new_brick.shapesize(stretch_wid=1, stretch_len=BRICK_LENGTH)
                    new_brick.color(color)
                    new_brick.goto(x, y)
                    self.all_bricks.append(new_brick)
                    x += X_GAP