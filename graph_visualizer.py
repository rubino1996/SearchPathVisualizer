'''
The GraphVisualizer class is designed to load a graph from a file, manage nodes and edges, and visualize the graph with optional path highlighting.

Classes:
    - GraphVisualizer: Provides methods for loading a graph from a file, marking start/goal nodes, marking a path, and visualizing the graph.

GraphVisualizer:
    Attributes:
        - nodes (list): A list of Node objects representing vertices in the graph.
        - edges (list): A list of Edge objects representing connections between nodes.
        - node_map (dict): A dictionary mapping node labels to Node objects for efficient lookup.
        - marked_nodes (set): A set of nodes marked as start or goal, primarily for visualization.
        - marked_edges (set): A set of edges marked as part of the path, for visualization purposes.

    Methods:
        - load_graph_from_file: Reads a graph file and populates nodes and edges, interpreting each line based on a regex pattern.
        - mark_start: Marks a node as the start for visualization.
        - mark_goal: Marks a node as the goal for visualization.
        - mark_path: Marks the edges in a specified path for visualization.
        - plot: Displays the graph, highlighting any marked path, and optionally saves the plot as an image.
        - save: Saves the current plot to a specified filename.

Usage:
    - Load a graph from a file using `load_graph_from_file`.
    - Mark start and goal nodes with `mark_start` and `mark_goal`.
    - Optionally, highlight a path using `mark_path`.
    - Visualize the graph with `plot`, optionally saving the image.
'''


import re
from graph_elements import Node, Edge
import matplotlib.pyplot as plt


class GraphVisualizer:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.node_map = {}
        self.marked_nodes = set()
        self.marked_edges = set()

    def load_graph_from_file(self, filename):
        # Regex pattern to match the expected line format
        pattern = re.compile(
            r"\('(.+?)', '(.+?)', (\d+), \[(\d+), (\d+)\], \[(\d+), (\d+)\]\)")

        with open(filename, 'r') as file:
            for line in file:
                match = pattern.match(line.strip())
                if match:
                    try:
                        # Extract components based on regex groups
                        node1, node2, cost = match.group(
                            1), match.group(2), int(match.group(3))
                        x1, y1 = int(match.group(4)), int(match.group(5))
                        x2, y2 = int(match.group(6)), int(match.group(7))

                        # Create nodes and add to node_map if not already present
                        if node1 not in self.node_map:
                            self.node_map[node1] = Node(x1, y1, label=node1)
                            self.nodes.append(self.node_map[node1])
                        if node2 not in self.node_map:
                            self.node_map[node2] = Node(x2, y2, label=node2)
                            self.nodes.append(self.node_map[node2])

                        # Create and store the edge
                        new_edge = Edge(
                            self.node_map[node1], self.node_map[node2], cost)
                        new_edge.set_labels(node1, node2)
                        self.edges.append(new_edge)

                    except ValueError as e:
                        print(f"Error parsing line '{line}': {e}")
                else:
                    print(f"Skipping malformed line: {line.strip()}")

    def mark_start(self, label):
        self.marked_nodes.add(label)

    def mark_goal(self, label):
        self.marked_nodes.add(label)

    def mark_path(self, path):
        for i in range(len(path) - 1):
            self.marked_edges.add((path[i], path[i + 1]))

    def plot(self, path=None, save_path=None):
        plt.figure()
        plt.title("Graph with Path Highlighted")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        # Plot nodes
        for node in self.nodes:
            plt.plot(node.x, node.y, 'o', color="black")
            plt.text(node.x, node.y, node.label, color="blue", fontsize=12)

        # Plot edges
        for edge in self.edges:
            plt.plot([edge.node1.x, edge.node2.x], [
                     edge.node1.y, edge.node2.y], color="blue")
            mid_x = (edge.node1.x + edge.node2.x) / 2
            mid_y = (edge.node1.y + edge.node2.y) / 2
            plt.text(mid_x, mid_y, str(edge.cost), color="green", fontsize=10)

        # Highlight path if provided
        if path:
            for i in range(len(path) - 1):
                start_node = self.node_map[path[i]]
                end_node = self.node_map[path[i + 1]]
                plt.plot(
                    [start_node.x, end_node.x], [start_node.y, end_node.y],
                    color="red", linewidth=2, zorder=5
                )

        # Save or show the plot based on save_path
        if save_path:
            plt.savefig(save_path, format='png')
            print(f"Graph with path saved as: {save_path}")

        plt.show()  # Show after saving to ensure it doesn't overwrite the saved file

    def save(self, filename):
        plt.savefig(filename)
