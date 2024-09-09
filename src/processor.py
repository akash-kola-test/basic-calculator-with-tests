from interface import display_menu, get_user_input
from handlers import operation_handlers

def calculation_processor():
    display_menu()
    num1, num2, operation = get_user_input()

    try:
        num1, num2, operation = int(num1), int(num2), int(operation)
    except Exception as e:
        print("invalid inputs")
        return

    handler = operation_handlers.get(operation)

    if operation == 4:
        print(handler())
        return operation

    if handler == None:
        print("Invalid operation choice.")
        return

    print(handler(num1, num2))

