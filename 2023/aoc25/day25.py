from collections import defaultdict, deque

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def bfs(graph, start):
    q = deque()
    visited = set()
    visited.add(start)
    q.append(start)
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                q.append(w)
    return len(visited)


def p1(lines):
    # print('strict graph {')
    graph = defaultdict(set)
    for l in lines:
        left, rights = l.split(': ')
        for right in rights.split():
            s1 = {'zdj', 'nvt'}
            s2 = {'bbm', 'mzg'}
            s3 = {'cth', 'xxk'}
            if len({left, right} | s1) == 2:
                continue
            if len({left, right} | s2) == 2:
                continue
            if len({left, right} | s3) == 2:
                continue
            graph[left].add(right)
            graph[right].add(left)
            # print(f'    {left} -- {right}')
    # print('}')
    s_left = bfs(graph, 'zdj')
    s_right = bfs(graph, 'nvt')
    print(s_left * s_right)
    
# zdj -- nvt
# bbm -- mzg
# cth -- xxk

puzzle_input = parse_input()

p1(puzzle_input[:])
