"""This is a Python program of  avery basic calculator that is able to continue manipulating the current answer
   until the user is done with it and wants to begin a new calculation
"""


#The four functions below are all functions for the four basic arithmetic methods
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

"""This is a dictionary where the key is the arithmetic operator 
and its value is its coresponding function from the four stated above """
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#this is the recursive calculator function
def calculator():

#here the user is asked for the initial number to begin his calculation
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
#"should_continue" will mark whether the user wants to continue solving with the current answer thus keeping the while loop running   
    should_continue = True
    while should_continue:
# user picks the operator they would like to use
        operation_symbol = input("Pick an operation: ")
# user picks the second number 
        num2 = float(input("What is the next number?: "))

        answer = 0
# for each operator chosen, the appropriate function is called
        if operation_symbol == "+":
            answer = add(num1, num2)
        elif operation_symbol == "-":
            answer = subtract(num1 , num2)
        elif operation_symbol == "*":
            answer = multiply(num1, num2)
        else:
            answer = divide(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
 
# this asks if the user would like to continue solving with the current answer

        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if decision == 'y':
            num1 = answer
        else:
            should_continue = False
 #if the user is done, then the function calls itself and starts again 
            calculator()

    
# function call 
calculator()
