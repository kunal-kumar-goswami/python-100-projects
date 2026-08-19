#tip calculator 

print("Welcome to the tip calculator!.🧮")

your_bill = float(input(" What's your total bill? $"))
given_tip = int(input("What % of tip you will give ? 10 12 15: "))
no_people = int(input("How many people are you spliting the bill? "))

bill = your_bill * (1 + given_tip/ 100)
total_bill = bill / no_people
final_bill = round(total_bill, 2)
print(f" Each person should pay: ${final_bill}")
