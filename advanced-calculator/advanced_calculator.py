print("Calculator")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input - please enter numbers only")
    exit()

operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: You cannot divide by zero")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operation")
    result = None

if result is not None:
    print("Result:", result)
