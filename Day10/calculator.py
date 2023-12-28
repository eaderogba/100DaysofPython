# calculator
# add
from art import logo


def add(n1, n2):
    return n1 + n2

# subtract


def subtract(n1, n2):
    return n1 - n2

# multiply


def multiply(n1, n2):
    return n1 * n2

# divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for operators in operations:
        print(operators)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick a operation: ")

        num2 = float(input("What is the next number?: "))

        # Optimized. And a smart way to get it done in just 2 lines of code
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
