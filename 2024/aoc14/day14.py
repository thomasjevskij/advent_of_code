import numpy as np
import re
from copy import deepcopy

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    robots = []
    for line in lines:
        numbers = [int(x) for x in re.findall(r'-?\d+', line)]
        robots.append((np.array(numbers[:2]), np.array(numbers[2:])))
    return robots

def safety_factor(robots):
    x_lim, y_lim = (11, 7) if len(robots) == 12 else (101, 103)
    x_mid = x_lim // 2
    y_mid = y_lim // 2

    UL = sum(pos[0] < x_mid and pos[1] < y_mid for pos, _ in robots)
    LL = sum(pos[0] < x_mid and pos[1] > y_mid for pos, _ in robots)
    UR = sum(pos[0] > x_mid and pos[1] < y_mid for pos, _ in robots)
    LR = sum(pos[0] > x_mid and pos[1] > y_mid for pos, _ in robots)

    return UL * LL * UR * LR

def p1(robots):
    x_lim, y_lim = (11, 7) if len(robots) == 12 else (101, 103)
    x_mid = x_lim // 2
    y_mid = y_lim // 2
    for _ in range(100):
        for pos, vel in robots:
            pos += vel
            pos[0] %= x_lim
            pos[1] %= y_lim
    print(safety_factor(robots))

def p2(robots):
    x_lim, y_lim = (11, 7) if len(robots) == 12 else (101, 103)
    vals = []
    for c in range(1, 101 * 103 + 1):
        for pos, vel in robots:
            pos += vel
            pos[0] %= x_lim
            pos[1] %= y_lim
        vals.append(safety_factor(robots))
    idx, _ = min(enumerate(vals, start=1), key=lambda x: x[1])
    print(idx)

puzzle_input = parse_input()

p1(deepcopy(puzzle_input[:]))
p2(deepcopy(puzzle_input[:]))