# Advanced Calculator 🧮

A Python program that demonstrates conditional logic, user input validation, and multiple arithmetic operations.

## Features ✨

- **Multiple Operations**: Supports addition (+), subtraction (-), multiplication (\*), and division (/)
- **User Input**: Takes two numbers and operation choice from user
- **Error Handling**: Validates operation input and provides feedback for invalid choices
- **Conditional Logic**: Uses if/elif/else statements to handle different operations

## How to Run 🏃‍♂️

1. Navigate to the advanced-calculator directory
2. Run the Python script:

```bash
python advanced_calculator.py
```

## Usage Examples 📝

### Addition

Calculator
Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, \*, /): +
Result: 15.0

### Division

Calculator
Enter the first number: 20
Enter the second number: 4
Choose an operation (+, -, \*, /): /
Result: 5.0

### Invalid Operation

Calculator
Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, \*, /): %
Invalid operation

## Learning Concepts 📚

This program demonstrates:

- **Conditional Statements**: Using `if`, `elif`, and `else` for decision making
- **String Comparison**: Comparing user input with operation symbols
- **Error Handling**: Basic validation and user feedback
- **Multiple Code Paths**: Different execution paths based on user choice
- **Variable Scope**: Understanding where variables are accessible
- **Type Conversion**: Converting input strings to numbers

## Code Structure 🔧

1. Get user input (two numbers)
2. Get operation choice
3. Use conditional logic to perform correct operation
4. Handle invalid operations
5. Display result (if valid operation)

## Future Enhancements 🚀

Potential improvements could include:

- Input validation for numbers (handling non-numeric input)
- Division by zero protection
- More operations (exponentiation, modulo, etc.)
- Loop for multiple calculations without restarting
- Menu-driven interface with numbered options
- History of previous calculations
