import statTools
from statTools import *

def test_mode():
    assert(mode([4, 5, 10]) == -1)

def test_mode2():
    assert(mode([]) == -1)

def test_mode3():
    assert(mode([1, 1, 2, 3, 4, 5, 5, 5, 5, 5]) == 5)