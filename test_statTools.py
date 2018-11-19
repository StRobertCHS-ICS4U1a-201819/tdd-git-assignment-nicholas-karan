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

"""
-------------------------------------------------------------------------
Name:               test_statTools.py

Purpose:       Contains test cases for functions of Measures of Central Tendancy

Author:             Polobotu.K, Gin.N

Created:       08/11/2018
-------------------------------------------------------------------------
"""


import pytest
import math
# FUNCTION: MODE
from statTools import *

def test_mode_basic():
    assert(mode([4, 5, 10]) == "no Mode")

def test_mode_emptyList():
    assert(mode([]) == None)

def test_mode_nonValue():
    with pytest.raises(TypeError) as error:
        mode([1, 1, 2, 3, 4, "b", 5, 5])
    assert("list contains non integer values" == str(error.value))

def test_mode_OneValue():
    assert(mode([1]) == "no Mode")

def test_mode_oneType():
    assert(mode([1,1,1,1]) == [1])

def test_mode_finalTest():
    assert(mode([ 4, 3 ,6 ,7, 4, 3, 4, 4 ,3 ,4]) == [4])

# FUNCTION: RANGE
def test_range_basic():
    assert(func_range([0, 3]) == 3)

def test_range_basic2():
    assert(func_range([1, 3, 4, 5, 5, 91]) == 90)

def test_range_oneType():
    assert(func_range([1, 1, 1, 1]) == 0)

def test_range_empty():
    with pytest.raises(ValueError) as error:
        func_range([])
    assert("no values given") == str(error.value)

def test_range_nonValue():
    with pytest.raises(TypeError) as error:
        func_range([1, 2, 4, "nope"])
    assert("cannot take in strings") == str(error.value)

def test_range_oneValue():
        assert(func_range([5]) == 0)

# FUNCTION: VARIANCE

def test_variance_basic():
    assert(variance([1, 2, 3]) == 0.6666666666666666)

def test_variance_basic2():
    assert(variance([1, 2, 4, 5]) == 2.5)

def test_variance_nonValue():
    with pytest.raises(TypeError) as error:
        variance([2, 3, 5, 5, 3, 4, 5, 6, "a"])
    assert("list contains non integer values") == str(error.value)

def test_variance_empty():
    with pytest.raises(ValueError) as error:
        variance([])
    assert("no variance if there are one or less values") == str(error.value)

def test_variance_negatives():
    assert (variance([-8, -8, -8, -8]) == 0)

def test_variance_oneValue():
    with pytest.raises(ValueError) as error:
        variance([3])
    assert("no variance if there are one or less values") == str(error.value)

# FUNCTION: STANDARD DEVIATION

def test_stndDev_basic():
    assert(stnd_dev([1, 2, 3]) == 0.816)

def test_stndDev_nonValue():
    with pytest.raises(TypeError) as error:
        stnd_dev([1, 2, 4, "Code"])
    assert("list contains non integer values") == str(error.value)

def test_stndDev_basic3():
    assert(stnd_dev([2, 3, 5, 5, 3, 4, 5, 6, 3]) == 1.247)

def test_stndDev_empty():
    with pytest.raises(ValueError) as error:
        stnd_dev([])
    assert("list contains one or less elements") == str(error.value)

def test_stndDev_oneType():
    assert(stnd_dev([-8, -8, -8, -8]) == 0)

def test_stndDev_oneValue():
    with pytest.raises(ValueError) as error:
        stnd_dev([3])
    assert("list contains one or less elements" == str(error.value))
