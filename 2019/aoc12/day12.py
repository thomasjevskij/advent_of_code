import numpy as np
import re
from itertools import combinations, count
from copy import deepcopy

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    planets = []
    for l in lines:
        planets.append([np.array([int(n) for n in re.findall(r'\-?\d+', l)]), np.array([0, 0, 0])])
    return planets

def step(planets):
    for (p1, v1), (p2, v2) in combinations(planets, 2):
        x = 1 if p1[0] < p2[0] else -1 if p1[0] > p2[0] else 0
        y = 1 if p1[1] < p2[1] else -1 if p1[1] > p2[1] else 0
        z = 1 if p1[2] < p2[2] else -1 if p1[2] > p2[2] else 0
        a = np.array([x, y, z])
        v1 += a
        v2 -= a
    for p, v in planets:
        p += v

def p1(planets):
    for _ in range(1000):
        step(planets)
    energy = lambda x, y: np.linalg.norm(x, 1) * np.linalg.norm(y, 1)
    s = sum(energy(*planet) for planet in planets)
    print(int(s))

def p2(planets):
    def flatten(planets, i):
        t = sum(((p[i], v[i]) for p, v in planets), ())
        return t
    
    periods = []
    for axis in range(3):
        t_planets = deepcopy(planets)
        visited = set()
        t = flatten(t_planets, axis)
        visited.add(t)
        for i in count(1):
            step(t_planets)
            t = flatten(t_planets, axis)
            if t in visited:
                break
            visited.add(t)
        periods.append(i)
    print(np.lcm.reduce(periods))

planets = parse_input()

p1(deepcopy(planets))
p2(deepcopy(planets))
