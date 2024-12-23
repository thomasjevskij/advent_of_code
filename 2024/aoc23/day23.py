import networkx as nx
from itertools import combinations

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    G = nx.Graph()
    G.add_edges_from([tuple(line.split('-')) for line in lines])
    return G

def find_cliques(G, size):
    result = []
    for clique in nx.find_cliques(G):
        if len(clique) == size:
            result.append(tuple(clique))
        elif len(clique) > size:
            result.extend(combinations(clique, size))
    return result

def p1(G):
    cliques = set(tuple(sorted(c)) for c in find_cliques(G, 3))
    num = sum(any(node.startswith('t') for node in c) for c in cliques)
    print(num)

def p2(G):
    clique = max(nx.find_cliques(G), key=len)
    print(','.join(sorted(clique)))

puzzle_input = parse_input()

p1(puzzle_input)
p2(puzzle_input)
