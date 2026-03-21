# 📝 Simple To-Do List

A basic command-line to-do list application in Python that allows you to view, add, and remove tasks using a simple menu interface.

## ⭐ What it does

- Uses a list to store tasks in memory.
- Provides a menu with options to view, add, remove tasks, or exit.
- Runs in a loop until the user chooses to exit.
- Handles invalid inputs and empty lists gracefully.

## ▶️ How to run

From the folder containing the file:

```bash
python simple_to_do_list.py
```

Or with Python 3 explicitly:

```bash
python3 simple_to_do_list.py
```

Use the menu options (1-4) to interact with your to-do list.

## 🛠️ File contents

- `simple_to_do_list.py` - the to-do list application script.
- `README.md` - this documentation.

## 💡 Learning Concepts

### 1. Lists as data structures

- `tasks = []` initialises an empty list to store tasks.
- `append()` adds items, `remove()` deletes items.
- Lists maintain order and allow duplicates.

### 2. Control flow with loops

- `while True:` creates an infinite loop for the menu.
- `break` exits the loop when user chooses to quit.

### 3. Conditional statements

- `if-elif-else` handles different menu choices.
- Nested conditionals for input validation.

### 4. User input and string comparison

- `input()` reads user choices and task names.
- String equality (`==`) for menu selection.
- Membership testing (`in`) for task removal.

### 5. Console output and formatting

- `print()` statements for menu and feedback.
- Basic text formatting for readability.

### 6. Program structure and flow

- Initialisation, main loop, and exit.
- Separation of concerns with menu display and action handling.

## 📚 Notes

This repository is part of basic Python practice projects. It demonstrates fundamental concepts like lists, loops, and conditionals in a practical, interactive application.
