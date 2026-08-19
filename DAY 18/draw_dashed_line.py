from turtle import *

king = Turtle()

for _ in range(20):
    king.forward(5)
    king.penup()
    king.forward(5)
    king.pendown()
    king.color("green")
  
screen = Screen()
screen.exitonclick()
