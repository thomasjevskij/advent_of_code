from itertools import product

def parse_input(filename=0):
    with open(filename) as f:
        b_list = [eval(l.strip()) for l in f.readlines()]
    return b_list

def get_neighbors(pos):
    for d in [(1, 0), (0, 1)]:
        yield tuple(x + y for x, y in zip(pos, d))
        yield tuple(x - y for x, y in zip(pos, d))

# Just label the obstacles as already visited nodes
def bfs(visited, start, goal):
    # Vanilla BFS
    lim = goal[0]
    Q = []
    visited.add(start)
    Q.append((start, 0)) # Schema: (x, y), (steps from start)
    # Put the filter here so the if statement below is less ugly
    valid = lambda n: n not in visited and all(0 <= x <= lim for x in n)
    # Learned a new trick about how you can for through a list and append
    # to it mid loop to use it as a queue. No need for deque and popleft()
    for node, dist in Q:
        if node == goal:
            break
        # This is prettier than "for blabla: if blo and bli:"
        for neighbor in filter(valid, get_neighbors(node)):
            visited.add(neighbor)
            Q.append((neighbor, dist + 1))
    if goal in visited:
        return dist
    return None

def p1(b_list):
    lim, num = (6, 12) if len(b_list) == 25 else (70, 1024)
    c = bfs(set(b_list[:num]), (0, 0), (lim, lim))
    print(c)

def p2(b_list):
    lim, L = (6, 12) if len(b_list) == 25 else (70, 1024)
    R = len(b_list) - 1
    # Binary search for SPEED (linear search worked just fine)
    # Avoid final iteration (usually condition is L <= R) because
    # we already know we will find an answer here
    while L < R:
        num = (L + R) // 2
        if bfs(set(b_list[:num]), (0, 0), (lim, lim)):
            L = num + 1
        else:
            R = num - 1
    print(','.join(map(str,b_list[(L + R) // 2])))

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
