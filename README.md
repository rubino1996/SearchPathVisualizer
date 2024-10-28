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


# Graph Search Visualizer

A Python project for visualizing graph search algorithms on custom graphs loaded from files. This tool allows users to explore four different search algorithms (Breadth-First Search, Depth-First Search, Best-First Search, and A* Search), visualize the search process, and highlight paths between a start and goal node.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command-Line Arguments](#command-line-arguments)
- [File Format](#file-format)
- [Example](#example)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [License](#license)

## Overview
This project was developed to help visualize graph traversal and pathfinding algorithms in Python. Given a graph file in a specified format, users can select a start and goal node and run any of the available search algorithms to find and highlight a path if one exists. The visualization is saved as a `.png` file.

## Features
- Supports four search algorithms:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Best-First Search
  - A* Search
- Visualizes the graph and highlights the path found
- Saves the graph visualization with the path as a `.png` file
- Command-line options for flexibility in choosing the graph file, start/goal nodes, and verbosity

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/graph-search-visualizer.git
   cd graph-search-visualizer
