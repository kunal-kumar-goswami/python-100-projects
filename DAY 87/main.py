from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time

# ---------- Screen setup ----------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_SPEED = 0.1        # lower = faster game loop

# ---------- Playing field boundaries ----------
LEFT_WALL = -380
RIGHT_WALL = 380
TOP_WALL = 280
OUT_OF_BOUNDS_Y = -280      # ball fell past the paddle -> lose a life

PADDLE_HIT_DISTANCE = 40
BRICK_HIT_DISTANCE = 35

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Breakout Game")
screen.tracer(0)

# ---------- Create game objects ----------
score = Scoreboard()
paddle = Paddle((0, -250))
ball = Ball()
bricked_wall = Wall()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(GAME_SPEED)
    screen.update()
    ball.move()

    # bounce off the left/right screen edges
    if ball.xcor() < LEFT_WALL or ball.xcor() > RIGHT_WALL:
        ball.bounce_x()

    # bounce off the top wall
    if ball.ycor() > TOP_WALL:
        ball.bounce_y()

    # bounce off the paddle
    if ball.distance(paddle) < PADDLE_HIT_DISTANCE and ball.ycor() < -240:
        ball.bounce_y()

    # check for collisions with bricks
    # loop over a copy of the list since we remove bricks while looping
    for brick in bricked_wall.all_bricks[:]:
        if ball.distance(brick) < BRICK_HIT_DISTANCE:
            brick.hideturtle()
            bricked_wall.all_bricks.remove(brick)
            ball.bounce_y()
            score.get_point(brick)

    if not bricked_wall.all_bricks:
        game_is_on = False
        score.game_over()

    # ball fell below the paddle
    if ball.ycor() < OUT_OF_BOUNDS_Y:
        ball.reset_position()
        score.lose_life()

    if score.lives == 0:
        game_is_on = False
        score.game_over()

screen.exitonclick()
