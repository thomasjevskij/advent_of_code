import numpy as np
import re
from fractions import Fraction

def parse_input(filename=0):
    with open(filename) as f:
        machines = [
            np.array(
            [*(re.findall(r'\d+', s) for s in machine.strip().split('\n'))],
            dtype=int).T + Fraction()
            for machine in f.read().split('\n\n')
        ]
    return machines

def inv(mat):
    adj = np.array([[mat[1, 1], -mat[0, 1]],
                    [-mat[1, 0], mat[0, 0]]])
    det = mat[0, 0] * mat[1, 1] - mat[0, 1] * mat[1, 0]
    return adj / det

def solve(matrix, vector, valid):
    A, B = inv(matrix) @ vector
    return 3*A + B if (valid(A) and valid(B)) else 0

def p1(machines):
    tokens = sum(solve(buttons[:,:2], buttons[:, 2],
                       lambda n: n.denominator == 1 and round(n) < 100)
                       for buttons in machines)
    print(tokens)

def p2(machines):
    offset = 10000000000000
    tokens = sum(solve(buttons[:, :2], buttons[:, 2] + offset,
                       lambda n: n.denominator == 1)
                       for buttons in machines)
    print(tokens)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
