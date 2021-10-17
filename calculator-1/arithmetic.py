"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    sums = num1 + num2
    return sums


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    
    difference = num2 - num1
    return difference

def multiply(num1, num2):
    """Multiply the two inputs together."""
    product = num1 * num2
    return product

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divided = num1/num2
    return divided

def square(num1):
    """Return the square of the input."""
    squared = num1*num1
    return squared

def cube(num1):
    """Return the cube of the input."""
    cubed = num1*num1*num1
    return cubed

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    exponent = num1 ** num2
    return exponent

def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    remainder = num1 % num2
    return remainder

def add_mult(num1, num2, num3):
    """Get the sum of num1 and num2, then multiply sum with num3."""
    
    addmult = (num1 + num2) * num3
    return addmult


def add_cubes(num1, num2):
    """Add the cubes of num1 and num2."""
    
    addcube = (num1*num1*num1) + (num2*num2*num2)
    return addcube