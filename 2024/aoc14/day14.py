import numpy as np
import re
from copy import deepcopy
from itertools import count

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    robots = []
    for line in lines:
        numbers = [int(x) for x in re.findall(r'-?\d+', line)]
        robots.append((np.array(numbers[:2]), np.array(numbers[2:])))
    return robots

def p1(robots):
    x_lim, y_lim = (11, 7) if len(robots) == 12 else (101, 103)
    x_mid = x_lim // 2
    y_mid = y_lim // 2
    for _ in range(100):
        for pos, vel in robots:
            pos += vel
            pos[0] %= x_lim
            pos[1] %= y_lim
    UL = sum(pos[0] < x_mid and pos[1] < y_mid for pos, _ in robots)
    LL = sum(pos[0] < x_mid and pos[1] > y_mid for pos, _ in robots)
    UR = sum(pos[0] > x_mid and pos[1] < y_mid for pos, _ in robots)
    LR = sum(pos[0] > x_mid and pos[1] > y_mid for pos, _ in robots)
    print(UL*LL*UR*LR)

def print_robots(robots):
    cols, rows = (101, 103)
    s = ''
    for row in range(rows):
        for col in range(cols):
            if any(all(pos == [col, row]) for pos, _ in robots):
                s += '#'
            else:
                s += '.'
        s += '\n'
    print(s)

def p2(robots):
    cols, rows = (101, 103)
    arr = np.zeros((rows, cols))
    for pos, _ in robots:
        col, row = pos
        arr[row, col] += 1
    for c in count(1):
        for pos, vel in robots:
            col, row = pos
            arr[row, col] -= 1
            pos += vel
            pos[0] %= cols
            pos[1] %= rows
            col, row = pos
            arr[row, col] += 1
        if sum(arr.flat > 1) == 0:
            # print_robots(robots)
            print(c)
            break

puzzle_input = parse_input()

p1(deepcopy(puzzle_input[:]))
p2(deepcopy(puzzle_input[:]))
