def find_shortest_path(grid, startCord, endCord):
    queue = [('', startCord)]
    visited = {}
    while queue:
        popped = queue.pop(0)
        path, cord = popped
        if cord == endCord:
            return (path, len(path))
        if cord in visited and visited[cord]:
            continue
        else:
            visited[cord] = True
        i, j = cord
        # Neighbor Left
        if j - 1 >= 0 and grid[i][j - 1] != 1:
            queue.append((path + 'R', (i, j-1)))
        # Neighbor Right
        if j + 1 < len(grid[0]) and grid[i][j + 1] != 1:
            queue.append((path + 'R', (i, j + 1)))
        # Neighbor Up
        if i - 1 >= 0 and grid[i - 1][j] != 1:
            queue.append((path + 'U', (i - 1, j)))
        # Neighbor Down
        if i + 1 < len(grid) and grid[i + 1][j] != 1:
            queue.append((path + 'D', (i + 1, j)))
