from astar import astar
from greedy import greedy_best_first


grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0]
]

start = (0, 0)
goal = (6, 6)

astar_path, astar_nodes = astar(grid, start, goal)
greedy_path, greedy_nodes = greedy_best_first(grid, start, goal)

print("A* Search")

if astar_path:
    print("Path:", astar_path)
    print("Path Length:", len(astar_path) - 1)
    print("Nodes Explored:", astar_nodes)
else:
    print("No path found")

print()
print("Greedy Best First Search")

if greedy_path:
    print("Path:", greedy_path)
    print("Path Length:", len(greedy_path) - 1)
    print("Nodes Explored:", greedy_nodes)
else:
    print("No path found")
