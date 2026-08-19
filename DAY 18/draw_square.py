from turtle import Turtle, Screen

tom_turtle = Turtle()

for i in range(4):
    tom_turtle.forward(180)
    tom_turtle.right(90)

screen = Screen()
screen.exitonclick()