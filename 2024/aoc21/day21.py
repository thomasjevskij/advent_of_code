from itertools import pairwise
from functools import cache

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

numpad = {'7': {'8': '>', '4': 'v'},
          '8': {'7': '<', '9': '>', '5': 'v'},
          '9': {'8': '<', '6': 'v'},
          '4': {'7': '^', '5': '>', '1': 'v'},
          '5': {'4': '<', '8': '^', '6': '>', '2': 'v'},
          '6': {'5': '<', '9': '^', '3': 'v'},
          '1': {'4': '^', '2': '>'},
          '2': {'1': '<', '5': '^', '3': '>', '0': 'v'},
          '3': {'2': '<', '6': '^', 'A': 'v'},
          '0': {'2': '^', 'A': '>'},
          'A': {'0': '<', '3': '^'}}

arrowpad = {'^': {'A': '>', 'v': 'v'},
            'A': {'^': '<', '>': 'v'},
            '<': {'v': '>'},
            'v': {'<': '<', '^': '^', '>': '>'},
            '>': {'v': '<', 'A': '^'}}

def bfs(graph, start, goal):
    Q = []
    depth = {start: 0}
    Q.append((start, ''))
    valid = lambda n: n not in depth
    while Q:
        node, path = Q.pop(0)
        if node == goal:
            break
        for neighbor in filter(valid, graph[node]):
            depth[neighbor] = depth[node] + 1
            new_path = path + graph[node][neighbor]
            Q.append((neighbor, new_path))
    return path, depth

def dfs(graph, node, goal, depth, path=None):
    if path is None:
        path = []
    if node == goal:
        yield ''.join(path) + 'A'
    else:
        valid = lambda n: n in depth and depth[n] == depth[node] + 1
        for neighbor in filter(valid, graph[node]):
            for sp in dfs(graph, neighbor, goal, depth,
                          [*path, graph[node][neighbor]]):
                yield sp
    if path:
        path.pop()

@cache
def get_length(code, level, is_numpad=True):
    graph = numpad if is_numpad else arrowpad
    result = 0
    for start, goal in pairwise('A' + code):
        _, depth = bfs(graph, start, goal)
        candidates = dfs(graph, start, goal, depth)
        if level == 0:
            result += len(min(candidates))
        else:
            result += min(get_length(c, level - 1, False) for c in candidates)
    return result

def p1(codes):
    complexity = sum(get_length(code, 2) * int(code[:-1]) for code in codes)
    print(complexity)

def p2(codes):
    complexity = sum(get_length(code, 25) * int(code[:-1]) for code in codes)
    print(complexity)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
