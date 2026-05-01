# 📖 User Story

## 🎯 Overview

This is a fun interactive program that generates a creative story by combining user inputs. It's inspired by the classic Mad Libs game, where users provide words (adjectives, nouns, and verbs) that get inserted into a pre-written story template.

## 📝 Description

The User Story program creates a personalised narrative by prompting the user to enter various parts of speech. The program then weaves these inputs into a cohesive story about a walk through the woods. Each time you run the program with different inputs, you get a unique and often humorous story!

## ✨ Features

- **Interactive Input**: Prompts user for adjectives, nouns, and verbs
- **Dynamic Story Generation**: Creates unique stories based on user inputs
- **Simple & Fun**: Perfect for learning basic Python concepts
- **Instant Feedback**: Displays the complete story immediately after input

## 🚀 Getting Started

### How to Run

1. Navigate to the `user-story` directory:

   ```bash
   cd user-story
   ```

2. Run the program:

   ```bash
   python user_story.py
   ```

3. Follow the prompts and enter the requested words when asked

### Example Usage

```bash
Enter an adjective: dark
Enter a noun: rabbit
Enter a second adjective: fluffy
Enter a verb: hopped
Enter one last adjective: amazed

Output:
Today I went for a walk through the dark woods.
On my journey, I saw rabbit.
rabbit was fluffy and hopped.
I was amazed to see such a sight!
```

## 📚 Learning Concepts

This program demonstrates several important Python concepts:

### 1. **Input Function**

- The `input()` function is used to capture user input from the console
- Whatever the user types is stored as a string variable
- Example: `adjective1 = input("Enter an adjective: ")`

### 2. **Variables & Data Types**

- Understanding how to create and store data in variables
- All inputs from `input()` are strings in Python
- Variables can be referenced and reused throughout the program

### 3. **String Interpolation (f-strings)**

- f-strings (formatted string literals) allow embedding expressions inside strings
- Syntax: `f"Text {variable} more text"`
- Makes it easy to create dynamic, readable output
- Example: `f"Today I went for a walk through the {adjective1} woods."`

### 4. **Print Function**

- The `print()` function outputs text to the console
- Can print strings, variables, and f-strings
- Multiple print statements create multiple lines of output

### 5. **Program Flow & Logic**

- Understanding the sequence of operations in a program
- Input → Processing → Output flow
- How variables carry data through a program

### 6. **String Manipulation**

- Combining multiple strings and variables into coherent sentences
- Creating readable output by understanding spacing and punctuation
