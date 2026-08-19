from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = 10
        self.colors = ["red", "blue", "yellow", "purple", "orange", "green", "pink", "brown"] 

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(self.colors))
            y_pos = random.randint(-250, 250)
            car.goto(300, y_pos)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += 10
