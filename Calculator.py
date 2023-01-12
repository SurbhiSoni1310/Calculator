from art import logo
import os

print(logo)
print("Welcome to your personal calculator")


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


operations = {
    '+': add,
    "-": sub,
    "/": divide,
    "*": multiply
}

print("The operations available are : ")
for i in operations:
    print(i + " ", end=" ")
print("\n")
continue_loop = True
num1 = float(input("Enter first number : "))
while continue_loop:
    option = input("Enter the operation you want to perform : ")
    if option not in operations:
        print("Wrong operator. Program terminated")
        exit(1)
    num2 = float(input("What's the next number : "))
    cal_func = operations[option]
    result = cal_func(num1, num2)
    print(f"{num1} {option} {num2} = {result}")
    ask = input(f"Want to continue with the {result} or want to start new calculation. Type 'yes' or 'no' or anything "
                f"to terminate the program : ")
    if ask == "yes":
        num1 = result
    elif ask == "no":
        os.system('cls')
        num1 = int(input("Enter first number : "))
    else:
        print("Program Terminated")
        continue_loop = False
