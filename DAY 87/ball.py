from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
RESET_Y_POSITION = -230
BALL_COLOR = "#f4c430"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = STARTING_MOVE_DISTANCE
        self.y_move = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, RESET_Y_POSITION)
        self.y_move = STARTING_MOVE_DISTANCE
        # send it off in a random left/right direction each time it resets
        self.x_move = STARTING_MOVE_DISTANCE * random.choice([1, -1])