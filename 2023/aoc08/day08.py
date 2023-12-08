import re
from itertools import cycle
from collections import defaultdict
from math import lcm

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    lr = lines.pop(0)
    lines.pop(0)
    graph = {}
    for l in lines:
        node, e1, e2 = re.match(r'(\w+) = \((\w+), (\w+)\)', l).groups()
        graph[node] = (e1, e2)
    return lr, graph

def p1(lr, graph):
    s = 0
    current = 'AAA'
    for c in cycle(lr):
        s += 1
        current = graph[current][0] if c == 'L' else graph[current][1]
        if current == 'ZZZ':
            break
    print(s)

def p2(lr, graph):
    current = [n for n in graph if n.endswith('A')]
    path_lengths = []
    for cur in current:
        start = cur
        s = 0
        for c in cycle(lr):
            s += 1
            cur = graph[cur][0] if c == 'L' else graph[cur][1]
            if cur.endswith('Z'):
                path_lengths.append(s)
                break
    print(lcm(*path_lengths))

lr, graph = parse_input()

p1(lr, graph.copy())
p2(lr, graph.copy())
