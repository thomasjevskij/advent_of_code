def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(banks):
    print(calc_joltage(banks, 2))

def p2(banks):
    print(calc_joltage(banks, 12))

def calc_joltage(banks, digits):
    joltage = 0
    for b in banks:
        s = ''
        for i in range(digits - 1, -1, -1):
            if i != 0:
                digit = max(b[:-i])
            else:
                digit = max(b)
            s += digit
            idx = b.index(digit)
            b = b[idx + 1:]
        joltage += int(s)
    return joltage

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
