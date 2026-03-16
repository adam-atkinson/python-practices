# Team Selector ⚽️

A simple Python script that randomly selects team captains from predefined teams.

## Description 🧐

This script defines two teams with member names and randomly selects one captain from each team using Python's `random` module. It then prints the selected captains to the console.

## Features ✨

- Predefined team members
- Random captain selection
- Simple console output

## Requirements 📋

- Python 3.x

## Usage

1. Ensure you have Python installed.
2. Run the script:

   ```bash
   python team_selector.py
   ```

3. View the output showing the selected captains.

## Example Output

```markdown
Team 1 Captain: Sarah
Team 2 Captain: Emma
```

## Code Structure 🔧

- `team1` and `team2`: Lists containing team member names
- `captain1` and `captain2`: Randomly selected captains
- Uses `random.choice()` for selection

## Learning Concepts 📚

This script demonstrates fundamental Python concepts:

- **Importing modules**: Using `import random` to access the random module
- **Lists**: Storing team members in list data structures
- **Random selection**: Utilising `random.choice()` for unpredictable outcomes
- **Console output**: Printing results with the `print()` function
