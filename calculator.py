def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    
    return num1 / num2  


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /): ")

        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")


def calculate(num1, operation, num2):
    if operation == "+":
        return addition(num1, num2)
    elif operation == "-":
        return subtraction(num1, num2)
    elif operation == "*":
        return multiplication(num1, num2)
    elif operation == "/":
        return division(num1,num2)


def show_history(history):
    print("\nCalculation History:")

    if not history:
        print("No calculations yet.")
    else:
        for calculation in history:
            print(calculation)


def show_menu():
    print("Calculator Menu:")
    print("1. Continue")
    print("2. View Calculation History")
    print("3. Clear History")
    print("4. Exit")


def get_menu_choice():
    while True:
        show_menu()

        choice = input("Choose an option (1-4): ")

        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def save_history(calculation):
    with open("history.txt", "a") as file:
        file.write(calculation + "\n")


def load_history():
    history = []

    try:
        with open("history.txt", "r") as file:

            for line in file:
                history.append(line.strip())

    except FileNotFoundError:
        pass

    return history


def clear_history():
    with open("history.txt", "w") as file:
        pass


history = load_history()


running = True
while running:
    num1 = get_number("Enter first number: ")

    operation = get_operation()

    num2 = get_number("Enter second number: ")

    try:
        result = calculate(num1, operation, num2)

    except ZeroDivisionError as error:
        print("Error:", error)
        print("Calculation was not saved to history.")
        continue

    calculation = f"{num1} {operation} {num2} = {result}"

    history.append(calculation)
    save_history(calculation)

    print("Result:", result)


    while True:
        choice = get_menu_choice()

        if choice == "1":
            break

        elif choice == "2":
            show_history(history)

        elif choice == "3":
            history.clear()
            clear_history()
            print("Calculation history cleared.")
        
        elif choice == "4":
            running = False
            break

show_history(history)