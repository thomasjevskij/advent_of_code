from itertools import pairwise

def parse_input(filename=0):
    with open(filename) as f:
        lines = [tuple(int(x) for x in l.strip().split()) for l in f.readlines()]
    return lines

def is_safe(report):
    is_sorted = report == tuple(sorted(report)) or report == tuple(sorted(report, reverse=True))
    good_levels = all(abs(first - second) >= 1 and abs(first - second) <= 3 
                      for first, second in pairwise(report))

    return (is_sorted and good_levels)

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
