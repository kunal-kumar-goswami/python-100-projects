from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0.1)
    return screen

def start_game():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_running = True
    while game_running:
        screen.update()
        time.sleep(0.1)

        snake.move()

        if snake.head.distance(food.food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.increase_score()

        if abs(snake.head.xcor()) > 390 or abs(snake.head.ycor()) > 290:
            time.sleep(0.5)
            scoreboard.reset()
            snake.reset()
            food.refresh()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                time.sleep(0.5)
                scoreboard.reset()
                snake.reset()
                food.refresh()
                break

screen = setup_screen()
start_game()
screen.mainloop()
