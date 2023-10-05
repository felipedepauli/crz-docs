# ----------------------------------------------------------
# Fixture: test_fixture
# ----------------------------------------------------------

import pytest
from accumulator.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()


# ----------------------------------------------------------
# Tests
# ----------------------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0
    
def test_accumulator_add(accum):
    assert accum.count == 0