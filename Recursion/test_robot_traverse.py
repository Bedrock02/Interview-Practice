from robot_traverse import *


def test_robot_traverse():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    start = (0, 0)
    end = (2, 2)
    paths = traverse(start, end, grid)
    assert len(paths) == 6
