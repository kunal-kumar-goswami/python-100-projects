import turtle
import random

rgb_colors = [
    (239, 244, 245), (250, 231, 234), (245, 243, 239), (237, 240, 243), (231, 245, 237),
    (249, 237, 241), (201, 160, 109), (135, 166, 189), (222, 135, 148), (41, 105, 137),
    (140, 184, 164), (237, 213, 90), (127, 77, 95), (180, 159, 44), (218, 85, 66),
    (51, 111, 91), (145, 80, 55), (14, 97, 74), (181, 186, 210), (25, 87, 110),
    (95, 147, 126), (168, 102, 107), (216, 177, 191), (35, 61, 75), (112, 40, 43),
    (84, 133, 178), (163, 203, 211), (184, 91, 112), (60, 49, 41), (76, 72, 40)
]

turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, 101):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()


