from itertools import combinations

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def find_galaxies(image, expansion):
    galaxies = []
    y = 0
    for row, l in enumerate(image):
        if '#' not in l:
            y += expansion
            continue
        x = 0
        for col, c in enumerate(l):
            if '#' not in ''.join(image[row][col] for row in range(len(image))):
                x += expansion
                continue
            if c == '#':
                galaxies.append((x, y))
            x += 1
        y += 1
    return galaxies

def p1(image):
    s = sum(manhattan(p1, p2) for p1, p2 in combinations(find_galaxies(image, 2), 2))
    print(s)
        
def p2(image):
    s = sum(manhattan(p1, p2) for p1, p2 in combinations(find_galaxies(image, 1e6), 2))
    print(s)
    



puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
