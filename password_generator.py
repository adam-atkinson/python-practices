# Python Practices
# Password Generator
# This program generates a secure random password for the user by first asking for the desired length
# then selecting characters from a combined set of letters, digits, and punctuation symbols

import string 
import secrets 

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    return "".join(secrets.choice(characters) for _ in range(length)) 

user_length = int(input("Please enter desired password length: "))
new_password = generate_password(user_length)

print(f"Your secure password is: \n{new_password}") 
