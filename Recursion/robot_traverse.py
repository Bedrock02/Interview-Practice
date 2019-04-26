"""
Starting from 0,0 traverse to x,y with the only possible moves as
Down and Right. Collect All Paths
"""

def traverse(current, goal, path, grid, collection):
    x_is_invalid = current[0] > goal[0] or current[0] >= len(grid)
    y_is_invalid = current[1] > goal[1] or current[1] >= len(grid[0])

    if x_is_invalid or y_is_invalid:
        return

    if grid[current[0]][current[1]] != 0:
        return

    if current == goal:
        collection.append(path)
        return

    traverse((current[0] + 1, current[1]), goal, path + ' D', grid, collection)
    traverse((current[0], current[1] + 1), goal, path + ' R', grid, collection)
