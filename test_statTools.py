import pytest
from statTools import *

def test_mean_basic1():
    assert(mean([1,2,3,4,5]) == 3)

def test_mean_basic2():
    assert(mean([93, 91, 90, 96, 89, 93]) == 92)

def test_mean_negatives():
    assert(mean([-5, -8,-23,87, -30,56]) == 77/6)