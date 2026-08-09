# task_synenttech_task1
Python CLI calculator with basic arithmetic operations, input validation, error handling, and unit tests using unittest.
#  CLI Calculator

A simple command-line calculator built with **Python**. It performs basic arithmetic operations and includes input validation and error handling.

## Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Handles invalid number input
* Prevents division by zero
* Validates mathematical operators
* Supports decimal numbers
* Type `exit` or `quit` at any prompt to close the calculator
* Runs continuously until the user exits
* Handles `Ctrl+C` gracefully

## Technologies Used

* **Python 3**
* **unittest** for testing

## Project Structure

```text
cli-calculator/
│
├── calculator.py
├── test_calculator.py
└── README.md
```

##  Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd cli-calculator
```

### 2. Run the Calculator

```bash
python calculator.py
```

You should see:

```text
====================================
      Welcome to CLI Calculator
====================================
Type 'exit' or 'quit' at any prompt to close the application.

--- New Calculation ---
Enter the first number:
```

### 3. Example

```text
Enter the first number: 10
Enter an operator (+, -, *, /): *
Enter the second number: 5

Result: 10 * 5 = 50
```

Another example:

```text
Enter the first number: 10
Enter an operator (+, -, *, /): /
Enter the second number: 4

Result: 10 / 4 = 2.5
```

## Running Tests

The project includes automated unit tests using Python's built-in `unittest` framework.

Run:

```bash
python -m unittest test_calculator.py
```

The tests cover:

* Addition
* Subtraction
* Multiplication
* Division
* Division by zero
* Invalid operators

For example, the test suite verifies that division by zero raises a `ZeroDivisionError` and unsupported operators raise a `ValueError`.

## Error Handling

The calculator handles common errors instead of crashing unexpectedly.

### Invalid Number

```text
Enter the first number: abc
Invalid input. Please enter a valid number (e.g., 5 or 3.14).
```

### Invalid Operator

```text
Enter an operator (+, -, *, /): %
Invalid operator. Please enter one of the following: +, -, *, /
```

### Division by Zero

```text
Enter the first number: 10
Enter an operator (+, -, *, /): /
Enter the second number: 0

Error: Division by zero is not allowed.
```

##  Test Coverage

The test suite includes positive and negative test cases, including integer and decimal calculations.

| Operation        | Tested |
| ---------------- | ------ |
| Addition         | ✅      |
| Subtraction      | ✅      |
| Multiplication   | ✅      |
| Division         | ✅      |
| Decimal numbers  | ✅      |
| Negative numbers | ✅      |
| Division by zero | ✅      |
| Invalid operator | ✅      |

## Purpose

This project was created as a small Python project to practice:

* Python functions
* User input handling
* Exception handling
* Command-line applications
* Unit testing
* Writing clean and modular code

## Future Improvements

Possible future features include:

* More mathematical operations
* Power and square-root functions
* Calculation history
* Better CLI interface
* Automated test coverage reporting
* Packaging the calculator as a Python application

## Author

**Alisha Amin**

---

⭐ If you found this project useful, consider giving the repository a star!
