"""
This module contains basic unit tests for the math module.
Their purpose is to show how to use the pytest framework by example.
"""

# -----------------------------------------------------------------------------
# A most basic test function
# -----------------------------------------------------------------------------

import pytest

def test_one_plus_one():
	assert 1 + 1 == 2
 
def	test_one_plus_two():
	assert 1 + 2 == 3
	a = 1
	b = 2
	c = 3
	assert a + b == c
	assert a + b == 3
	# assert a + b == 4 # this will fail
 
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
	    num  = 1 / 0
    assert 'division by zero' in str(excinfo.value)
  