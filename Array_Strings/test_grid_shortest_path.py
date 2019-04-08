from grid_shortest_path import find_shortest_path

def test_shortest_path():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert find_shortest_path(grid, (0,0), (0,2)) == ('DDRRUU', 6)
    assert find_shortest_path(grid, (0,0), (1,2)) == ('DDRRU', 5)

def test_shortest_path_2():
    grid = [
        [ 0, 1, 0, 1, 1, 1, 1, 1,],
        [ 0, 1, 0, 1, 0, 0, 0, 0,],
        [ 0, 1, 1, 1, 0, 1, 1, 1,],
        [ 0, 0, 0, 0, 0, 0, 0, 1,],
        [ 0, 0, 0, 0, 0, 0, 0, 1,],
        [ 0, 0, 0, 0, 0, 0, 0, 1,],
        [ 0, 0, 0, 0, 0, 0, 0, 1,],
        [ 0, 0, 0, 0, 0, 0, 0, 1,],
        [ 0, 0, 0, 0, 0, 0, 0, 0,],
    ]
    assert find_shortest_path(grid, (0,0), (1,7)) == ('DDDRRRRUURRR', 12)
    assert find_shortest_path(grid, (0,0), (8,7)) == ('DDDRRRRRRDDDDDR', 15)
