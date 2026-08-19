import random
from art import logo 


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5 

# Generate random number
num = random.randint(1, 100)

# Function to set difficulty
def difficulty_level():
    level = input("Choose a level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN

# Function to check user guess against actual answer
def check_answer(guess, num):
    if guess > num:
        print("Too high.")
        return False
    elif guess < num:
        print("Too low.")
        return False
    else:
        print(f"Correct! You guessed it right 👍. The number was {num}.")
        return True
 
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    turns = difficulty_level()
    guess = None

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining.")
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if check_answer(guess, num):
            break
        turns -= 1

    if turns == 0 and guess != num:
        print(f"Sorry, you're out of guesses. The number was {num}.")

game()
