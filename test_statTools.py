"""
-------------------------------------------------------------------------------
Name:		test_statTools.py

Purpose:    Contains test cases for fucntions of Measures of Central Tendency and Measures of Spread

Author:		Gin.N, Polobotu.K

Created:    08/11/2018
------------------------------------------------------------------------------
"""

import pytest
from statTools import *

# Mean tests

def test_mean_basic1():
    assert(mean([1, 2, 3, 4, 5]) == 3)


def test_mean_basic2():
    assert(mean([93, 91, 90, 96, 89, 93]) == 92)


def test_mean_negative():
    assert(mean([-5, -8, -23, -87, 30, 56]) == -37/6)


def test_mean_negative2():
    assert(mean([-9, -8, -5, -3, -1]) == -5.2)


def test_mean_empty_list():
    with pytest.raises(ValueError) as error:
        mean([])
    assert("An empty list was provided" == str(error.value))


def test_illegal_input():
    with pytest.raises(TypeError) as error:
        mean([1, 2, 3, 'a'])
    assert("List contains a non integer value" == str(error.value))

# Median tests


def test_median_basic1():
    assert(median([1, 2, 3, 4, 5, 6, 7]) == 4)


def test_median_basic2():
    assert(median([5, 6, 7, 8, 9, 10]) == 7.5)


def test_median_basic3():
    assert(median([22, 77, 73, 59, 95, 31, 66, 14]) == 62.5)


def test_median_negatives():
    assert(median([-9, -8, -5, -3, -1]) == -5)


def test_median_empty_list():
    with pytest.raises(ValueError) as error:
        median([])
    assert("An empty list was provided" == str(error.value))


def test_median_illegal_input():
    with pytest.raises(TypeError) as error:
        median([1, 2, 3, 'a'])
    assert("List contains a non integer value" == str(error.value))

# Lower quartile tests


def test_lower_quartile_basic1():
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2.5)


def test_lower_quartile_basic2():
    assert(lower_quartile([12, 23, 34, 45, 46, 57, 58, 59, 67, 78, 100]) == 34)


def test_lower_quartile_basic3():
    assert(lower_quartile([7, 9, 3, 4, 9, 11, 18, 6]) == 5)


def test_lower_quartile_empty_list():
    assert(lower_quartile([]) == -1)


def test_lower_quartile_less_than4():
    assert(lower_quartile([1, 2, 3]) == -1)


def test_lower_quartile_illegal_input():
    with pytest.raises(TypeError) as error:
        lower_quartile([1, 2, 3, 'a'])
    assert("List contains a non integer value" == str(error.value))


# Upper quartile tests

def test_upper_quartile_basic1():
    assert (upper_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7.5)



def test_upper_quartile_basic2():
    assert(upper_quartile([1, 1, 3, 4, 6, 7, 7, 9, 10, 11, 14, 17]) == 10.5)


def test_upper_quartile_basic3():
    assert(upper_quartile([7, 9, 3, 4, 9, 11, 18, 6]) == 10)


def test_upper_quartile_empty_list():
    assert(upper_quartile([]) == -1)


def test_upper_quartile_less_than4():
    assert(upper_quartile([1, 2, 3]) == -1)


def test_upper_quartile_illegal_input():
    with pytest.raises(TypeError) as error:
        upper_quartile([1, 2, 3, 'a'])
    assert("List contains a non integer value" == str(error.value))

