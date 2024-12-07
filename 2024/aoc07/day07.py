from itertools import product
from operator import mul, add

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def parse_line(line, allowed_ops):
    ans, operands = line.split(': ')
    ans = int(ans)
    operands = [int(o) for o in operands.split()]
    for operators in product(allowed_ops, repeat=len(operands) - 1):
        first = operands[0]
        for op, second in zip(operators, operands[1:]):
            first = op(first, second)
        if first == ans:
            return ans
    return 0

def p1(lines):
    c = sum(parse_line(line, [add, mul]) for line in lines)
    left = [line for line in lines if parse_line(line, [add, mul]) == 0]
    print(c)

    return left, c

def concat(a, b):
    return (int(f'{a}{b}'))

def p2(lines, c):
    c += sum(parse_line(line, [add, mul, concat]) for line in lines)
    print(c)

puzzle_input = parse_input()

p2(*p1(puzzle_input[:]))
