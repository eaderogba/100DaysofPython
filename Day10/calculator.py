# calculator
# add
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

num1 = int(input("What is the first number?: "))


for operators in operations:
    print(operators)

operation_symbol = input("Pick a operation from the line above: ")

num2 = int(input("What is the second number?: "))

"""Here is what i first thought of to do the arithmetic after the user enters num1 and num2

if operation_symbol == "+":
    answer = add(num1, num2)
elif operation_symbol == "-":
    answer = subtract(num1, num2)
elif operation_symbol == "*":
    answer = multiply(num1, num2)
elif operation_symbol == "/":
    answer = divide(num1, num2)"""

# Optimized. And a smart way to get it done in just 2 lines of code
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
