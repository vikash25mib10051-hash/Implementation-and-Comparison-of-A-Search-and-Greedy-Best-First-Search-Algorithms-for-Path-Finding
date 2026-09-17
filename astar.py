import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    queue = [(0, start)]
    came_from = {}
    g_cost = {start: 0}
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
                    new_cost = g_cost[current] + 1

                    if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                        g_cost[neighbor] = new_cost
                        came_from[neighbor] = current

                        f_cost = new_cost + heuristic(neighbor, goal)
                        heapq.heappush(queue, (f_cost, neighbor))

    return None, len(visited)
