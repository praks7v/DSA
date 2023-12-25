class Graph:
    def __init__(self):
        self.graph = {}

    def insert_edge(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, start_node):
        visited = set()
        if start_node not in self.graph:
            print(f"{start_node} not present in the graph.")
            return
        stack = [start_node]

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node, end=" ")
                for neighbor in self.graph[current_node]:
                    stack.append(neighbor)


if __name__ == "__main__":
    g = Graph()
    g.insert_edge("A", "B")
    g.insert_edge("A", "C")
    g.insert_edge("C", "D")
    g.insert_edge("D", "E")
    g.insert_edge("E", "G")
    g.insert_edge("B", "F")
    print(g.graph)
    g.dfs("G")
    print()


class Graph:
    def __init__(self):
        """
        Initialize an empty graph represented as an adjacency list.
        """
        self.graph = {}

    def insert_edge(self, v1, v2):
        """
        Insert an undirected edge between two nodes into the graph.
        """
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, start_node):
        """
        Perform Depth-First Search (DFS) traversal starting from a given node.
        Print the visited nodes in the order they are encountered.
        """
        visited = set()
        if start_node not in self.graph:
            print(f"{start_node} not present in the graph.")
            return
        stack = [start_node]

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node, end=" ")
                stack.extend(neighbor for neighbor in self.graph[current_node] if neighbor not in visited)
                # Simple version
                # for neighbor in self.graph[current_node]:
                #     stack.append(neighbor)


if __name__ == "__main__":
    # Example Usage
    g = Graph()
    g.insert_edge("A", "B")
    g.insert_edge("A", "C")
    g.insert_edge("C", "D")
    g.insert_edge("D", "E")
    g.insert_edge("E", "G")
    g.insert_edge("B", "F")

    # Print the graph representation (adjacency list)
    print(g.graph)

    # Perform DFS traversal starting from node 'G'
    g.dfs("G")
    print()
