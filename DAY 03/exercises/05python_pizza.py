#Pizz cafe - order calculator 
print("Welcome to Python Pizza Cafe")

size = input("Which size do you wamt? quater = Q , half = H, full = F : ")
need1 = input("Do you want pepperoni ? Y or N :")
need2 = input("Do you need extra cheese?  Y or N :")

your_bill = 0 
if size == "Q":
   your_bill += 15
elif size == "H"   :
   your_bill += 20
elif size == "F"   :
   your_bill += 25
else:
   print("invalid input")   

if need1 ==  "Y":
   if size == "Q":
      your_bill += 2
   else:
      your_bill +=3
   
if need2 =="Y"   :
   your_bill +=3

print(f"Your Total Bill is :$ {your_bill}")   