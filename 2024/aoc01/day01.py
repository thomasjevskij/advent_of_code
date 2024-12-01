def parse_input(filename=0):
    with open(filename) as f:
        lines = [tuple(int(x) for x in l.strip().split()) for l in f.readlines()]

    return list(zip(*lines))

def p1(numbers):
    first, second = numbers
    s = sum(abs(x - y) for x, y in zip(sorted(first), sorted(second)))
    print(s)

def p2(numbers):
    first, second = numbers
    s = sum(x * second.count(x) for x in first)
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
