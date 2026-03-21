import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif user == "rock" and computer == "scissors":
        return "You win! Rock beats scissors."
    elif user == "paper" and computer == "rock":
        return "You win! Paper beats rock."
    elif user == "scissors" and computer == "paper":
        return "You win! Scissors beats paper."
    else:
        return "Computer wins!"
    
def play_game():
    print("=== Rock, Paper, Scissors Game ===")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
