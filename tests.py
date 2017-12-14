from perfect_numbers import *

def test_factors():
    assert(is_factor(6,2) )
    assert (not is_factor(12,5) )

def dtest_perfect():
    assert(classify(6) == True)
