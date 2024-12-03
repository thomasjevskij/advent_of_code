import re
from operator import mul

def parse_input(filename=0):
    with open(filename) as f:
        code = f.read()
    return code

def p1(code):
    s = sum(eval(m) for m in re.findall(r'mul\(\d+,\d+\)', code))
    print(s)

def p2(code):
    should = True
    s = 0
    while re.search(r'mul\(\d+,\d+\)', code):
        if code.startswith("do()"):
            should = True
            code = code[4:]
        if code.startswith("don't()"):
            should = False
            code = code[7:]
        if m := re.search(r'^mul\(\d+,\d+\)', code):
            if should:
                s += eval(m[0])
            code = code[len(m[0]):]
        else:
            code = code[1:]
    print(s)



puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
