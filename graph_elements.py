'''
The Node and Edge classes represent the fundamental components of a graph structure, often used in visualization or pathfinding algorithms.

Classes:
    - Node: Represents a single point or vertex in the graph with x and y coordinates and a label.
    - Edge: Represents a connection between two nodes with an associated cost.

Node:
    Attributes:
        - x (int/float): The x-coordinate of the node.
        - y (int/float): The y-coordinate of the node.
        - label (str): A unique label or identifier for the node.

    Methods:
        - __repr__: Returns a string representation of the Node in the format "Node(label: (x, y))".

Edge:
    Attributes:
        - node1 (Node): The first node (or vertex) in the edge.
        - node2 (Node): The second node (or vertex) in the edge.
        - cost (int/float): The weight or cost associated with traversing this edge.
        - label1 (str): Label of the first node (optional, can be set later).
        - label2 (str): Label of the second node (optional, can be set later).

    Methods:
        - __init__: Initializes an Edge, converting node1 and node2 from tuples to Node instances if they are provided as coordinates.
        - set_labels: Sets the labels for the two nodes connected by this edge, useful for referencing during visualization.
'''


class Node:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __repr__(self):
        return f"Node({self.label}: ({self.x}, {self.y}))"


class Edge:
    def __init__(self, node1, node2, cost):
        # Check if node1 and node2 are tuples, and convert them to Node instances if they are
        if isinstance(node1, tuple):
            node1 = Node(node1[0], node1[1], label="")  # Convert tuple to Node
        if isinstance(node2, tuple):
            node2 = Node(node2[0], node2[1], label="")  # Convert tuple to Node

        self.node1 = node1
        self.node2 = node2
        self.cost = cost
        self.label1 = None
        self.label2 = None

    def set_labels(self, label1, label2):
        """Set labels for the nodes connected by this edge."""
        self.label1 = label1
        self.label2 = label2
