from turtle import *
import random 

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid","IndianRed", "DeepSkyBlue","LightSeaGreen", "saddle brown", "SlateGrey", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
      tim.forward(80)
      tim.right(angle)

for shape_side_n in range(3, 11):
   tim.color(random.choice(colours))
   draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()

