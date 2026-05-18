# Python Practices
# Guessing Game
# This program asks the user to input a number between 1-10. If the correct number is input, "Correct!" will be displayed. If the incorrect number is input, "Wrong!" will be displayed

secret = 5
guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong!")
