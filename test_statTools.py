import pytest
from statTools import *

# mean tests
def test_mean_basic1():
    assert(mean([1, 2, 3, 4, 5]) == 3)

def test_mean_basic2():
    assert(mean([93, 91, 90, 96, 89, 93]) == 92)

def test_mean_negative():
    assert(mean([-5, -8, -23, -87, 30, 56]) == -37/6)

#illegal input empty list
def test_mean_empty_List():
    with pytest.raises(ValueError) as error:
        mean([])
    assert("An empty list was provided" == str(error.value))

#illegal input characters

def test_mean_illegal_input():
    with pytest.raises(TypeError) as error:
        mean([1, 2, 3, 'a'])
    assert("List contains a non integer value" == str(error.value))

#median tests

def test_median_basic1():
    assert(median([1, 2, 3, 4, 5, 6, 7]) == 4)

def test_median_basic2():
    assert(median([5, 6, 7, 8, 9, 10]) == 7.5)

def test_median_basic3():
    assert(median([22, 77, 73, 59, 95, 31, 66, 14]) == 62.5)

def test_median_empty_list():
    assert(median([]) == -1)

#def test_median_illegal_input():
#   assert(median([1, 2, 3, 'f'])

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

#def test_lq_illegal_imput():

#upper quartile tests

def test_uq_basic1():
    assert (uQ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7.5)

def test_uq_basic2():
    assert(uQ([1, 1, 3, 4, 6, 7, 7, 9, 10, 11, 14, 17]) == 10.5)

def test_uq_basic3():
    assert(uQ([7, 9, 3, 4, 9, 11, 18, 6]) == 10)

def test_uq_empty_list():
    assert(uQ([]) == -1)

def test_uq_less_than4():
    assert(uQ([1,2,3]) == -1)

