import networkx as nx
import matplotlib.pyplot as plt

Graphland_bus_rout = nx.DiGraph()
bus_stops = [f'P{i}' for i in range(1,13)]
connections = [
    ('P1', 'P2'), ('P2', 'P3'), ('P3', 'P4'), ('P4', 'P2'),
    ('P2', 'P5'), ('P5', 'P6'), ('P6', 'P7'), ('P7', 'P3'),
    ('P3', 'P8'), ('P8', 'P9'), ('P9', 'P10'), ('P10', 'P4'), 
    ('P4', 'P11'), ('P11', 'P12'), ('P12', 'P5'), 
    ('P5', 'P8'), ('P8', 'P11'), ('P11', 'P4'),
    ('P4', 'P6'), ('P7', 'P10'), ('P9', 'P1')
]

Graphland_bus_rout.add_nodes_from(bus_stops)
Graphland_bus_rout.add_edges_from(connections)

plt.figure(figsize=(8, 8))
pos = nx.circular_layout(Graphland_bus_rout)
nx.draw(Graphland_bus_rout, pos, with_labels=True, node_color="red", node_size=700, font_size=10, font_weight="bold", edge_color="darkblue", arrows=True )
plt.title("Bus rout in Graphland")
plt.show()


# Analysis:
# Кількість вершин і ребер

num_nodes = Graphland_bus_rout.number_of_nodes()
num_edges = Graphland_bus_rout.number_of_edges()

# Ступінь вершин (вхідний і вихідний ступені)
in_degrees = dict(Graphland_bus_rout.in_degree())
out_degrees = dict(Graphland_bus_rout.out_degree())

# Щільність графа
density = nx.density(Graphland_bus_rout)

# Середня довжина шляху (якщо граф є сильно звязним)
if nx.is_strongly_connected(Graphland_bus_rout):
    avg_path_length = nx.average_shortest_path_length(Graphland_bus_rout)
else:
    avg_path_length = "Undefined (Graph is not strongly connected)"

# Центральність вузлів
degree_centrality = nx.degree_centrality(Graphland_bus_rout)
closeness_centrality = nx.closeness_centrality(Graphland_bus_rout)

# Сильно зв'язні компоненти
strongly_connected_components = list(nx.strongly_connected_components(Graphland_bus_rout))

# Вивід результатів аналізу грфа:
print("Number of stops (nodes):", num_nodes)
print("Number of routes (edges):", num_edges)
print("In-degree of each stop:", in_degrees)
print("Out-degree of each stop:", out_degrees)
print("Density of the graph:", density)
print("Average path length:", avg_path_length)
print("Degree centrality:", degree_centrality)
print("Closeness centrality:", closeness_centrality)
print("Strongly connected components:", strongly_connected_components)


