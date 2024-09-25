import heapq

# Manhattan Distance Heuristic Function
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Exclude the empty tile (0)
                x, y = divmod(state[i][j] - 1, 3)  # Get goal position of current tile
                distance += abs(i - x) + abs(j - y)
    return distance

# Puzzle Class
class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    # Find Blank Tile (0)
    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    # Generate Possible Moves (Swapping Blank Tile)
    def generate_moves(self, state):
        x, y = self.find_blank(state)
        moves = []
        directions = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]
        for direction, dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in state]  # Create a copy of the current state
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                moves.append(new_state)
        return moves

    # Trace the Path Back to the Initial State
    def trace_path(self, came_from, current_state):
        path = []
        while current_state:
            path.append(current_state)
            current_state = came_from.get(tuple(tuple(row) for row in current_state))
        path.reverse()
        return path

    ############## Implement the A* Search Algorithm here ################################################
    def a_star_search(self):
         priority_queue = []
         heapq.heappush(priority_queue, (manhattan_distance(self.initial_state, self.goal_state), self.initial_state))
         g_score = {tuple(tuple(row) for row in self.initial_state): 0}
         came_from = {tuple(tuple(row) for row in self.initial_state): None}
         while(priority_queue):
            _, current_state = heapq.heappop(priority_queue)

            if current_state == self.goal_state:
                print("Solution found!")
                return self.trace_path(came_from, current_state)
            
            for newState in self.generate_moves(current_state):
                neighbor_tuple = tuple(tuple(row) for row in newState)
                tentative_g_score = g_score[tuple(tuple(row) for row in current_state)] + 1
                if neighbor_tuple in g_score and tentative_g_score >= g_score.get(neighbor_tuple, float('inf')):
                  continue
                came_from[neighbor_tuple] = current_state
                g_score[neighbor_tuple] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(newState, self.goal_state)
                if neighbor_tuple not in [x[1] for x in priority_queue]:
                  heapq.heappush(priority_queue, (f_score, newState))
         return None

# Function to Print Puzzle State
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Main Code
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]



puzzle = Puzzle(initial_state, goal_state)
solution_path = puzzle.a_star_search()

if solution_path:
    print("Steps to solve the puzzle:")
    for i, step in enumerate(solution_path):
        print(f"Step {i}:")
        print_puzzle(step)