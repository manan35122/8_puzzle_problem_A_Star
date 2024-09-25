# 8_puzzle_problem_A_Star
**8-Puzzle Solver Using A* Search Algorithm**
Overview
This project solves the 8-puzzle problem using the A Search Algorithm*. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with numbered tiles and one blank space. The goal of the puzzle is to move the tiles into a specified goal configuration by sliding the tiles into the blank space.

In this implementation, we use the Manhattan Distance heuristic to guide the A* search towards the goal configuration efficiently.

Key Concepts:
A Search Algorithm*: A graph traversal algorithm that finds the shortest path to the goal by combining the actual cost to reach a state (g(n)) and the estimated cost to the goal from that state (h(n)).
Manhattan Distance Heuristic: The sum of the absolute differences in the row and column positions of each tile from its goal position.
How the Algorithm Works
Initial State: The starting configuration of the puzzle.
Goal State: The target configuration we want to achieve.
Heuristic (Manhattan Distance): For each tile, the Manhattan distance is calculated based on its current position and goal position. The Manhattan distance is the sum of the horizontal and vertical distances between the tile's current and target positions.
Priority Queue: The A* algorithm uses a priority queue to explore the state with the lowest f(n) = g(n) + h(n) value, where g(n) is the cost to reach the current state and h(n) is the estimated cost to reach the goal.
The A* algorithm ensures the solution is found with the minimum number of moves while considering the best possible next state based on the Manhattan distance heuristic.

Code Components
1. manhattan_distance(state, goal)
This function calculates the Manhattan distance for each tile in the current puzzle state compared to the goal state. It returns the sum of the distances for all tiles, which serves as the heuristic h(n) for the A* algorithm.

2. Puzzle Class
Encapsulates the core logic of the 8-puzzle problem, including:

find_blank(): Locates the position of the blank tile (0).
generate_moves(): Generates all possible moves by sliding the blank tile up, down, left, or right.
trace_path(): Traces back the sequence of moves from the goal state to the initial state once a solution is found.
a_star_search(): Implements the A* search algorithm, where each state is evaluated based on the cost g(n) and the heuristic h(n).
3. print_puzzle(state)
Helper function to print the current state of the puzzle in a readable format.

Requirements
This project requires Python's built-in heapq library for implementing the priority queue.
