"""
Triangle classification function.
Static analysis improved version.
"""

from typing import Any, Union


def classify_triangle(a, b, c):
    """
    Classify a triangle based on three side lengths.

    Returns:
        str: triangle type
    """
    print("three sides :" + str(a) + ", " + str(b) + ", " + str(c))
    if is_not_triangle(a, b, c):
        print("this is not a triangle\n")
        return "not"

    if is_equilateral(a, b, c):
        print("this is an equilateral triangle\n")
        return "equilateral"

    if is_isosceles(a, b, c):
        print("this is an isosceles triangle\n")
        return "isosceles"

    if is_right(a, b, c):
        print("this is a right triangle\n")
        return "right"

    print("this is a scalene triangle\n")
    return "scalene"


def is_right(a, b, c) -> Union[bool, Any]:
    """
    Judge if it is a right triangle.

    Returns:
        bool
    """
    arr = sorted([a, b, c])
    a, b, c = arr
    return a * a + b * b == c * c


def is_isosceles(a, b, c) -> Union[bool, Any]:
    """
    Judge if it is an isosceles triangle.

    Returns:
        bool
    """
    return a == b or b == c or c == a


def is_equilateral(a, b, c) -> Union[bool, Any]:
    """
    Judge if it is a equilateral triangle.

    Returns:
        bool
    """
    return a == b and b == c


def is_not_triangle(a, b, c) -> Union[bool, Any]:
    """
    Judge if it is a triangle.

    Returns:
        bool
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return True
    return a + b <= c or (a + c) <= b or (c + b) <= a or a <= 0 or b <= 0 or c <= 0
