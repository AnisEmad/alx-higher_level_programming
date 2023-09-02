#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result.

    Parameters:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Defaults to 98 if not provided.

    Returns:
    int: The sum of 'a' and 'b' as an integer.

    Raises:
    TypeError: If 'a' or 'b' is not an integer or float.
    """
    # Check if 'a' is an integer or float; if not, raise a TypeError
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")
    
    # Check if 'b' is an integer or float; if not, raise a TypeError
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or float")
    
    # Convert 'a' and 'b' to integers
    a = int(a)
    b = int(b)
    
    # Return the sum of 'a' and 'b' as an integer
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
