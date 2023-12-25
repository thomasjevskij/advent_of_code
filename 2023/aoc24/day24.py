from collections import namedtuple
from itertools import combinations
import numpy as np
from random import sample

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    hails = []
    for l in lines:
        p, v = l.split(' @ ')
        p = np.array([int(x) for x in p.split(', ')])
        v = np.array([int(x) for x in v.split(', ')])
        hails.append(Hail(p, v))
    return hails

class Hail:
    def __init__(self, pos, vel):
        self.position = pos
        self.velocity = vel
    def __call__(self, t):
        return self.position + t * self.velocity
    def __getitem__(self, i):
        return (self.position, self.velocity)[i]

def intersects2(line1, line2):
    p1, v1 = line1
    p2, v2 = line2
    a = np.zeros((2, 2))
    a[:,0] = v1[:2]
    a[:,1] = -v2[:2]
    b = (p2-p1)[:2]
    try:
        t1, t2 = np.linalg.solve(a, b)
    except np.linalg.LinAlgError:
        return None
    return t1, t2

def p1(hails):
    b = (200000000000000, 400000000000000)
    c = 0
    for h1, h2 in combinations(hails, 2):
        p = intersects2(h1, h2)
        if p is not None:
            t1, t2 = p
            p1 = h1(t1)
            if b[0] <= p1[0] <= b[1] and b[0] <= p1[1] <= b[1] and t1 > 0 and t2 > 0:
                c += 1
    print(c)

def make_row(p1, v1, p2, v2):
    a = v2[1]-v1[1]
    b = v1[0]-v2[0]
    c = p1[1]-p2[1]
    d = p2[0]-p1[0]
    e = v1[0]*p1[1] - v2[0]*p2[1] + p2[0]*v2[1] - p1[0]*v1[1]
    return np.array([a, b, c, d, e])

def p2(hails):
    m = np.zeros((4, 5))
    x = min(h.position[0] for h in hails[:8])
    y = min(h.position[1] for h in hails[:8])
    z = min(h.position[2] for h in hails[:8])
    offset = np.array([x, y, z])

    for i, (h1, h2) in enumerate(zip(hails[:4], hails[4:8])):
        p1, v1 = h1
        p2, v2 = h2
        m[i,:] = make_row((p1-offset)[:2], v1[:2], (p2-offset)[:2], v2[:2])
    px, py, _, _ = np.linalg.solve(m[:,:4], m[:,4])

    for i, (h1, h2) in enumerate(zip(hails[:4], hails[4:])):
        p1, v1 = h1
        p2, v2 = h2
        m[i,:] = make_row((p1-offset)[1:], v1[1:], (p2-offset)[1:], v2[1:])
    _, pz, _, _ = np.linalg.solve(m[:,:4], m[:,4])
    pos = np.array([px, py, pz]) + offset
    print(int(sum(np.round(pos))))

hails = parse_input()

p1(hails)
p2(hails)
