'''
This script serves as the entry point for running graph search algorithms, allowing users to load a graph from a file, specify start and goal nodes, choose a search algorithm, and visualize the resulting path.

Functions:
    - main: Parses command-line arguments, initializes a Searcher instance, performs the specified search, and optionally visualizes the graph.

Usage:
    - Run the script from the command line with options for the filename, start and goal nodes, search algorithm, and verbosity.
    - Supported search algorithms are Breadth-First Search, Depth-First Search, Best-First Search, and A* Search.
    - Optionally use the --plot flag to save the visualized graph with the highlighted path.

Command-Line Arguments:
    --filename: Name of the file containing the graph data (default: "40node.txt").
    --start: Label of the start node in the graph (default: "A").
    --goal: Label of the goal node in the graph (default: "Z").
    --search: Search algorithm to use; choices are "BREADTH", "DEPTH", "BEST", or "A*" (default: "BEST").
    --plot: Flag to save the graph with the highlighted path as an image file.
    --verbose: Flag to enable detailed output during the search process.

Example:
    python main.py --filename "40node.txt" --start "A" --goal "Y" --search "A*" --plot --verbose
    - Loads the graph from "40node.txt", sets "A" as the start and "Y" as the goal node, runs A* Search, and visualizes the path.
'''


from searcher import Searcher
import argparse
import sys


def main():
    # Define the default values for filename, start, and goal
    default_filename = "filename.txt"  # replace with you filename
    default_start = "A"    # Replace with your start node
    default_goal = "Z"     # Replace with your goal node

    parser = argparse.ArgumentParser(description="Run search algorithms.")
    parser.add_argument("--filename", default=default_filename,
                        help="Graph file to load")
    parser.add_argument("--start", default=default_start, help="Start node")
    parser.add_argument("--goal", default=default_goal, help="Goal node")
    parser.add_argument("--search", choices=["BREADTH", "DEPTH", "BEST", "A*"],
                        default="BREADTH", help="Type of search algorithm")
    parser.add_argument("--plot", action="store_true", help="Plot the graph")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")
    args = parser.parse_args()

    # Initialize the Searcher with the provided or default values
    searcher = Searcher(args.filename, args.search, verbose=args.verbose)

    # Validate that start and goal nodes exist in the graph
    if args.start.upper() not in searcher.graph:
        print(f"Error: Start node '{args.start}' not found in the graph.")
        sys.exit(1)
    if args.goal.upper() not in searcher.graph:
        print(f"Error: Goal node '{args.goal}' not found in the graph.")
        sys.exit(1)

    # Set the start and goal nodes
    searcher.setStartGoal(args.start, args.goal)

    # Perform the search and retrieve the path
    path, total_cost = searcher.search_and_reconstruct_path()

    # Display the path and total cost
    if path:
        print(f"Path found: {path}, Total cost: {total_cost}")
    else:
        print("No path found.")

    # Plot the graph if the --plot option is provided
    if args.plot:
        # Replace '*' with an underscore to avoid invalid filename issues
        save_path = f"{args.search.replace('*', 'star')}_{args.filename.replace('.txt', '')}.png"
        searcher.visualize_path(path, save_path=save_path)


if __name__ == "__main__":
    main()
