import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E']
}

print("Adjacency List:")
pprint(adj_list)


G_list = nx.Graph()
for node, neighbors in adj_list.items():
    for neighbor in neighbors:
        G_list.add_edge(node, neighbor)



nodes = ['A', 'B', 'C', 'D', 'E', 'F']

adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

print("\nAdjacency Matrix:")
pprint(adj_matrix)


G_matrix = nx.Graph()
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if adj_matrix[i][j] == 1:
            G_matrix.add_edge(nodes[i], nodes[j])



plt.figure(figsize=(12, 5))


pos = nx.spring_layout(G_list, seed=42)


plt.subplot(1, 2, 1)
nx.draw(G_list, pos, with_labels=True,
        node_color='skyblue', node_size=2000, font_size=12)
plt.title("Graph from Adjacency List")


plt.subplot(1, 2, 2)
nx.draw(G_matrix, pos, with_labels=True,
        node_color='lightgreen', node_size=2000, font_size=12)
plt.title("Graph from Adjacency Matrix")

plt.show()
