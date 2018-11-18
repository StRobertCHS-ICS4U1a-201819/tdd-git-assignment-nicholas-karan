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

def test_range_oneValue():
    assert(func_range([5]) == 0)

def test_range_empty():
    with pytest.raises(ValueError) as error:
        func_range([])
    assert("max () arg is an empty sequence" == str(error.value))

def test_range_oneType():
    assert(func_range([1, 1, 1, 1]) == 0)

def test_range_basic2():
    assert(func_range([1, 3, 4, 5, 5, 91]) == 90)

def test_range_nonValue():
    with pytest.raises(TypeError) as error:
        func_range([1, 1, "yeet", 53])
    assert("list contains non integer values") == str(error.value)

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
