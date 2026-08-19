import turtle as t
import random 

tim = t.Turtle()
t.colormode(255)

def random_color():
    r= random.randint(0, 250)
    g= random.randint(0, 250)
    b= random.randint(0, 250)
    color = (r,g,b)
    return color

tim.speed("fastest")

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading( tim.heading() + size_of_gap)

spirograph(4)

screen = t.Screen()
screen.exitonclick()
