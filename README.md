
# Syntecxhub-Maze-Solver
🚀 AI Maze Solver - A* Search Algorithm
Syntecxhub Internship | Project - 1

This repository contains an intelligent pathfinding agent developed as part of my Artificial Intelligence internship. The solver uses the A Search Algorithm* to find the most efficient path between two points in a dynamically generated grid filled with obstacles.

🌟 Key Features      
1.Dynamic Maze Generation: Generates a random 15x15 grid with a customizable obstacle probability (default 20%).  

2.Heuristic Analysis: Implements a choice between Manhattan Distance ($L1$ norm) and Euclidean Distance ($L2$ norm) to compare search efficiency.

3.Advanced Visualization:
Red Line: Represents the final optimal path.                                                                           
Yellow Dots: Visualizes the "Explored Nodes," showing exactly how the AI "thought" through the maze.     
Black/White Grid: Clearly distinguishes between walls and walkable paths.  

4.Automatic Retries: Includes logic to ensure the generated maze is solvable before attempting to display results.

🛠️ Tech Stack
Language: Python 3.13

Libraries:

Matplotlib: For real-time path visualization.

NumPy: For efficient grid manipulations.

Heapq: To manage the priority queue for the A* open set.

📖 How It Works
The A* algorithm uses a heuristic-based approach to navigate the grid. It calculates the priority of each node using the formula: f(n) = g(n) + h(n)

g(n): The cost to reach the current node from the start.
h(n): The estimated cost to reach the goal (heuristic).

🚀 Installation & Usage
1.Clone the repository:

Bash:
git clone https://github.com/vaishnaviibhaltand28/Syntecxhub-Maze-Solver.git

2.Install Dependencies:

Bash:
pip install matplotlib numpy

3.Execute the Solver:

Bash:
python maze_solver.py

4.Interact: Enter 1 for Manhattan or 2 for Euclidean distance when prompted in the terminal.

📊 Sample Results
During testing, the algorithm successfully navigated the grid by exploring 125 nodes using the Manhattan heuristic, demonstrating high search efficiency.
