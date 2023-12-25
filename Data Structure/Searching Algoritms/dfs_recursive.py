class Graph:
    def __init__(self):
        # Initialization: Creates an empty graph represented as a dictionary.
        self.graph = {}

    def insert_edge(self, start, end):
        # Inserts an undirected edge between two nodes in the graph.
        if start not in self.graph:
            self.graph[start] = []  # If start node not in graph, add it with an empty list as its neighbors.
        if end not in self.graph:
            self.graph[end] = []    # If end node not in graph, add it with an empty list as its neighbors.

        self.graph[start].append(end)  # Add end as a neighbor of start.
        self.graph[end].append(start)  # Add start as a neighbor of end.

    def dfs(self, start_node):
        # Performs Depth-First Search (DFS) starting from a specified node.
        visited = set()  # Set to keep track of visited nodes.

        def dfs_recursive(node):
            # Inner recursive function to perform DFS traversal.
            visited.add(node)         # Mark the current node as visited.
            print(node, end=" ")      # Print the current node.

            for neighbor in self.graph.get(node, []):
                # Iterate through neighbors of the current node.
                if neighbor not in visited:
                    dfs_recursive(neighbor)  # Recursively call DFS on unvisited neighbors.

        dfs_recursive(start_node)  # Start DFS from the specified node.


if __name__ == "__main__":
    g = Graph()
    g.insert_edge("A", "B")
    g.insert_edge("A", "C")
    g.insert_edge("B", "C")
    g.insert_edge("C", "D")
    g.insert_edge("C", "F")
    g.insert_edge("A", "F")
    g.insert_edge("B", "D")
    g.insert_edge("F", "G")

    print("DFS traversal starting from 'A':")
    g.dfs("A")  # Initiate DFS traversal starting from node 'A'.
    print()
