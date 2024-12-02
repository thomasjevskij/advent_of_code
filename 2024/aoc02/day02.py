from itertools import pairwise

def parse_input(filename=0):
    with open(filename) as f:
        lines = [tuple(int(x) for x in l.strip().split()) for l in f.readlines()]
    return lines

def is_safe(report):
    test = lambda x: not any(second - first < 1 or second - first > 3 
                      for first, second in pairwise(x))
    return test(report) or test(report[::-1])

def dampener(report):
    for i in range(len(report)):
        yield tuple(x for j, x in enumerate(report) if j != i)

def p1(reports):
    unsafe = [report for report in reports if not is_safe(report)]
    num_safe = len(reports) - len(unsafe)
    print(num_safe)

    return num_safe, unsafe

def p2(num_safe, unsafe):
    num_safe += sum(any(is_safe(r) for r in dampener(report)) for report in unsafe)

    print(num_safe)

puzzle_input = parse_input()

p2(*p1(puzzle_input[:]))
