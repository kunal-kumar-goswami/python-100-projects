import art

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operators:
            print(symbol)
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        operation_function = operators.get(operator_symbol)
        if not operation_function:
            print("Invalid operation.")
            continue

        answer = operation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if decision == 'y':
            num1 = answer 
        else:
            should_continue = False
            print("\n" * 3)
            calculator()

calculator()