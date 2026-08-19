#Display Art
from art import logo, vs
from data import data
import random

# Formatting account data into printable format.
def formating_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, follower_count_01, follower_count_02):
    if follower_count_01 > follower_count_02:
        return user_guess == "1"
    else:
        return user_guess == "2"

print(logo)
score = 0
game_continue = True
account_2 = random.choice(data)

# Generate a random account from the data.
while game_continue:
    account_1 = account_2
    account_2 = random.choice(data)
    if account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare 1: {formating_data(account_1)}.")
    print(vs)
    print(f"Against 2: {formating_data(account_2)}.")

    # Asking user to guess.
    valid_input = False
    while not valid_input:
        guess = input("Who has more followers? Type '1' or '2': ")
        if guess == '1' or guess == '2':
            valid_input = True
        else:
            print("Invalid input. Please type '1' or '2'.")

    print("\n" * 20)
    print(logo)

    # Checking if the user is correct.
    # Get follower count for each account.
    follower_count_01 = account_1["follower_count"]
    follower_count_02 = account_2["follower_count"]
    correct = check_answer(guess, follower_count_01, follower_count_02)

    # Use if statement to check if the user is correct.
    if correct:
        score += 1
        print(f"***** You are Right! Your score is {score}. *****")
    else:
        print(f"***** Sorry, that is wrong. Final score: {score}. *****")
        game_continue = False

