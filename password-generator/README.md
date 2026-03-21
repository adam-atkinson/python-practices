# 🔐 Secure Password Generator

A Python script that creates cryptographically secure random passwords using the `secrets` module, combining letters, numbers, and special characters.

## ⭐ What it does

- Imports `string` and `secrets` modules.
- Defines a function `generate_password(length)` that builds a password from all ASCII letters, digits, and punctuation.
- Prompts user for desired password length.
- Generates and prints a secure random password.

## ▶️ How to run

From the folder containing the file:

```bash
python secure_password_generator.py
```

Or with Python 3 explicitly:

```bash
python3 secure_password_generator.py
```

Enter a number when prompted (e.g., 12 for a 12-character password).

## 🛠️ File contents

- `secure_password_generator.py` - the main script that generates secure passwords.
- `README.md` - this documentation.

## 💡 Learning Concepts

### 1. Cryptographically secure randomness (`secrets` module)

- `secrets.choice()` provides secure random selection, unlike `random.choice()`.
- Essential for security-sensitive applications like password generation.

### 2. String constants (`string` module)

- `string.ascii_letters` - all lowercase and uppercase letters.
- `string.digits` - 0-9.
- `string.punctuation` - special characters like !@#$%.
- Combining them creates a comprehensive character set.

### 3. Generator expressions

- `''.join(secrets.choice(characters) for _ in range(length))` uses a generator for efficiency.
- Builds the password character by character without storing intermediate lists.

### 4. User input and validation

- `input()` reads user input as a string.
- `int()` converts to integer for length.
- Basic input handling for interactive programs.

### 5. Function definition and modularity

- `def generate_password(length):` encapsulates password generation logic.
- Makes code reusable and testable.

### 6. Security best practices

- Using `secrets` over `random` for cryptographic purposes.
- Including diverse character types for stronger passwords.

## 📚 Notes

This repository is part of basic Python practice projects. It demonstrates secure coding practices and is suitable for beginners learning about randomness, security, and user interaction in Python.
