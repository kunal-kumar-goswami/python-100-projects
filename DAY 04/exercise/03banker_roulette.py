import random
boys = ["Suraj", "Sagar", "Deepak", "Rohit", "Avinash"]

#1st method 
print( random.choice(boys))

#2nd method
x = random.randint(0 , 4)
print(boys[x])
