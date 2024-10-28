# SearchPathVisualizer
A Python project for visualizing pathfinding algorithms on a graph using both uninformed and informed search methods

Description
PathSearchViz provides an interactive and visual exploration of fundamental search algorithms on graphs. It supports both uninformed (blind) and informed (heuristic-based) search methods, allowing users to see how different algorithms explore paths from a start node to a goal node. This tool is perfect for students, educators, and researchers interested in understanding how various search strategies work in solving graph-based problems.

With PathSearchViz, you can:

Load custom graph data from a file.
Visualize node connections and edge costs.
Highlight the shortest or optimal path discovered by each algorithm.
Observe the step-by-step process in verbose mode to learn more about algorithm behavior.
Key Features
Supported Search Algorithms:
Uninformed: Breadth-First Search (BFS) and Depth-First Search (DFS)
Informed: Best-First Search and A* Search (A* Search)
Graph Visualization: Nodes, edges, and paths are plotted using Matplotlib, with start, goal, and path highlighted for easy interpretation.
Customizable: Load graphs from .txt files and set custom start and goal nodes.
Detailed Path Information: Path found, total path cost, and intermediate exploration steps displayed for enhanced understanding.
Technologies Used
Python
Matplotlib for visualization
Argument parsing for custom configurations via command-line options
