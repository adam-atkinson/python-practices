# Python Practices
# First Program
# This is my very first program written in Python
# I have now added validation and error handling, and I added a loop allowing the user to choose whether to quit the program or restart it again from the beginning

while True:
    while True:
        first_name = input("Please enter your first name: ").strip()                # .strip()      - removes accidental whitespace
        if first_name.isalpha():                                                    # .isalpha()    - checks input contains only letters
            first_name = first_name.capitalize()                                    # .capitalize() - formats the input so first letter is uppercase and the rest are lowercase
            break                                                                   # break         - if the conditions are met, the while loop can break and move to the next block of code, if not the user is prompted to try again
        print("Invalid input! First name should only contain letters!")

    while True:
        last_name = input("Please enter your last name: ").strip()
        if last_name.isalpha():
            last_name = last_name.capitalize()
            break
        print("Invalid input! Last name should only contain letters!")

    while True:
        try:
            age = int(input("Please enter your age: "))
            if age >= 0:                                                            # this checks the number entered is not lower than zero as this is not logical
                break
            print("Invalid input! Age must be a positive number!")
        except ValueError:                                                          # if anything other than a whole number is entered, the user is prompted to try again
            print("Invalid input! Please enter your age as a whole number!")

    print(f"Your full name is: {first_name} {last_name}")
    print(f"You are: {age} years old")

    while True:
        choice = input("\nWould you like to start again? (y/n): ").strip().lower()  # asks the user if they would like to start again or quit
        if choice == "n":
            print("Goodbye!")                                                       # if the choice is 'n' execute the print statement and break
            break
        elif choice == "y":                                                         # if the choice is 'y' start the program from the beginning 
            break
        else:
            print("Invalid choice. Please type 'y' or 'n'.")                        # anything other than 'y' or 'n' entered will prompt the user to try again 

    if choice == "n":
        break
