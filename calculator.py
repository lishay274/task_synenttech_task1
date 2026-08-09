#!/usr/bin/env python3
"""
Simple CLI Calculator
A command-line calculator that performs addition, subtraction, multiplication, and division.
It handles invalid input and division by zero errors.
"""

import sys

def get_number(prompt: str) -> float:
    """Prompts the user for a number and handles invalid float inputs."""
    while True:
        try:
            user_input = input(prompt).strip()
            # Allow the user to exit at any point
            if user_input.lower() in ('exit', 'quit'):
                print("Exiting calculator. Goodbye!")
                sys.exit(0)
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 5 or 3.14).")

def get_operator(prompt: str) -> str:
    """Prompts the user for a mathematical operator and validates it."""
    valid_operators = ('+', '-', '*', '/')
    while True:
        op = input(prompt).strip()
        if op.lower() in ('exit', 'quit'):
            print("Exiting calculator. Goodbye!")
            sys.exit(0)
        if op in valid_operators:
            return op
        print(f"Invalid operator. Please enter one of the following: {', '.join(valid_operators)}")

def calculate(num1: float, op: str, num2: float) -> float:
    """Performs the arithmetic operation based on the operator."""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operator: {op}")

def main():
    print("====================================")
    print("      Welcome to CLI Calculator     ")
    print("====================================")
    print("Type 'exit' or 'quit' at any prompt to close the application.")
    
    while True:
        print("\n--- New Calculation ---")
        num1 = get_number("Enter the first number: ")
        op = get_operator("Enter an operator (+, -, *, /): ")
        num2 = get_number("Enter the second number: ")
        
        try:
            result = calculate(num1, op, num2)
            # Format the output: print as integer if there's no fractional part
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result
            
            # Formatted inputs
            fmt_num1 = int(num1) if num1.is_integer() else num1
            fmt_num2 = int(num2) if num2.is_integer() else num2
            
            print(f"\nResult: {fmt_num1} {op} {fmt_num2} = {formatted_result}")
        except ZeroDivisionError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculator terminated. Goodbye!")
        sys.exit(0)
