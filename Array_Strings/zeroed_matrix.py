'''
Given a NxM matrix
Write an algorithm such that if element is 0, entire row and column is set to 0
'''


def zero_out(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    zeroed_rows = [0] * num_rows
    zeroed_cols = [0] * num_cols

    for i in range(num_rows):
        for j in range(num_cols):
            if zeroed_rows[i] or zeroed_cols[j]:
                continue
            if grid[i][j] == 0:
                zeroed_rows[i] = 1
                zeroed_cols[j] = 1

    for i in range(num_rows):
        for j in range(num_cols):
            if zeroed_rows[i] or zeroed_cols[j]:
                grid[i][j] = 0
