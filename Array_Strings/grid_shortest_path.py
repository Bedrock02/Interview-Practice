def find_shortest_path(grid, startCord, endCord):
    queue = [('', 0, startCord)]

    while queue:
        for candidate in range(len(queue)):
            popped = queue.pop(0)
            path, steps, cord = popped
            if cord == endCord:
                return (path, steps)

            i, j = cord

            # Neighbor Left
            if j - 1 >= 0 and grid[i][j - 1] != 1:
                queue.append((path + 'R', steps + 1, (i, j-1)))
            # Neighbor Right
            if j + 1 < len(grid[0]) and grid[i][j + 1] != 1:
                queue.append((path + 'R', steps + 1, (i, j + 1)))
            # Neighbor Up
            if i - 1 >= 0 and grid[i - 1][j] != 1:
                queue.append((path + 'U', steps + 1, (i - 1, j)))
            # Neighbor Down
            if i + 1 < len(grid) and grid[i + 1][j] != 1:
                queue.append((path + 'D', steps + 1, (i + 1, j)))
