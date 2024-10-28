# Graph Search Visualizer

A Python project for visualizing graph search algorithms on custom graphs loaded from files. This tool allows users to explore four different search algorithms (Breadth-First Search, Depth-First Search, Best-First Search, and A* Search), visualize the search process, and highlight paths between a start and goal node.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)


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
https://github.com/rubino1996/SearchPathVisualizer.git

2. Ensure you have the matplotlib.pyplot library

## Usage
After cloning the repository, you can run the graph search visualizer from the command line by specifying the graph file, start node, goal node, and search algorithm. The program offers the option to save a plot of the graph with the path found, if any, as a .png file.

Command Line Arguments:
1. python main.py --filename <graph_file> --start <start_node> --goal <goal_node> --search <algorithm> [--plot] [--verbose]
2. --filename : The name of the text file containing the graph data (e.g., 40node.txt). 
3. --start : The starting node in the graph.
4. --goal : The goal node in the graph.
5. --search : The search algorithm to use. Choose from BREADTH, DEPTH, BEST, or A*.
6. --plot : Optional. Adds this flag to save the graph visualization with the highlighted path as a .png file.
7. --verbose : Optional. Adds this flag for detailed step-by-step output of the search process.

File Format Guidelines:
To ensure the program reads the graph correctly, save the .txt file in the following format, where each line defines an edge between two nodes with specific coordinates and cost:

- ('Node1', 'Node2', cost, [x1, y1], [x2, y2])

For example:
- ('A', 'B', 1, [2, 3], [4, 5])
- ('B', 'C', 2, [4, 5], [6, 7])
- ('C', 'D', 3, [6, 7], [8, 9])

## Example
Assume you have a file 40node.txt formatted for the graph structure, and you want to find a path from node A to node Y using A* Search. To do this, you can run the following command:
python main.py --filename "40node.txt" --start "A" --goal "Y" --search "A*" --plot --verbose

This command will:
- Load the graph data from 40node.txt.
- Set A as the start node and Y as the goal node.
- Use the A* Search algorithm to find a path.
- Display detailed search steps in the console.
- Save the resulting graph with the highlighted path as a .png file (e.g., Astar_40node.png).

Here is an example visualization for A* search method in a 40 node:
![A-star Example](https://github.com/rubino1996/SearchPathVisualizer/blob/main/Astar_40node.png)
