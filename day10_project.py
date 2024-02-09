# Calculator Program

# Add Function
def add(n1: float, n2: float):
    return n1 + n2

# Substract Function
def substract(n1: float, n2: float):
    return n1 - n2

# Multiply Function
def multiply(n1: float, n2: float):
    return n1 * n2

# Divide Function
def divide(n1: float, n2: float):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    op = input("Pick an operation from the symbols above: ")
    num2 = float(input("What is the second number? "))

    answer_func = operations[op]
    answer = answer_func(n1=num1, n2=num2)
    print(f"{num1} {op} {num2} = {answer}")

    loop = True
    while loop:
        loop_state = input(f"Type 'y' to continue calculating with {answer}, or type 'a' to start anew, or type 'N' to exit: ")
        if loop_state == "y":
            new_op = input("Pick an operation: ")
            num3 = float(input("What is the new number? "))
            answer_func = operations[new_op]
            new_answer = answer_func(n1=answer, n2=num3)
            print(f"{answer} {new_op} {num3} = {new_answer}")
            answer = new_answer
        elif loop_state == "a":
            loop = False
            calculator()
        elif loop_state ==  "N":
            loop = False

calculator()
