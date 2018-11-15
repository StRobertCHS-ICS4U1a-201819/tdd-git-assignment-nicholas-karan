import pytest
# FUNCTION: MODE
from statTools import *

def test_mode_basic():
    assert(mode([4, 5, 10]) == "no Mode")

def test_mode_emptyList():
    assert(mode([]) == -1)

def test_mode_basic3():
    assert(mode([1, 1, 2, 3, 4, 5, 5, 5, 5, 5]) == [5])

def test_mode_OneValue():
    assert(mode([1]) == [1])

def test_mode_oneType():
    assert(mode([1,1,1,1]) == [1])

def test_mode_finalTest():
    assert(mode([5, 4, 3 ,5 ,6 ,7, 4, 3, 4,5, 6, 4 ,43 ,23 ,4 ,45, 64, 3 ,4 ]) == [4])

# FUNCTION: RANGE
def test_range_basic():
    assert(func_range([0, 3]) == 3)

def test_range_oneValue():
    assert(func_range([0]) == 0)

def test_range_empty():
    assert(func_range([]) == -1)

def test_range_oneType():
    assert(func_range([1, 1, 1] == 0))

def test_range_basic2():
    assert(func_range([1, 3, 4, 5, 5, 91]) == 90)

def test_range_basic3():
    assert(func_range([1, 1, 14, 53]) == 52)