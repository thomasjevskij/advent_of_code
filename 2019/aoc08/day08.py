import numpy as np
from collections import deque

def parse_input():
    with open(0) as f:
        input_line = deque(int(c) for c in list(f.read().strip()))

    width, height = 25, 6
    layers=[]
    while input_line:
        rows = []
        for _ in range(height):
            rows.append([input_line.popleft() for _ in range(width)])
        layers.append(np.array([*rows]))
    
    return layers

def p1(layers):
    min_layer = max(layers, key=lambda x: np.count_nonzero(x))
    s = np.count_nonzero(min_layer == 1) * np.count_nonzero(min_layer == 2)
    print(s)

def p2(layers):
    i = 0
    final_layer = np.ones(layers[i].shape) * 2
    while np.count_nonzero(indices := final_layer == 2):
        final_layer[indices] = layers[i][indices]
        i += 1
    for row in range(final_layer.shape[0]):
        s = ''
        for col in range(final_layer.shape[1]):
            c = '#' if final_layer[row, col] else ' '
            s += c
        print(s)

layers = parse_input()

p1(layers)
p2(layers)
