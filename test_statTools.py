import pytest
from statTools import *

# mean tests
def test_mean_basic1():
    assert(mean([1,2,3,4,5]) == 3)

def test_mean_basic2():
    assert(mean([93, 91, 90, 96, 89, 93]) == 92)

def test_mean_negative_basic():
    assert(mean([-5, -8,-23,-87, 30,56]) == -37/6)

#illegal input empty list
def test_mean_unusual1():
    assert(mean([]) == 0)

#illegal input characters
#def test_mean_unusual2():
#    assert(mean(['a', 'b', 'c']) == error)

# mode tests

def test_mode_basic1():
    assert(mode([1,2,3,4,5,5,6,7,8,9]) == 5)
