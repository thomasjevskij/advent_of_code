from itertools import combinations
from math import prod
import networkx as nx

def parse_input(filename=0):
    with open(filename) as f:
        lines = [eval(f'({l.strip()})') for l in f.readlines()]
    return lines

def p1(nodes):
    edges = sorted(
        combinations(nodes, 2),
        key=lambda u: sum((x - y) ** 2 for x, y in zip(*u))
    )
    G = nx.Graph(edges[:10]) if len(nodes) == 20 else \
    nx.Graph(edges[:1000])
    product = prod(
        len(S) for S in sorted(
            nx.connected_components(G), key=len, reverse=True
        )[:3]
    )
    print(product)

def p2(nodes):
    edges = sorted(
        combinations(nodes, 2),
        key=lambda u: sum((x - y) ** 2 for x, y in zip(*u))
    )
    G = nx.Graph()
    G.add_nodes_from(nodes)
    while not nx.is_connected(G):
        U, V = edges.pop(0)
        G.add_edge(U, V)
    print(U[0] * V[0])

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
