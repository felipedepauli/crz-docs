# This test performans the following tests:

# 1. two positive integers
# 2. identity: multiplying any number by 1
# 3. zero: multiplying any number by 0
# 4. positive times negative
# 5. negative times negative
# 6. multiplying floats

import pytest
import math

def test_multiply_two_positive_ints():
    pass

def test_multiply_identity():
    pass

def test_multiply_by_zero():
    pass

def test_multiply_pos_times_neg():
    pass

def test_multiply_neg_times_neg():
    pass

def test_multiply_floats():
    pass


# -----------------------------------------------------------------------------
# A parametrized test function
# -----------------------------------------------------------------------------

products = [
    (2, 3, 6),          # two positive integers
    (1, 99, 99),        # identity: multiplying any number by 1
    (0, 99, 0),         # zero: multiplying any number by 0
    (2, -4, -8),        # positive times negative
    (-5, -5, 25),       # negative times negative
    (2.5, 6.7, 16.75)   # multiplying floats
]

@pytest.mark.parametrize("a, b, product", products)
def test_multiply(a, b, product):
    assert a * b == product