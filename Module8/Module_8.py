# ===============================================================
# Final Project Challenge:
# ===============================================================
# This contains the code I created for the Final Project of the Python course

import math  # Importing math module for factorial


# Function to save each calculation and result into a text file
def save_to_file(operation, result):
    # Open (or create) "calculations.txt" in append mode
    with open("calculations.txt", "a+") as f:
        # Write the operation and its result in an equation format
        f.write(f"{operation} = {result}\n")


# Function to get an integer input from the user
def get_int_from_user(message_displayed):
    user_input = input(message_displayed)
    try:
        # Try converting input to integer
        return int(user_input)
    except:
        # If input is invalid, notify user and return None
        print("Error: Please only use integers")
        return None


# Function to read previously saved calculations from file
def read_calculations():
    try:
        with open("calculations.txt", "r") as f:
            # Return all lines as a list
            return f.readlines()
    except FileNotFoundError:
        # If file does not exist it returns an empty list
        return []


# Main calculator function
def calculator():
    # Greets the user and gets their name capitalising to have good grammar
    name = input("Hello! Please enter your name: ").capitalize()
    print(f"Ok {name}, let's start calculating!")

    # Infinite loop until the user has chosen to exit
    while True:
        # Display menu of options
        print("""\nOptions: 
        1) addition
        2) subtraction
        3) multiplication
        4) division
        5) factorial
        6) exit
        """)

        choice = input("Please choose an operation:\n > ").lower()
        # If the user has chosen to leave
        if choice == "exit" or choice == "6":
            break
        # If the user has chosen to add, divide, subtract or multiply
        elif choice in ["addition", "subtraction", "multiplication", "division", "1", "2", "3", "4"]:
            a = get_int_from_user("Enter first number: ")
            # Restarts the loop if the input was invalid
            if a is None:
                continue
            b = get_int_from_user("Enter second number: ")
            if b is None:
                continue
            if choice == "addition" or choice == "1":
                result = a + b
                operation = f"addition: {a} + {b}"
            elif choice == "subtraction" or choice == "2":
                result = a - b
                operation = f"subtraction: {a} - {b}"
            elif choice == "multiplication" or choice == "3":
                result = a * b
                operation = f"multiplication: {a} * {b}"
            elif choice == "division" or choice == "4":
                if b == 0:
                    print("Error you cannot divide by zero")
                    continue
                else:
                    result = a / b
                    operation = f"division: {a} / {b}"

        # If the user has chosen factorial
        elif choice == "factorial" or choice == "5":
            a = get_int_from_user("Enter number: ")
            if a is None:
                continue
            elif a < 0:
                print("Error you cannot use a negative number")
                continue
            else:
                result = math.factorial(a)
                operation = f"factorial: {a}!"

        # To handle any invalid choices
        else:
            print("Invalid choice, try again.")
            continue

        # Display result and save it to file
        print(f"Result:", result)
        save_to_file(operation, result)

    # When loop exits, say goodbye and show the user's calculation history
    print(f"\nGoodbye, {name}!")
    history = read_calculations()
    print(f"You performed {len(history)} calculations in total:")
    for calc in history:
        print(calc.strip())

if __name__ == "__main__":
    calculator()

