import heapq
import matplotlib.pyplot as plt
import numpy as np
import random
import math

# 1. UNIQUE FEATURE: RANDOM MAZE GENERATOR
def generate_random_maze(rows, cols, obstacle_probability=0.3):
    """Creates a grid where 1s are walls based on probability."""
    maze = [[1 if random.random() < obstacle_probability else 0 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0        # Ensure Start is clear
    maze[rows-1][cols-1] = 0  # Ensure Goal is clear
    return maze

# 2. UNIQUE FEATURE: MULTIPLE HEURISTICS
def get_heuristic(a, b, choice):
    if choice == '1': # Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    else: # Euclidean
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def a_star(maze, start, goal, h_choice):
    neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start: get_heuristic(start, goal, h_choice)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1], close_set

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
                if maze[neighbor[0]][neighbor[1]] == 1:
                    continue
            else:
                continue
                
            tentative_g_score = gscore[current] + 1
            
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + get_heuristic(neighbor, goal, h_choice)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
                
    return False, close_set

# --- USER INTERFACE ---
print("--- Syntecxhub Advanced Maze Solver ---")
print("Generating maze...")
h_choice = input("Choose Heuristic (1: Manhattan, 2: Euclidean): ")
size = 15 # You can increase this for a bigger maze
maze = generate_random_maze(size, size, obstacle_probability=0.25)
start, goal = (0, 0), (size-1, size-1)

print("Running A* algorithm...")
path, explored = a_star(maze, start, goal, h_choice)
print("Algorithm completed!")

# 3. UNIQUE FEATURE: VISUALIZING THE "THINKING" (Explored Nodes)
if path:
    print(f"Path found! Nodes explored: {len(explored)}")
    maze_np = np.array(maze)
    plt.figure(figsize=(8,8))
    plt.imshow(maze_np, cmap='binary')
    
    # Plot explored nodes (The AI's 'thinking' process)
    ex_x, ex_y = zip(*explored)
    plt.scatter(ex_y, ex_x, color='yellow', s=10, alpha=0.3, label='Explored')
    
    # Plot final path
    px, py = zip(*path)
    plt.plot(py, px, color='red', linewidth=3, label='Shortest Path')
    
    plt.scatter(start[1], start[0], color='green', s=100, label='Start')
    plt.scatter(goal[1], goal[0], color='blue', s=100, label='Goal')
    plt.title(f"A* Solver ({'Manhattan' if h_choice=='1' else 'Euclidean'})")
    plt.legend()
    plt.show()
else:
    print("No path found. Try running again to generate a new maze!")