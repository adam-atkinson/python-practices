# File Handler 📝

A simple Python program that demonstrates basic file operations for note-taking.

## Features ✨

- Write notes to a file
- Read and display all saved notes
- Delete all notes with confirmation
- Simple menu-driven interface
- Demonstrates file I/O operations
- **Customisable file handling**: Change the `FILENAME` variable to read any existing text file

## Customisation 🔧

You can modify the `FILENAME` variable at the top of the script to point to any text file:

```python
FILENAME = "your_file.txt"  # Change this to any file you want to read
```

This allows you to:

- View the contents of existing text files line by line
- Use the program as a simple file viewer for any text-based file
- Not restricted to note-taking - can open and display any text file

## How to Run 🏃‍♂️

1. Navigate to the file-handler directory
2. Run the Python script:

```bash
python file_handler.py
```

## Usage Example 📝

```bash
== Simple File Handler ==
1. Write a note
2. Read notes
3. Delete all notes
4. Quit
Choose an option: 1
Enter your note: This is my first note
Note saved!

== Simple File Handler ==
1. Write a note
2. Read notes
3. Delete all notes
4. Quit
Choose an option: 2

Your notes:
1. This is my first note
```

## Learning Concepts 📚

This program demonstrates:

- **File I/O Operations**: Using `open()`, `read()`, `write()`, and `close()` for file handling
- **File Existence Checking**: Using `os.path.exists()` to check if a file exists before reading
- **Context Managers**: Using `with` statements for automatic file closing
- **String Manipulation**: Using `strip()` to remove whitespace from input
- **Loop Control**: Using `while True` with `break` for menu navigation
- **Conditional Logic**: Using `if/elif/else` for menu options and confirmations
- **List Operations**: Using `enumerate()` to number the notes when displaying
- **User Input Handling**: Using `input()` for interactive menu choices
