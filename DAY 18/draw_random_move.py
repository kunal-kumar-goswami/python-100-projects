from turtle import *
import random 

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "saddle brown", "SlateGrey", "SeaGreen"]

def random_color():
    r= random.randint(0, 250)
    g= random.randint(0, 250)
    b= random.randint(0, 250)
    random.color = (r,g,b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(500):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
screen = Screen()
screen.exitonclick()

