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

def walk(start, target, graph, lr):
    s = 0
    current = start
    for c in cycle(lr):
        s += 1
        current = graph[current][0] if c == 'L' else graph[current][1]
        if current.endswith(target):
            return s

def p1(lr, graph):
    s = walk('AAA', 'ZZZ', graph, lr)
    print(s)

def p2(lr, graph):
    s = lcm(*[walk(n, 'Z', graph, lr) for n in graph if n.endswith('A')])
    print(s)

lr, graph = parse_input()

p1(lr, graph.copy())
p2(lr, graph.copy())
