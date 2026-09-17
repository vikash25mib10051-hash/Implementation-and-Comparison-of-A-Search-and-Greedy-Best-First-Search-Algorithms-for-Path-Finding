import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    queue = [(heuristic(start, goal), start)]
    came_from = {}
    visited = set()

    while queue:
        _, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = []

            while current != start:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, len(visited)

        x, y = current

        neighbors = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0:
                    neighbor = (nx, ny)

                    if neighbor not in visited:
                        if neighbor not in came_from:
                            came_from[neighbor] = current

                        h_cost = heuristic(neighbor, goal)
                        heapq.heappush(queue, (h_cost, neighbor))

    return None, len(visited)
