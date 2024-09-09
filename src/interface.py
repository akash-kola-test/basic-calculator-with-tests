def display_menu():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

def get_user_input():
    num1, num2 = 0, 0
    operation = input("Choose operation (1-4): ")
    if int(operation) != 4:
        num1 = input("Enter the first positive integer: ")
        num2 = input("Enter the second positive integer: ")
    return num1, num2, operation
