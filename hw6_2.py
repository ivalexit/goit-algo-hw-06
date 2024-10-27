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



def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in set(graph[vertex]) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph[vertex]) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))


start, goal = 'P1', 'P11'

print("DFS Paths from P1 to P11:")
dfs_results = list(dfs_paths(Graphland_bus_rout, start, goal))
for path in dfs_results:
    print(path)


print("\nBFS Paths from P1 to P11:")
bfs_results = list(bfs_paths(Graphland_bus_rout, start, goal))
for path in bfs_results:
    print(path)


"""
DFS націлений на відвідання глибших рівнів графа, що іноді приводить його до зайвих циклів
 чи довших шляхів, оскільки він продовжує шлях доти, доки не досягне мети 
 чи кінця гілки. В моєму випадку деякі шляхи, знайдені DFS, є довшими та включають більше вузлів,
   оскільки DFS не оптимізує за кількістю вершин.


BFS завжди знайде найкоротший шлях, оскільки досліджує вузли рівень за рівнем.
 В цьому прикладі BFS першими знаходить шляхи з мінімальною кількістю кроків,
 як-от перший рядок: ['P1', 'P2', 'P3', 'P8', 'P11'], і вже після цього досліджує довші шляхи.
 Це пояснюється тим, що BFS побудований таким чином, що перевіряє всі можливі варіанти одночасно.


"""