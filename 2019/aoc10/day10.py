import numpy as np
from collections import defaultdict, deque

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    asteroids = [np.array([x, y]) for y, l in enumerate(lines) for x, c in enumerate(l) if c in 'X#']
    return asteroids

def p1(asteroids):
    def get_visible(a1):
        dirs = defaultdict(list)
        for a2 in asteroids:
            if np.all(a1 == a2):
                continue
            d = a2 - a1
            dirs[tuple(d / np.gcd.reduce(d))].append(a2)
        return a1, dirs

    a, vectors = max((get_visible(a) for a in asteroids), key=lambda x: len(x[1]))
    print(len(vectors))
    return a, vectors

def p2(a, vectors):
    for v in vectors:
        vectors[v].sort(key=lambda x: np.linalg.norm(a-x))
    keys = deque(sorted(vectors.keys(), key=lambda x: np.arctan2(x[1], x[0])))
    keys.rotate(-keys.index((0.0, -1.0)))
    
    i = 0
    while i < 200:
        for k in keys:
            x, y = vectors[k].pop(0)
            i += 1
            if i == 200:
                break

    print(100*x+y)

asteroids = parse_input()

p2(*p1(asteroids.copy()))
