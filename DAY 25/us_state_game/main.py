import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/coding-programming/100 Days of Code/DAY 25/us_state_game/states.gif"  
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("C:/coding-programming/100 Days of Code/DAY 25/us_state_game/50_states.csv") 
all_states = states_data.state.to_list() 

guessed_states = []

def display_guesses():
    screen.clear()
    screen.bgcolor("white")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write(f"Congratulations! You guessed {len(guessed_states)}/50 states correctly.", align="center", font=("Arial", 16, "normal"))
    turtle.goto(0, -100)
    turtle.write("Thanks for playing! Press 'Enter' to quit.", align="center", font=("Arial", 12, "normal"))
    turtle.hideturtle()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)       
        new_data.to_csv("state_you_missed.csv")
        break


    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        state_data = states_data[states_data.state == answer_state]
        x = state_data.x.item()
        y = state_data.y.item()

        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x, y)
        state_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))

display_guesses()

turtle.done()
