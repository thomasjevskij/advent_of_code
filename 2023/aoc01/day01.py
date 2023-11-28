import re

def parse_input():
    with open(0) as f:
        lines = f.readlines()
    return lines

def p1(puzzle_input):
    s = 0
    for l in puzzle_input:
        nums = re.findall(r'\d', l.strip())
        s += int(nums[0])*10 + int(nums[-1])
    print(s)

def p2(puzzle_input):
    s = 0
    t = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
        'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6,
        'seven':7, 'eight':8, 'nine':9}
    for l in puzzle_input:
        pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
        nums = re.findall(pattern, l.strip())
        s += t[nums[0]]*10 + t[nums[-1]]
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
