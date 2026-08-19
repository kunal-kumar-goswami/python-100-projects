#Functions with no input.

def greet():
    print("Hello there!")
    print("Welcome to Day 6.")

greet()


#Functions with inputs (parameters).

def greet_with_name(name):
    print(f"Hello {name}!")

greet_with_name("Kunal")


#Functions with outputs (return values).

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 3)
print(result)


#While loop basics.

count = 1
while count <= 5:
    print(count)
    count += 1


#While loop with user input (loop until a condition is met).

number = 0
while number != 7:
    number = int(input("Guess the secret number (1-10): "))
    if number != 7:
        print("Wrong, try again.")

print("You guessed it! The secret number was 7.")