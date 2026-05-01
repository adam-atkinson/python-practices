# ✂️ Rock, Paper, Scissors Game

A classic Rock, Paper, Scissors game implemented in Python, where you play against the computer in a single round.

## ⭐ What it does

- Imports the `random` module for computer choices.
- Defines functions for getting computer and user choices.
- Determines the winner based on game rules.
- Plays one round and displays the result.

## ▶️ How to run

From the folder containing the file:

```bash
python rock_paper_scissors.py
```

Or with Python 3 explicitly:

```bash
python3 rock_paper_scissors.py
```

Enter your choice when prompted (rock, paper, or scissors).

## 💡 Learning Concepts

### 1. Randomness and lists (`random` module)

- `random.choice()` selects a random item from a list.
- Used for simulating computer decisions.

### 2. User input handling

- `input()` reads user input as a string.
- `.lower()` normalises input to lowercase for case-insensitive comparison.

### 3. Conditional logic and game rules

- `if-elif-else` statements implement Rock-Paper-Scissors rules.
- Handles ties and all win/lose scenarios.

### 4. Function decomposition

- Breaking down the program into functions: `get_computer_choice()`, `get_user_choice()`, `determine_winner()`, `play_game()`.
- Improves readability and reusability.

### 5. String formatting and output

- f-strings (`f"\nYou chose: {user_choice}"`) for dynamic string insertion.
- Clear console output for game interaction.

### 6. Basic game loop structure

- Single-round game with setup, input, processing, and output phases.
