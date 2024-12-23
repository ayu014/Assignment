import os

def clear_screen():
    os.system('cls')

def add(first,second):
    '''This function will take the two paramaters and return the addition of it.'''
    #The above line of code is the example of docstring in python.
    return first+second

def minus(first,second):
    return first-second

def multi(first,second):
    return first*second

def divide(first,second):
    return first/second

def expo(first,second):
    return first**second


def calculator():
    should_continue = True
    print(logo)
    first = float(input("What's your first number? "))
    while should_continue:
        print("+\n-\n*\n/\n^\n√")
        operation = input("Pick an operation: ")
        next = float(input("What's your next number? "))
        if operation == '+':
            result = add(first,next)
            print(f"{first} + {next} = {result}")
        elif operation == '-':
            result = minus(first,next)
            print(f"{first} - {next} = {result}")
        elif operation == '*':
            result = multi(first,next)
            print(f"{first} * {next} = {result}")
        elif operation == '/':
            result = divide(first,next)
            print(f"{first} / {next} = {result}")
        elif operation == '^':
            result = expo(first,next)
            print(f"{first} ^ {next} = {result}")
        else:
            print("You chose an invalid operation ")
            quit()


        choice = input(f"Type 'y' to continue calculating with {result} or type'n' to exit or type 's' to start fresh calculation:")
        if choice == 'y':
            first = result
            clear_screen()
            continue
        elif choice=='s':
            clear_screen()
            calculator()
        else:
            should_continue = False
            print("Goodbye!")
            exit()

calculator()
        