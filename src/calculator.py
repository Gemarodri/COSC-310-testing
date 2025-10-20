"""
Simple calculator module to perform additions.
"""

def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Return the difference between two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of subtracting b from a. Result rounded to 2 digits.
    """
    return a - b
