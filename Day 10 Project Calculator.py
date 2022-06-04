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
def calculator():

    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = 0
        if operation_symbol == "+":
            answer = add(num1, num2)
        elif operation_symbol == "-":
            answer = subtract(num1 , num2)
        elif operation_symbol == "*":
            answer = multiply(num1, num2)
        else:
            answer = divide(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if decision == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()