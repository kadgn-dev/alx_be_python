#!/usr/bin/env python3
"""
Module: robust_division_calculator
Provides a safe_divide function with error handling for invalid inputs and division by zero.
"""

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling invalid inputs and division by zero.
    Returns a string describing the result or error.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
