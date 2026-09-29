"""
Utility functions for robust terminal input validation.
"""


def read_int(prompt: str) -> int:
    """Prompts user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt: str) -> float:
    """Prompts user until a valid floating-point number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_positive_int(prompt: str) -> int:
    """Prompts user until a positive integer (>= 1) is entered."""
    while True:
        val = read_int(prompt)
        if val >= 1:
            return val
        print("Please enter a number greater than or equal to 1.")