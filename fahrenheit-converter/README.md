# 🌡️ Fahrenheit to Celsius Converter

A simple Python script that converts temperatures from Fahrenheit to Celsius using the standard conversion formula.

## ⭐ What it does

- Defines a function `fahrenheit_to_celsius(fahrenheit)` that performs the conversion.
- Prompts user for a Fahrenheit temperature.
- Converts and displays the result in Celsius with 2 decimal places.

## ▶️ How to run

From the folder containing the file:

```bash
python fahrenheit_to_celsius.py
```

Or with Python 3 explicitly:

```bash
python3 fahrenheit_to_celsius.py
```

Enter a number when prompted (e.g., 32 for freezing point).

## 🛠️ File contents

- `fahrenheit_to_celsius.py` - the temperature conversion script.
- `README.md` - this documentation.

## 💡 Learning Concepts

### 1. Mathematical formulas in code

- Implementing the conversion formula: `celsius = (fahrenheit - 32) * 5/9`
- Translating real-world math into programming logic.

### 2. Function definition and return values

- `def fahrenheit_to_celsius(fahrenheit):` defines a reusable function.
- `return celsius` sends the result back to the caller.

### 3. User input and type conversion

- `input()` reads string input from user.
- `float()` converts string to floating-point number for decimal temperatures.

### 4. String formatting and output

- f-strings for embedding variables: `f"\n{user_input}°F is equal to {converted_temp:.2f}°C"`
- `.2f` formats to 2 decimal places.

### 5. Basic program structure

- Function definitions.
- Main execution code.

### 6. Temperature conversion concepts

- Understanding Fahrenheit and Celsius scales.
- The freezing point of water (32°F = 0°C).

## 📚 Notes

This repository is part of basic Python practice projects. It introduces mathematical operations, user input, and formatted output in a practical context.
