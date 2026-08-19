from turtle import *

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(5)

def move_backwards():
    tom.backward(10)

def move_left():
    h = tom.heading() + 10
    tom.setheading(h)

def move_right():
    h = tom.heading() - 10
    tom.setheading(h)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey( move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey( move_left, "a")
screen.onkey( move_right, "d")
screen.onkey( clear, "c")
screen.exitonclick()
clear()
