#Type Checking 
print(type("Wellcome"))      #string
print(type(123456789))       #integer
print(type(3.1459))          #float
print(type(True))            #boolean

#Conversion of data type string to integer .
#for integer = int() , for string = str(), for float = float(), for boolean = bool()
print(int("356") + int("987"))

#Correcting code
# print("Number of letters in ypur name :" + len(input("Enter  your name")))
your_name = input("Enter your name: ") # it is a string .
name_length = len(your_name)  #it is a integer.
print(" Number of letters in your name:" + str(name_length))