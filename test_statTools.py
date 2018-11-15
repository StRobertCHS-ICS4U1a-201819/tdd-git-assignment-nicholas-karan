import pytest
import math
# FUNCTION: MODE
from statTools import *

def test_mode_basic():
    assert(mode([4, 5, 10]) == "no Mode")

def test_mode_emptyList():
    assert(mode([]) == -1)

def test_mode_nonValue():
    assert(mode([1, 1, 2, 3, 4, 5, "b", 5, 5, 5]) == "list contains non integer values")

def test_mode_OneValue():
    assert(mode([1]) == [1])

def test_mode_oneType():
    assert(mode([1,1,1,1]) == [1])

def test_mode_finalTest():
    assert(mode([5, 4, 3 ,5 ,6 ,7, 4, 3, 4, 5, 6, 4 ,43 ,23 ,4 ,45, 64, 3 ,4]) == [4])

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

def test_range_nonValue():
    assert(func_range([1, 1, "yeet", 53]) == "list contains non integer values")

# FUNCTION: VARIANCE

def test_variance_basic():
    assert(variance([1, 2, 3]) == 0.6666666666666666)

def test_variance_basic2():
    assert(variance([1, 2, 4, 5]) == 2.5)

def test_variance_nonValue():
    assert(variance([2, 3, 5, 5, 3, 4, 5, 6, "a"] == ""))

def test_variance_empty():
    assert(variance([]) == -1)

def test_variance_oneType():
    assert variance([-8, -8, -8, -8] == 0)

def test_variance_oneValue():
    assert(variance([3]) == -1)

# FUNCTION: STANDARD DEVIATION

def test_stndDev_basic():
    assert(stnd_dev([1, 2, 3]) == 0.816)

def test_stndDev_nonValue():
    assert(stnd_dev([1, 2, 4, "Code"]) == "list contains non integer values")

def test_stndDev_basic3():
    assert(stnd_dev([2, 3, 5, 5, 3, 4, 5, 6, 3]) == 1.247)

def test_stndDev_empty():
    assert(stnd_dev([]) == -1)

def test_stndDev_oneType():
    assert(stnd_dev([-8, -8, -8, -8]) == 0)

def test_stndDev_oneValue():
    assert(stnd_dev([3]) == -1)
