import sys
from collections import defaultdict

sys.path.append('..')
from intcode import IntcodeComputer

def parse_input():
    with open(0) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

def paint(robot, start = 0):
    # Returns a defaultdict(int) containing the color at each painted position
    # where black is 0 and white is 1
    pos = 0
    dir = 1j
    turns = {0: 1j, 1: -1j}
    hull = defaultdict(int)
    hull[pos] = start
    while not robot.run(input_stream=[hull[pos]]).is_finished():
        color, turn = robot.popleft(), robot.popleft()
        hull[pos] = color
        dir *= turns[turn]
        pos += dir
    return hull

def p1(opcodes):
    robot = IntcodeComputer(opcodes[:])
    hull = paint(robot)
    print(len(hull))

def p2(opcodes):
    WHITE = 1
    robot = IntcodeComputer(opcodes[:])
    hull = paint(robot, start=1)

    # The robot walks in positive orientation, these coordinates are in negative orientation
    # max_x doesn't need +1, there's padding
    min_x, min_y = int(min(z.real for z in hull)), int(min(z.conjugate().imag for z in hull))
    max_x, max_y = int(max(z.real for z in hull)), int(max(z.conjugate().imag for z in hull)) + 1

    # Beautiful
    print('\n'.join(''.join('#' if hull[x - y*1j] == WHITE else '.'
                          for x in range(min_x, max_x))
                  for y in range(min_y, max_y)))

opcodes = parse_input()

p1(opcodes)
p2(opcodes)
