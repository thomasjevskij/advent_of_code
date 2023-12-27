import sys

sys.path.append('..')
from intcode import IntcodeComputer

def parse_input():
    with open(0) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

def p1(opcodes):
    c = IntcodeComputer(opcodes[:])
    print(c.run(input_stream=[1]).output_stream.pop())

def p2(opcodes):
    c = IntcodeComputer(opcodes[:])
    print(c.run(input_stream=[5]).output_stream.pop())

opcodes = parse_input()

p1(opcodes)
p2(opcodes)
