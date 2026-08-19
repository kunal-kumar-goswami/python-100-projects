#Movie Ticket Pricing ( nested conditions )
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
else:
    print("Invalid age entered.")
