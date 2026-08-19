from turtle import *

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(5)

screen.listen()
screen.onkey(key ="s", fun = move_forwards)
screen.exitonclick()