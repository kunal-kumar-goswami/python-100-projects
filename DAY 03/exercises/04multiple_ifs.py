#Movie Ticket Pricing + Rating feedback
print("Welcome to the movie theater!")
age = int(input("What is your age? "))

if age >= 0:
    if age < 5:
        print("You get in for free!")
    else:
        if age < 13:
            print("Child ticket: $5")
        elif age < 18:
            print("Teen ticket: $7")
        elif age < 60:
            print("Adult ticket: $10")
        else:
            print("Senior ticket: $6")
    movie_rating = input("Enter the movie rating Good / Bad :")
    if movie_rating == "good ":
        print("Thanks You! Come Again. ")
    else:
        print("Ok thanks for watching ")
else:
    print("Invalid age entered.")
