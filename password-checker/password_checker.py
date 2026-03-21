password = input("Enter a password: ")

if len(password) < 6:
    print("Weak password: Password must be at least 6 character long!")
elif password.isalpha():
    print("Weak password: Password must contain at least one number!")
elif password.isnumeric():
    print("Weak password: Password must contain at least one letter!")
else:
    print("Strong password!")
