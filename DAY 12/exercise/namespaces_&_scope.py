enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")


increase_enemies()
print(f"enemies outside function : {enemies}")


#Local Scope
def my_function():
    my_local_var = 2

    print(my_local_var) 
 
my_function()

#Global Scope
my_global_var = 3

def my_function():
    print(my_global_var)


my_function()
print(my_global_var)

