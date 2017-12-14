from perfect_numbers import *
import sys
import pytest

def test_factors():
    assert(is_factor(6,2) )
    assert (not is_factor(12,5) )

def test_get_factors():
    assert(get_factors(12)=={1,2,3,4,6})
    assert(sorted(get_factors(256)) ==[1,2,4,8,16,32,64,128])
    assert(sorted(get_factors(13)) == [1])

def test_perfect():
    perfect_numbers=[6,28,496,8128]
    for num in perfect_numbers:
        assert(classify(num) == "perfect")

def test_deficient():
    deficient_numbers=[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 43, 44, 45, 46, 47, 49, 50]
    for num in deficient_numbers:
        assert(classify(num)=="deficient")

def test_abundant():
    abundant_numbers=[12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120]
    for num in abundant_numbers:
        assert(classify(num)== "abundant" )

def test_user_input():
    with pytest.raises(ValueError) as val_err:
        classify(1.5)
    assert(val_err.value.args[0]=='1.5 is not an integer')
    with pytest.raises(ValueError) as val_err:
        classify("Hi")
    assert(val_err.value.args[0]=='Hi is not an integer')
    with pytest.raises(ValueError) as val_err:
        classify(99999999999999)
    assert(val_err.value.args[0]=='99999999999999 is too big')
    with pytest.raises(ValueError) as val_err:
        classify(0)
    assert(val_err.value.args[0]=='I only work on positive integers')
