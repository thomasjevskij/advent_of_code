def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(banks):
    joltage = 0
    for b in banks:
        first = max(b[:-1])
        idx = b.index(first)
        last = max(b[idx + 1:])
        joltage += int(first + last)
    print(joltage)

def p2(banks):
    joltage = 0
    for b in banks:
        s = ''
        for i in range(11, -1, -1):
            if i != 0:
                digit = max(b[:-i])
            else:
                digit = max(b)
            s += digit
            idx = b.index(digit)
            b = b[idx + 1:]
        joltage += int(s)
    print(joltage)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
