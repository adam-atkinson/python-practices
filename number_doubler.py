# Python Practices
# Number Doubler
# This program asks the user for a number and then multiplies the number by 2. After this operation the new value is displayed

def double(number):
    return number * 2

value = int(input("Enter a number: "))
result = double(value)

print("Doubled value:", result)
