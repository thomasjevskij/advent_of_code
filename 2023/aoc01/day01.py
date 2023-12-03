import re

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(puzzle_input):
    def make_number(line):
        nums = re.findall(r'\d', line)
        return int(nums[0] + nums[-1])
    
    s = sum(make_number(l) for l in puzzle_input)
    print(s)

def p2(puzzle_input):
    def make_number(line):
        t = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
            'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6,
            'seven':7, 'eight':8, 'nine':9}
        pattern1 = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
        pattern2 = r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'
        return 10 * t[re.search(pattern1, line)[0]] + t[re.search(pattern2, line[::-1])[0][::-1]]
    
    s = sum(make_number(l) for l in puzzle_input)
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
