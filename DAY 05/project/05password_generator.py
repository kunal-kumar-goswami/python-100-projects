#Password Generator
import random

# Lists of letters, numbers, and symbols
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

c = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input for how many of each type
print("Welcome to the PyPassword Generator!")
a1 = int(input("How many letters would you like in your password?\n"))
b1 = int(input("How many symbols would you like?\n"))
c1 = int(input("How many numbers would you like?\n"))

# Pick random characters from each list
password_a = [random.choice(a) for _ in range(a1)]
password_b = [random.choice(c) for _ in range(b1)]
password_c = [random.choice(b) for _ in range(c1)]

# Combine all parts
password = password_a + password_b + password_c

# Shuffle the resulting list to make the password unpredictable
random.shuffle(password)

# Join list into a string
password = ''.join(password)

print(f"Here is your password: {password}")
