import time
import numpy as np
from collections import defaultdict

class Particle:
    def __init__(self, s, ID):
        self.ID = ID
        p, v, a = s.split(', ')
        self.p = np.array(tuple(map(int, p[p.find('<')+1:-1].split(','))))
        self.v = np.array(tuple(map(int, v[v.find('<')+1:-1].split(','))))
        self.a = np.array(tuple(map(int, a[a.find('<')+1:-1].split(','))))
    def move(self):
        self.v += self.a
        self.p += self.v
        
t = time.process_time()
with open('in') as f:
    data = f.read()

particles = list()
for ID, line in enumerate(data.split('\n')):
    particles.append(Particle(line, ID))

p = min(particles, key=lambda x: sum(abs(i) for i in x.a))

t = time.process_time() - t
print(f"Problem 1: {p.ID}")
print(f"Time elapsed: {t:.2f} s")

t = time.process_time()
for _ in range(39): # Increase number of loops until happy
    collisions = defaultdict(list)
    for p in particles:
        p.move()
        collisions[tuple(p.p)].append(p)
    for k in collisions:
        if len(collisions[k]) > 1:
            for p in collisions[k]:
                particles.remove(p)
        
t = time.process_time() - t
print(f"Problem 2: {len(particles)}")
print(f"Time elapsed: {t:.2f} s")
    