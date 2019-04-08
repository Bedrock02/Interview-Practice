from zeroed_matrix import *


def test_zeroed_out():
    grid = [
        [1, 2, 3],
        [1, 0, 3],
        [1, 2, 0],
    ]
    zeroed_out = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    zero_out(grid)
    assert grid == zeroed_out
