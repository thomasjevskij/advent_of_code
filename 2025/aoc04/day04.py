def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        rolls = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '@':
                    rolls.add((x, y))
    return rolls

def neighbors(xy):
    x, y = xy
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            yield (x + i, y + j)

def find_removable(rolls):
    removable = set()
    for r in rolls:
        adj = 0
        for n in neighbors(r):
            if n in rolls:
                adj += 1
        if adj < 4:
            removable.add(r)
    return removable

def p1(rolls):
    print(len(find_removable(rolls)))

def p2(rolls):
    total = 0
    while (removable := find_removable(rolls)):
        total += len(removable)
        rolls -= removable
    print(total)


puzzle_input = parse_input()

p1(puzzle_input.copy())
p2(puzzle_input.copy())
