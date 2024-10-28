'''
The Searcher class provides a framework for executing and visualizing various graph search algorithms on a graph loaded from a file.

Classes:
    - Searcher: Manages graph structure, executes search algorithms, and supports visualization.

Searcher:
    Attributes:
        - filename (str): Name of the file from which to load the graph.
        - searchType (str): Type of search algorithm to use (e.g., BFS, DFS, Best-First, A*).
        - verbose (bool): Controls verbose output.
        - graph (dict): Adjacency list of nodes and edges.
        - heuristics (dict): Dictionary storing heuristic values for nodes (used in A* and Best-First search).
        - node_coordinates (dict): Dictionary mapping node labels to their coordinates.
        - OPEN (list): List of nodes currently open for exploration.
        - visualizer (GraphVisualizer): Visualizer instance to manage and display the graph.

    Methods:
        - load_graph: Loads a graph from a file and populates attributes like nodes, edges, and heuristics.
        - setStartGoal: Sets the start and goal nodes for the search.
        - search: Executes the specified search algorithm.
        - plot_graph: Generates a visualization of the graph.
        - bfs: Implements Breadth-First Search.
        - dfs: Implements Depth-First Search.
        - best_first_search: Implements Best-First Search with heuristic-based prioritization.
        - a_star_search: Implements A* Search with g-cost and h-cost computation.
        - visualize_path: Highlights the start, goal, and path on the graph visualization.
        - reconstruct_path: Rebuilds the path from the goal to the start node and calculates total path cost.
        - calculate_actual_cost_from_node: Calculates the cost from a given node to the goal.

Usage:
    - Initialize a Searcher with a filename and search type.
    - Set start and goal nodes using setStartGoal.
    - Call search to execute the specified search type.
    - Use visualize_path to display the graph with the chosen path highlighted.
'''


from graph_visualizer import GraphVisualizer
import matplotlib.pyplot as plt
import math


def reconstruct_path(parent, start, goal, graph):
    """Reconstruct the path from start to goal using the parent relationship and calculate path cost."""
    path = []
    current = goal
    total_cost = 0
    while current != start:
        path.append(current)
        previous = parent.get(current)
        if previous:
            # Add the cost between current and previous nodes to total_cost
            for neighbor in graph[previous]:
                if neighbor.label == current:
                    total_cost += neighbor.value  # Add edge weight
        current = previous
    path.append(start)
    path.reverse()
    return path, total_cost  # Return both path and total cost


class SearchNode:
    def __init__(self, label, value=0):
        self.label = label
        self.value = value

    def __repr__(self):
        return f"({self.label}, {self.value})"


