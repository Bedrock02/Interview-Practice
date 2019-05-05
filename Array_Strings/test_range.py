from range import *


def test_range_it():
    assert range_it([-2, -1, 1, 2, 3, 4, 7, 9, 10, 11]) == "-2, -1, 1-4, 7, 9-11"
    assert range_it_2([-2, -1, 1, 2, 3, 4, 7, 9, 10, 11]) == "-2, -1, 1-4, 7, 9-11"
