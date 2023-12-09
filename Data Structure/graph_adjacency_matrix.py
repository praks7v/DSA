import networkx as nx
import matplotlib.pyplot as plt


class GraphAdjacencyMatrix:
    """
    A class representing a graph using an adjacency matrix.

    Attributes:
    - graph: 2D list representing the adjacency matrix of the graph.
    - nodes: List containing the nodes of the graph.
    - node_count: Number of nodes in the graph.

    Methods:
    - __init__(): Initializes an empty graph.
    - add_node(v): Adds a node 'v' to the graph.
    - add_edge(v1, v2, cost): Adds an undirected edge between nodes 'v1' and 'v2' with the given cost.
    - del_node(v): Removes a node 'v' from the graph.
    - del_edge(v1, v2): Removes the edge between nodes 'v1' and 'v2'.
    - print_matrix(): Prints the adjacency matrix of the graph.
    - draw_graph(filename): Draws and saves the graph visualization using NetworkX and Matplotlib.

    Usage:
    graph_ad_matrix = GraphAdjacencyMatrix()
    graph_ad_matrix.add_node('A')
    graph_ad_matrix.add_node('B')
    graph_ad_matrix.add_edge('A', 'B', 3)
    graph_ad_matrix.draw_graph('graph_visualization.png')
    """

    def __init__(self):
        """
        Initializes an empty graph with an empty adjacency matrix.
        """
        self.graph = []
        self.nodes = []
        self.node_count = 0

    def add_node(self, v):
        """
        Adds a node 'v' to the graph.

        Args:
        - v: The node to be added.
        """
        if v in self.nodes:
            print(v, "is present in the list.")
        else:
            self.node_count += 1
            self.nodes.append(v)
            for n in self.graph:
                n.append(0)
            temp = [0] * self.node_count
            self.graph.append(temp)

    def add_edge(self, v1, v2, cost):
        """
        Adds an undirected edge between nodes 'v1' and 'v2' with the given cost.

        Args:
        - v1: The first node.
        - v2: The second node.
        - cost: The cost or weight of the edge.
        """
        if v1 not in self.nodes:
            print(v1, "not present in the nodes.")
        elif v2 not in self.nodes:
            print(v2, "not present in the nodes.")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            self.graph[index1][index2] = cost
            self.graph[index2][index1] = cost

    def del_node(self, v):
        """
        Removes a node 'v' from the graph.

        Args:
        - v: The node to be removed.
        """
        if v not in self.nodes:
            print(v, "not present in the nodes.")
        else:
            index1 = self.nodes.index(v)
            self.node_count -= 1
            self.nodes.remove(v)
            self.graph.pop(index1)
            for i in self.graph:
                i.pop(index1)

    def del_edge(self, v1, v2):
        """
        Removes the edge between nodes 'v1' and 'v2'.

        Args:
        - v1: The first node.
        - v2: The second node.
        """
        if v1 not in self.nodes:
            print(v1, 'not present in the graph.')
        elif v2 not in self.nodes:
            print(v2, "not present in the graph.")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            self.graph[index1][index2] = 0
            self.graph[index2][index1] = 0

    def print_matrix(self):
        """
        Prints the adjacency matrix of the graph.
        """
        for row in self.graph:
            for value in row:
                print(value, end=" ")
            print()

    def draw_graph(self, filename="graph_visualization.png"):
        """
        Draws and saves the graph visualization using NetworkX and Matplotlib.

        Args:
        - filename: The name of the file to save the visualization.
        """
        g = nx.Graph()

        for node in self.nodes:
            g.add_node(node)

        for i in range(self.node_count):
            for j in range(i + 1, self.node_count):
                if self.graph[i][j] != 0:
                    g.add_edge(self.nodes[i], self.nodes[j], weight=self.graph[i][j])

        pos = nx.circular_layout(g)
        edge_labels = {(self.nodes[i], self.nodes[j]): self.graph[i][j] for i in range(self.node_count) for j in
                       range(i + 1, self.node_count) if self.graph[i][j] != 0 and i != j}

        nx.draw(g, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black',
                font_size=8)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

        plt.savefig(filename)
        print(f"Graph visualization saved as {filename}")


if __name__ == "__main__":
    graph_ad_matrix = GraphAdjacencyMatrix()
    graph_ad_matrix.add_node('A')
    graph_ad_matrix.add_node('B')
    graph_ad_matrix.add_node('C')
    graph_ad_matrix.add_edge('A', 'B', 3)
    graph_ad_matrix.add_edge('B', 'C', 4)
    graph_ad_matrix.del_node('A')
    graph_ad_matrix.print_matrix()
    graph_ad_matrix.del_edge('B', 'C')
    graph_ad_matrix.add_node("D")
    graph_ad_matrix.add_node("F")
    graph_ad_matrix.add_node("X")
    graph_ad_matrix.add_node("H")
    graph_ad_matrix.add_edge("C", "H", 5)
    graph_ad_matrix.add_edge("B", "X", 8)
    graph_ad_matrix.add_edge("F", "D", 2)
    graph_ad_matrix.add_edge("B", "C", 6)
    graph_ad_matrix.add_edge("X", "D", 1)

    print("\nMatrix:")
    graph_ad_matrix.print_matrix()

    print("\nGraph Visualization:")
    graph_ad_matrix.draw_graph()
