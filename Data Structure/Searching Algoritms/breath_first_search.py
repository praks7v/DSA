class Graph:
    def __init__(self):
        # Initialize an empty dictionary to represent the graph.
        self.graph = {}

    def insert_edge(self, start, end):
        # Ensure that both start and end nodes are in the graph.
        if start not in self.graph:
            self.graph[start] = []
        if end not in self.graph:
            self.graph[end] = []

        # Add the edge between start and end nodes.
        self.graph[start].append(end)
        self.graph[end].append(start)

    def bfs(self, start_node):
        # Set to keep track of visited nodes.
        visited = set()

        # Check if the start_node is present in the graph.
        if start_node not in self.graph:
            print(f"{start_node} not present in the graph.")
            return

        # Initialize a queue with the start_node.
        queue = [start_node]

        # BFS traversal.
        while queue:
            # Get the current node from the front of the queue.
            current_node = queue.pop(0)

            # Process the current node if not visited.
            if current_node not in visited:
                visited.add(current_node)
                print(current_node, end=" ")

                # Add neighbors of the current node to the queue.
                for neighbor in self.graph[current_node]:
                    queue.append(neighbor)


# Main part of the code
if __name__ == "__main__":
    # Create an instance of the Graph class.
    g = Graph()

    # Insert edges to build the graph.
    g.insert_edge("A", "B")
    g.insert_edge("A", "C")
    g.insert_edge("B", "D")
    g.insert_edge("C", "D")
    g.insert_edge("D", "E")
    g.insert_edge("E", "F")
    g.insert_edge("F", "D")

    # Perform BFS traversal starting from node "A".
    g.bfs("A")
