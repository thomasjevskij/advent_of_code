from functools import cache
from collections import defaultdict

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    graph = defaultdict(list)
    for line in lines:
        node, neighbors = line.split(': ')
        graph[node] = neighbors.split()
    return graph

# Making the graph global since it won't
# work as an argument with @cache
graph = parse_input()

@cache
def dfs(node, end):
    if node == end:
        return 1
    return sum(
        dfs(neighbor, end) for neighbor in graph[node]
    )

def p1():
    print(dfs('you', 'out'))

def p2():
    # Input is very nicely structured:
    # fft always comes before dac
    # Otherwise we would need to prune some nodes
    svr_fft = dfs('svr', 'fft')
    fft_dac = dfs('fft', 'dac')
    dac_out = dfs('dac', 'out')
    
    print(svr_fft * fft_dac * dac_out)

p1()
p2()
