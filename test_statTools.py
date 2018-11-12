import pytest
from statTools import *

# mean tests
def test_mean_basic1():
    assert(mean([1, 2, 3, 4, 5]) == 3)

def test_mean_basic2():
    assert(mean([93, 91, 90, 96, 89, 93]) == 92)

def test_mean_negative_basic():
    assert(mean([-5, -8, -23, -87, 30, 56]) == -37/6)

#illegal input empty list
def test_mean_unusual1():
    assert(mean([]) == 0)

#illegal input characters
#def test_mean_unusual2():
#    assert(mean(['a', 'b', 'c']) == error)

# mode tests

def test_mode_basic1():
    assert(mode([1, 2, 3, 4, 5, 5, 6, 7, 8, 9]) == 5)

#def test_mode_basic2():
#    assert(mode([10,30,0,30,46,23]) == 30)


#lower quartile tests

def test_lQ_basic1():
    assert(lQ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2.5)

def test_lQ_basic2():
    assert(lQ([12, 23, 34, 45, 46, 57, 58, 59, 67, 78, 100]) == 34)

def test_lq_basic3():
    assert(lQ([7, 9, 3, 4, 9, 11, 18, 6]) == 5)

def test_lq_empty_List():
    assert(lQ([]) == -1)

def test_lq_less_than4():
    assert(lQ([1,2,3]) == -1)