class Searcher:
    # Default searchType: "Breadth"
    def __init__(self, filename, searchType="BREADTH", verbose=False):
        self.filename = filename
        self.searchType = searchType
        self.verbose = verbose  # Verbose mode toggle
        self.graph = {}
        self.heuristics = {}
        self.node_coordinates = {}
        self.OPEN = []
        self.visualizer = GraphVisualizer()
        print(
            f"Loaded search type {self.searchType.upper()} with map in file: {self.filename}")

        self.load_graph()
        self.visualizer.load_graph_from_file(filename)

    def setStartGoal(self, start_node, goal_node):
        """Set the start and goal nodes for the search."""
        self.start_node = start_node.upper()
        self.goal_node = goal_node.upper()
        print(f"Start: {self.start_node}, Goal: {self.goal_node}")

    def load_graph(self):
        """Read the graph from the given filename and populate self.graph and heuristic values."""
        with open(self.filename, 'r') as file:
            for line in file:
                parts = eval(line.strip())
                node = parts[0].upper()  # Convert to uppercase for consistency
                # Convert to uppercase for consistency
                neighbor = parts[1].upper()
                weight = parts[2]
                node_coords = parts[3]
                neighbor_coords = parts[4]

                # Add nodes and neighbors to the graph
                if node not in self.graph:
                    self.graph[node] = []
                if neighbor not in self.graph:
                    self.graph[neighbor] = []

                # Add both directions (bidirectional graph)
                self.graph[node].append(SearchNode(neighbor, value=weight))
                self.graph[neighbor].append(SearchNode(node, value=weight))

                # Store node coordinates
                self.node_coordinates[node] = node_coords
                self.node_coordinates[neighbor] = neighbor_coords

                # Initialize the heuristic values for both nodes
                if node not in self.heuristics:
                    self.heuristics[node] = {}
                if neighbor not in self.heuristics:
                    self.heuristics[neighbor] = {}

                # Add heuristic value (weight) between node and neighbor
                self.heuristics[node][neighbor] = weight
                self.heuristics[neighbor][node] = weight  # Reverse heuristic

    def euclidean_distance(self, node1, node2):
        """Calculate the Euclidean distance between two nodes."""
        coord1 = self.node_coordinates[node1]
        coord2 = self.node_coordinates[node2]
        return math.sqrt(((coord2[0] - coord1[0]) ** 2) + ((coord2[1] - coord1[1]) ** 2))

        return distance

    def show_open_list(self):
        """Display the nodes in the OPEN list if verbose is enabled."""
        if self.verbose:
            print(f"\nCurrent OPEN List: {self.format_open_list()}")

    def format_open_list(self):
        """Format the OPEN list for debugging across different search types."""
        formatted_list = []
        for node in self.OPEN:
            # For A*, use g_cost and h_cost; otherwise, just show the node label
            if hasattr(self, 'g_costs'):
                # This section is specific to A* search
                g_cost = self.g_costs.get(node.label, float('inf'))
                h_cost = (
                    self.euclidean_distance(node.label, self.goal_node)
                    if node.label in self.node_coordinates and self.goal_node in self.node_coordinates
                    else float('inf')
                )
                f_cost = g_cost + h_cost
                formatted_list.append(
                    f"{node.label};{g_cost};{h_cost:.2f};{f_cost:.2f}")
            else:
                # For BFS and DFS, just display the node label
                formatted_list.append(f"{node.label}")

        return formatted_list

    def search(self):
        """Perform the specified search algorithm."""
        if self.searchType == "BREADTH":
            self.bfs(self.start_node, self.goal_node)
        elif self.searchType == "DEPTH":
            self.dfs(self.start_node, self.goal_node)
        elif self.searchType == "BEST":
            self.best_first_search(self.start_node, self.goal_node)
        elif self.searchType == "A*":
            self.a_star_search(self.start_node, self.goal_node)
        else:
            print("Invalid search type specified.")

    def plot_graph(self, save_path=None):
        """Plot the graph and optionally save it as an image with the number of nodes as the title."""

        # Extract the file name without extension and use it as the title
        # Extracts the file name, e.g., '40node.txt'
        file_name = os.path.basename(self.filename)
        # Removes the file extension, leaving '40node'
        graph_title = os.path.splitext(file_name)[0]

        plt.figure(figsize=(8, 8))

        # Plot the nodes
        for node, coords in self.node_coordinates.items():
            plt.scatter(coords[0], coords[1], label=node)
            plt.text(coords[0], coords[1], node, fontsize=12, ha='right')

        # Plot the edges
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                node_coords = self.node_coordinates[node]
                neighbor_coords = self.node_coordinates[neighbor.label]
                plt.plot([node_coords[0], neighbor_coords[0]],
                         [node_coords[1], neighbor_coords[1]], 'b-')

        plt.title(graph_title)  # Set the title to the extracted file name
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)

        # Save the plot if a save path is provided
        if save_path:
            plt.savefig(save_path)
            print(f"Graph saved as {save_path}")
        else:
            plt.show()

    def bfs(self, start, goal):
        """Breadth-First Search algorithm with consistent parent tracking."""
        visited = set()
        parent = {start: None}
        queue = [SearchNode(start, 0)]

        if self.verbose:
            print("\nBFS: ")

        while queue:
            current_node = queue.pop(0)
            if self.verbose:
                print(f"Exploring node: {current_node.label}")

            if current_node.label in visited:
                continue

            visited.add(current_node.label)
            if current_node.label == goal:
                # Get the final path and its total cost
                final_path, path_cost = reconstruct_path(
                    parent, start, goal, self.graph)
                if self.verbose:
                    print(f"Success! Reached goal node {goal}")
                print(f"Path to goal: {final_path}")
                print(f"Total path cost: {path_cost}")  # Print the total cost
                return final_path, path_cost  # Return both path and total cost

            children = [
                neighbor for neighbor in self.graph[current_node.label]
                if neighbor.label not in visited and neighbor.label not in parent
            ]

            for child in children:
                if child.label not in parent:
                    parent[child.label] = current_node.label

            # Sorting children alphabetically
            children.sort(key=lambda x: x.label)

            if self.verbose:
                print(
                    f"Inserting new children: {[child.label for child in children]}")

            queue.extend(children)

            # Updating the OPEN list
            self.OPEN = [SearchNode(label=node.label, value=node.value)
                         for node in queue]
            self.show_open_list()

        # If goal is not found, return an empty path and zero cost
        return [], 0

    def dfs(self, start, goal):
        """Depth-First Search algorithm with consistent parent tracking."""
        visited = set()
        parent = {start: None}
        stack = [SearchNode(start, 0)]

        if self.verbose:
            print("\nDFS: ")

        while stack:
            current_node = stack.pop(0)
            if self.verbose:
                print(f"Exploring node: {current_node.label}")

            if current_node.label in visited:
                continue

            visited.add(current_node.label)
            if current_node.label == goal:
                # Get the final path and its total cost
                final_path, path_cost = reconstruct_path(
                    parent, start, goal, self.graph)
                if self.verbose:
                    print(f"Success! Reached goal node {goal}")
                print(f"Path to goal: {final_path}")
                print(f"Total path cost: {path_cost}")  # Print the total cost
                return final_path, path_cost  # Return both path and total cost

            children = [neighbor for neighbor in self.graph[current_node.label]
                        if neighbor.label not in visited]
            children.sort(key=lambda x: x.label)
            if self.verbose:
                print(
                    f"Inserting new children: {[child.label for child in children]}")

            for child in reversed(children):
                stack.insert(0, child)
                parent[child.label] = current_node.label

            self.OPEN = [SearchNode(label=node.label, value=node.value)
                         for node in stack]
            self.show_open_list()

        # If goal is not found, return an empty path and zero cost
        return [], 0

    def best_first_search(self, start, goal):
        """Best-First Search algorithm with correct child insertion and path reconstruction."""
        visited = set()
        parent = {start: None}
        priority_queue = [(start, 0)]  # (Node, Heuristic value)

        if self.verbose:
            print("\nBestFS :")

        while priority_queue:
            # Sort by heuristic value (ascending order) and pop the node with the smallest value
            priority_queue.sort(key=lambda x: x[1])
            current_node, _ = priority_queue.pop(0)

            if self.verbose:
                print(f"Exploring node: {current_node}")

            # If goal is reached, reconstruct the path and return
            if current_node == goal:
                final_path, path_cost = reconstruct_path(
                    parent, start, goal, self.graph)
                if self.verbose:
                    print(f"Success! Reached goal node {goal}")
                print(f"Path to goal: {final_path}")
                print(f"Total path cost: {path_cost}")  # Print the total cost
                return final_path, path_cost  # Return both path and total cost

            # Mark the current node as visited
            visited.add(current_node)

            # Gather all unvisited children and sort them by heuristic values
            children = [neighbor for neighbor in self.graph[current_node]
                        if neighbor.label not in visited]

            if self.verbose and children:
                print(
                    f"Inserting new children: {[child.label for child in children]}")

            # Insert children into the priority queue based on their heuristic values
            for child in children:
                if child.label not in parent:
                    # Set the parent relation
                    parent[child.label] = current_node

                # Calculate the heuristic value for the child
                heuristic_value = self.heuristics[current_node][child.label]

                # Add the child to the priority queue if not already present
                in_queue = [
                    node for node in priority_queue if node[0] == child.label]
                if not in_queue:
                    priority_queue.append((child.label, heuristic_value))
                else:
                    # If child already in queue with a higher heuristic, update the value
                    for idx, (node_label, heuristic) in enumerate(priority_queue):
                        if node_label == child.label and heuristic > heuristic_value:
                            priority_queue[idx] = (
                                child.label, heuristic_value)

            # Update the OPEN list for verbose output
            self.OPEN = [SearchNode(n[0], n[1]) for n in priority_queue]
            self.show_open_list()

        # If goal is not found, return an empty path and zero cost
        return [], 0

    def a_star_search(self, start, goal):
        """A* Search algorithm with admissibility check."""
        visited = set()
        priority_queue = [(start, 0)]
        self.g_costs = {start: 0}  # Initialize self.g_costs here
        self.parent = {start: None}

        if self.verbose:
            print("\nA*: ")

        while priority_queue:
            # Sort the priority queue by f_cost and pop the node with the lowest cost
            priority_queue.sort(key=lambda x: x[1])
            current_node, current_f_cost = priority_queue.pop(0)

            if self.verbose:
                print(f"Exploring node: {current_node}")

            if current_node == goal:
                final_path, total_cost = reconstruct_path(
                    self.parent, start, goal, self.graph)
                if self.verbose:
                    print(f"Success! Reached goal node {goal}")
                print(f"Path to goal: {final_path}")
                print(f"Total path cost: {total_cost}")
                return final_path, total_cost

            visited.add(current_node)

            # Explore all unvisited neighbors
            children = [neighbor for neighbor in self.graph[current_node]
                        if neighbor.label not in visited]

            for neighbor in children:
                # Calculate tentative g_cost
                tentative_g_cost = self.g_costs[current_node] + neighbor.value

                # Calculate heuristic value (h_cost) directly with Euclidean distance if necessary
                if neighbor.label in self.node_coordinates and goal in self.node_coordinates:
                    heuristic_value = self.euclidean_distance(
                        neighbor.label, goal)
                else:
                    heuristic_value = float('inf')

                f_cost = tentative_g_cost + heuristic_value

                # Only add to queue if this path is better
                if neighbor.label not in self.g_costs or tentative_g_cost < self.g_costs[neighbor.label]:
                    self.g_costs[neighbor.label] = tentative_g_cost
                    self.parent[neighbor.label] = current_node

                    # Update or add neighbor in the priority queue
                    priority_queue = [
                        (n, cost) for n, cost in priority_queue if n != neighbor.label]
                    priority_queue.append((neighbor.label, f_cost))

            # Update the OPEN list for debugging
            self.OPEN = [SearchNode(n[0], n[1]) for n in priority_queue]
            self.show_open_list()

    def calculate_actual_cost_from_node(self, node, goal):
        """
        Calculate the actual cost from a given node to the goal by performing a search.
        """
        # Use reconstruct_path to calculate the cost from the node to the goal
        path, cost = reconstruct_path(self.parent, node, goal, self.graph)
        return cost

    def search_and_reconstruct_path(self):
        """Perform the specified search algorithm and return the path and total cost."""
        path = None
        total_cost = 0
        if self.searchType == "BREADTH":
            path, total_cost = self.bfs(self.start_node, self.goal_node)
        elif self.searchType == "DEPTH":
            path, total_cost = self.dfs(self.start_node, self.goal_node)
        elif self.searchType == "BEST":
            path, total_cost = self.best_first_search(
                self.start_node, self.goal_node)
        elif self.searchType == "A*":
            path, total_cost = self.a_star_search(
                self.start_node, self.goal_node)
        else:
            print("Invalid search type specified.")
            return None, None

        if path:
            print(f"Path to goal: {path}")
            print(f"Total path cost: {total_cost}")
        return path, total_cost

    def visualize_path(self, path, save_path=None):
        """Visualize the graph with the search path highlighted."""
        self.visualizer.mark_start(self.start_node)
        self.visualizer.mark_goal(self.goal_node)
        self.visualizer.mark_path(path)  # Ensure path is highlighted
        # Save and display handled in plot
        self.visualizer.plot(path=path, save_path=save_path)
