#summing & finding the maximum
bills = [12,45,90,23,88,18,56,92,45,32,10]

total_bill = sum(bills)

sum = 0
for bill in bills :
    sum += bill

print(sum)                     # adding all collection in list 
print(max(bills))              #highest in list - 1st method 

max_bill = 0                   #2nd method 
for bill in bills :
    if bill > max_bill:
        max_bill = bill

print(max_bill)

