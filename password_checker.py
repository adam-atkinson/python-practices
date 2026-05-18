# Python Practices
# Password Strength Checker
# This program asks the user to input a password. The strength of the password is then evaluated based on specific criteria like the length, 
# if it only has numbers or letters, and a print statement is displayed based on the results of the basic validation techniques

password = input("Enter a password: ")

if len(password) < 6:                   # 'len' means if the length is less than 6
    print("Weak: Too short")
elif password.isalpha():                # 'isalpha()' returns true if the string only contains letters
    print("Weak: Add numbers")
elif password.isnumeric():              # 'isnumeric()' returns true if the string only contains numbers
    print("Weak: Add letters")
else:
    print("Strong Password!") 
