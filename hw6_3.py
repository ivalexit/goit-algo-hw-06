import networkx as nx
import matplotlib.pyplot as plt
import random

Graphland_bus_rout = nx.DiGraph()
bus_stops = [f'P{i}' for i in range(1, 13)]

connections = [
    ('P1', 'P2'), ('P2', 'P3'), ('P3', 'P4'), ('P4', 'P2'),
    ('P2', 'P5'), ('P5', 'P6'), ('P6', 'P7'), ('P7', 'P3'),
    ('P3', 'P8'), ('P8', 'P9'), ('P9', 'P10'), ('P10', 'P4'), 
    ('P4', 'P11'), ('P11', 'P12'), ('P12', 'P5'), 
    ('P5', 'P8'), ('P8', 'P11'), ('P11', 'P4'),
    ('P4', 'P6'), ('P7', 'P10'), ('P9', 'P1')
]

Graphland_bus_rout.add_nodes_from(bus_stops)

# Додавання випадкової ваги ребрам
for u, v in connections:
    weight = random.randint(1, 10) 
    Graphland_bus_rout.add_edge(u, v, weight=weight)

# Візуалізація графа з вагами
plt.figure(figsize=(8, 8))
pos = nx.circular_layout(Graphland_bus_rout)
nx.draw(Graphland_bus_rout, pos, with_labels=True, node_color="red", 
        node_size=700, font_size=10, font_weight="bold", edge_color="darkblue", arrows=True)
edge_labels = nx.get_edge_attributes(Graphland_bus_rout, 'weight')
nx.draw_networkx_edge_labels(Graphland_bus_rout, pos, edge_labels=edge_labels)
plt.title("Graphland Bus Route with random weights")
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra_all_paths(graph, start_node):
    return nx.single_source_dijkstra_path_length(graph, start_node)

# Обчислення найкоротших шляхів для кожної вершини
shortest_paths = {}
for node in Graphland_bus_rout.nodes:
    shortest_paths[node] = dijkstra_all_paths(Graphland_bus_rout, node)


print("Shortest paths from each node to all other nodes with random weights:")
for start_node, paths in shortest_paths.items():
    print(f"From {start_node}:")
    for target, distance in paths.items():
        print(f"  To {target} - Distance: {distance}")
    print()