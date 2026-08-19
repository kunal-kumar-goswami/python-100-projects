from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.color("red")
        self.food.penup()
        self.food.speed(0)
        self.refresh()

    def refresh(self):
        """Refresh food position to a random spot."""
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        self.food.goto(x, y)
