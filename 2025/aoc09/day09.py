from itertools import combinations, pairwise

def parse_input(filename=0):
    with open(filename) as f:
        lines = [eval(f'({l.strip()})') for l in f.readlines()]
    return lines

def area(tiles):
    p1, p2 = tiles
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def p1(tiles):
    # Area = (|x1 - x2| + 1) * (|y1 - y2| + 1)
    # Need to add one bc boundaries are inclusive
    m = max(combinations(tiles, 2), key=area)
    print(area(m))

def intersects(rect, edge2):
    # rect: (left, top, right, bottom)
    left, top, right, bottom = rect
    min_x = min(p[0] for p in edge2)
    max_x = max(p[0] for p in edge2)
    min_y = min(p[1] for p in edge2)
    max_y = max(p[1] for p in edge2)

    # Vertical edge: left <= x <= right
    if min_x == max_x:
        if left <= min_x <= right:
            if min_y <= top <= max_y or min_y <= bottom <= max_y:
                return True
    # Horizontal edge: bottom <= y <= top
    else:
        if bottom <= min_y <= top:
            if min_x <= left <= max_x or min_x <= right <= max_x:
                return True
    
    return False

def p2(tiles):
    edges = list(pairwise(tiles))
    edges.append((tiles[-1], tiles[0]))
    candidates = sorted(
        combinations(tiles, 2), key=area, reverse=True
    )
    for p1, p2 in candidates:
        left = min(p[0] for p in (p1, p2))
        right = max(p[0] for p in (p1, p2))
        bottom = min(p[1] for p in (p1, p2))
        top = max(p[1] for p in (p1, p2))
        # Rect edges will and should intersect with edges.
        # Inside should not!!!
        rect = [left + 1, top - 1, right - 1, bottom + 1]
        if not any(intersects(rect, edge) for edge in edges):
            break

    print(area((p1, p2)))

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
