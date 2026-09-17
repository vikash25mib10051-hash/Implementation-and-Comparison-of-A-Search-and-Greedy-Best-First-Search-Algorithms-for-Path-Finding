# A* Search vs Greedy Best First Search

## Overview

This project implements two informed search algorithms used in Artificial Intelligence: A* Search and Greedy Best First Search. The purpose of the project is to understand how heuristic information guides search and how the two algorithms differ when applied to a grid-based path finding problem.

---

## Features

* Grid-based path finding
* Implementation of A* Search for shortest path discovery
* Implementation of Greedy Best First Search for heuristic-based traversal
* Manhattan distance heuristic
* Comparison of path length and explored nodes
* Simple and readable code structure

---

## Concepts Used

* Informed search techniques
* Heuristic search
* State space representation
* Graph traversal methods
* Basic problem solving in AI

---

## Tech Stack

* Python
* No external libraries required

---

## Project Structure

```text
├── code
│   ├── astar.py
│   ├── greedy.py
│   └── main.py
├── Project_Report.docx
└── README.md
```

---

## How to Run

1. Open the project folder.

2. Navigate to the code directory.

```text
cd code
```

3. Run the program.

```text
python main.py
```

---

## Output

The program searches for a path between a defined start node and goal node using both A* Search and Greedy Best First Search. It displays the path found, its length, and the number of nodes explored by each algorithm.

For the included demonstration grid, A* finds a 12-step path while Greedy Best First Search finds a 14-step path. Greedy explores fewer nodes in this example, showing the trade-off between aggressively following the heuristic and considering the actual path cost.

---

## A* vs Greedy Best First Search Comparison

| A* Search | Greedy Best First Search |
| --- | --- |
| Uses `f(n) = g(n) + h(n)` | Uses `f(n) = h(n)` |
| Considers path cost and heuristic | Considers only the heuristic |
| Finds an optimal path with an admissible heuristic | Does not guarantee an optimal path |
| May explore more nodes | Can reach the goal with fewer explorations |
| More balanced search strategy | More goal-directed search strategy |

---

## Learning Outcome

This project provides a basic understanding of informed search algorithms in artificial intelligence. It demonstrates how A* combines path cost with heuristic information, while Greedy Best First Search selects nodes mainly according to estimated closeness to the goal.

---

## Note

This project was developed as part of coursework for Fundamentals in Artificial Intelligence and Machine Learning.

---

## Author

Name: VIKASH RAJ PATEL

Registration Number: 25MIB10051
