class Graph:
    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}

    def add_node(self, v):
        """
        Adds a node 'v' to the graph if it is not already present.

        Args:
        - v: The node to be added.
        """
        if v in self.graph:
            print(f"{v} is already present in the graph.")
        else:
            self.graph[v] = []

    def add_edge(self, v1, v2, cost):
        """
        Adds an edge between nodes 'v1' and 'v2' with the given cost.

        Args:
        - v1: The first node.
        - v2: The second node.
        - cost: The cost or weight of the edge.
        """
        if v1 not in self.graph:
            print(f"{v1} not in the graph.")
        elif v2 not in self.graph:
            print(f"{v2} not in the graph.")
        else:
            edge1 = [v2, cost]
            edge2 = [v1, cost]
            self.graph[v1].append(edge1)
            self.graph[v2].append(edge2)

    def del_node(self, v):
        """
        Deletes a node 'v' from the graph.

        Args:
        - v: The node to be removed.
        """
        if v not in self.graph:
            print(f"{v} not present in the graph.")
        else:
            del self.graph[v]
            for node in self.graph:
                edges = self.graph[node]
                for edge in edges[:]:  # Using [:] to create a copy for safe iteration while removing
                    if v == edge[0]:
                        edges.remove(edge)
                        break

    def del_edge(self, v1, v2, cost):
        """
        Deletes the edge between nodes 'v1' and 'v2' with the given cost.

        Args:
        - v1: The first node.
        - v2: The second node.
        - cost: The cost or weight of the edge.
        """
        if v1 not in self.graph:
            print(f"{v1} not present in the graph.")
        elif v2 not in self.graph:
            print(f"{v2} not present in the graph.")
        else:
            edge1 = [v2, cost]
            edge2 = [v1, cost]
            if edge1 in self.graph[v1]:
                self.graph[v1].remove(edge1)
                self.graph[v2].remove(edge2)

    def print_graph(self):
        """
        Prints the current state of the graph.
        """
        print("Graph:", self.graph)


# Example usage:
if __name__ == "__main__":
    graph_obj = Graph()
    graph_obj.add_node("A")
    graph_obj.add_node("B")
    graph_obj.add_node("C")
    graph_obj.add_edge("A", "B", 4)
    graph_obj.add_edge("A", "C", 3)
    graph_obj.add_edge("B", "C", 5)
    graph_obj.print_graph()

    # Uncomment the line below to test deleting a node
    # graph_obj.del_node("A")

    graph_obj.del_edge('A', 'B', 4)
    graph_obj.print_graph()
