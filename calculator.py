# Python Practices
# Calculator 
# A basic calculator that asks for two numbers and an operator, performs the chosen calculation and then displays the result.
# Once the result is displayed, the user is then given the option to either perform another calculation or to quit

while True:
    while True:                                                             # This block validates the first number input and prompts the user to try again if unacceptable input is entered
        try:
            num1 = float(input("Enter the first number: "))                 # Changed the typecast method from an integer to a float to allow decimal numbers and not just whole numbers
            break 
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break 
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    while True:
        operator = input("Choose an operator (+, -, *, /: ").strip()        # This block validates the operator input and prompts the user to try again if a valid operator is not entered
        if operator in ("+", "-", "*", "/"):
            break 
        print(f"'{operator}' is not a valid operator! Please choose from +, -, *, /")

    if operator == "+":                                    # This block performs the calculation based on the chosen operator
        result = num1 + num2 
    elif operator == "-":
        result = num1 - num2 
    elif operator == "*":
        result = num1 * num2 
    elif operator == "/":
        while True:                                        # This while loop and try/except block check to see if the user enters a zero. If this is the case, the error message is displayed and the user is prompted to enter any number other than zero
            try:
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
                break 
            except ZeroDivisionError:
                print("Error: You cannot divide by zero!")
                while True:
                    try:
                        num2 = float(input("Please enter a number that is not zero: "))
                        break 
                    except ValueError:
                        print("Invalid input! Please enter numbers only.")                                     
            
    if result is not None:
        print(f"Result: {round(result, 3)}")               # Displays the result if valid

    while True:                                            # Asks the user if they want to calculate again or quit
        choice = input("\nWould you like to perform another calculation or quit? (calculate/quit): ").strip().lower()
        if choice == "quit":
            print("Goodbye!")
            break 
        elif choice == "calculate":
            break 
        else:
            print("Invalid choice! Please either type 'calculate' or 'quit'.")

    if choice == "quit":                                   # Breaks the outer loop if user chooses to quit
        break 
