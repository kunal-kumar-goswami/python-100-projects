import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light blue")
screen.title("Turtle Crossing Game")
screen.tracer(0)  

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 290:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
