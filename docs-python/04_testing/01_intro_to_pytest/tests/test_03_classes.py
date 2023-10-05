# ---------------------------------------------------------------------
# Testing classes
# ---------------------------------------------------------------------

# Test for Accumulator class
# 1. Create an instance of Accumulator and check that the count is 0
# 2. Add 1 to the count
# 3. Add 2 to the count
# 4. Add 3 to the count
# 5. Add without specifying a value one
# 6. Add without specifying a value twice
# 7. Avoid adding a negative number
# 8. Avoid adding a string
# 9. Avoid set directly the count

import pytest
from accumulator.accum import Accumulator 

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0
    
def test_accumulator_add():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1
    accum.add(2)
    assert accum.count == 3
    accum.add(3)
    assert accum.count == 6
    accum.add()
    assert accum.count == 7
    accum.add()
    assert accum.count == 8
    
def test_accumulator_add_negative():
    accum = Accumulator()
    with pytest.raises(ValueError, match="Can't add a negative number"):
        accum.add(-1)

# def test_accumulator_add_string():
#     accum = Accumulator()
#     with pytest.raises(TypeError):
#         accum.add("a")
        
# def test_accumulator_set_count():
#     accum = Accumulator()
#     with pytest.raises(AttributeError, match="can't set attribute"):
#         accum.count = 1
 