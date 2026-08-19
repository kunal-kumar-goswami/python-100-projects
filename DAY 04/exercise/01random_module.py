#To use any module we have to first import that.
#using random module
import random 

random_number = random.randint(1 , 100)
print(random_number)

#To generate floating number .
decimal_0_to_1 = random.random() 
print(decimal_0_to_1)

floating_no = random.uniform(1 , 10)
print(floating_no)

#Heads and Tails 
coin = random.randint(0, 1)
if coin == 0 :
    print("Heads")
else:
    print("Tails")    