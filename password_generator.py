# Python Practices
# Password Generator
# This program generates a secure random password for the user by first asking for the desired length
# then selecting characters from a combined set of letters, digits, and punctuation symbols

import string 
import secrets 

while True:
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation                               # Combine all ascii letters, digits and punctuation to create a full character set for the password
        return "".join(secrets.choice(characters) for _ in range(length))                                    # Use secrets.choice for cryptographically secure random selection. join() combines selected characters into a single string 
    
    while True:
        try:
            user_length = int(input("Please enter desired password length: "))
            if user_length >= 8:                                                                             # Enforce a minimum password length of 8 characters for basic security
                break 
            print("Password should be at least 8 characters for security.")

        except ValueError:                                                                                   # Catch ValueError just in case the user enters anything other than a whole number
            print("Invalid input! Please enter a whole number.")

    new_password = generate_password(user_length)                                                            # Call the generate password function and store the value

    print(f"Your secure password is:\n{new_password}")

    while True:                                                                                              # Give the user the option to generate a new password or quit the program
        choice = input("\nWould you like to generate another password or quit? (new/quit): ").strip().lower()
        if choice == "quit":
            print("Goodbye!")
            break 
        elif choice == "new":
            break 
        else:
            print("Invalid choice! Please type 'new' or 'quit'.")

    if choice == "quit":                                                                                      # The outer loop is broken if the user chooses to quit
        break 
    