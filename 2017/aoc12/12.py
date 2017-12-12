import time
import networkx as nx

t = time.process_time()

edges = set()
G = nx.Graph()

with open('in') as f:
    for line in f:
        node, rest = line.rstrip().split(' <-> ')
        G.add_node(node)
        for n in rest.split(', '):
            edges.add(tuple(sorted([node, n])))
            
G.add_edges_from(edges)        

print("Problem 1: {}".format(len(nx.node_connected_component(G, '0'))))
print("Problem 2: {}".format(nx.number_connected_components(G)))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
