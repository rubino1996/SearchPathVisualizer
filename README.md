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
