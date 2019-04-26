from robot_traverse import *

def test_robot_traverse():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    start = (0, 0)
    end = (2, 2)
    paths = []
    current_path = ''
    traverse(start, end, current_path, grid, paths)
    assert len(paths) == 6
