import time
import networkx as nx
from sys import stdin

t = time.process_time()

edges = set()
G = nx.Graph()

for line in stdin:
    node, rest = line.rstrip().split(' <-> ')
    G.add_node(node)
    for n in rest.split(', '):
        edges.add(tuple(sorted([node, n])))
            
G.add_edges_from(edges)        

print("Problem 2: {}".format(nx.number_connected_components(G)))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
