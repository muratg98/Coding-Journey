import calculatorart
from calculatorart import logo
print(logo)

# get first number
# get operation (+, -, *, /)
# get second number
# give option to continue calculating with current calc or start new one

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator ():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_continue = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit")
        if user_continue == 'y':
            num1 = answer
        elif user_continue == 'n':
            should_continue = False
            calculator() #this is recursion -> function that calls itself, used to start a new calculation
calculator()

