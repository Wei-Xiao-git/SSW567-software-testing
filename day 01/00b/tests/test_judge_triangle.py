from project.judge_triangle_method import classify_triangle
import pytest

# test is not a triangle
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, "not"),
        (1, 1, 3, "not"),
        (2, 3, 6, "not"),
        (0, 3, 4, "not"),
        (-3, 4, 5, "not"),
        ("a", 3, 4, "not"),
    ],
)
def test_invalid(a,b,c,expected):
    assert classify_triangle(a,b,c) == expected

# test different types triangle
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 4, 5, "right"),
        (3, 4, 5.000001, "scalene"),
        (3, 4, 4.999999, "scalene"),
        (5, 12, 13, "right"),
        (0.3, 0.4, 0.5, "right"),
        (1.5, 2.0, 2.5, "right"),
        (3, 3, 3, "equilateral"),
        (3.3, 3.3, 3.3, "equilateral"),
        (3.3, 3.3, 2, "isosceles"),
        (3.3, 3.3, 2, "right"), # test mistake
    ]
)
def test_valid(a,b,c,expected):
    assert classify_triangle(a,b,c) == expected
