import sys

sys.path.append('..')
from intcode import IntcodeComputer
from itertools import product

def parse_input():
    with open(0) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

def p1(opcodes):
    c = IntcodeComputer(opcodes[:])
    c[1] = 12
    c[2] = 2
    print(c.run()[0])

def p2(opcodes):
    c = IntcodeComputer(opcodes[:])
    def execute(n, v):
        c.reset()
        c[1] = n
        c[2] = v
        return c.run()[0]
    s = next(100 * noun + verb for noun, verb in product(range(100), repeat=2) if execute(noun, verb) == 19690720)
    print(s)

opcodes = parse_input()

p1(opcodes)
p2(opcodes)
