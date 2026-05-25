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
        if num2 == 0:                                      # This checks to see if num2 is a zero then prints the error message as it is not logical to divide by zero
            print("Error: You cannot divide by zero!")
            result = None 
        else:
            result = num1 / num2 

    if result is not None:
        print(f"Result: {round(result, 3)}")               # Displays the result if valid

    while True:                                            # Asks the user if the want to calculate again or quit
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
