def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def p1(lines):
    c = 0
    for row, line in enumerate(lines):
        # Straight left-right
        s = line
        c += s.count('XMAS') + s.count('SAMX')
        # Half of diagonals going down right
        s = ''.join(
            lines[y][x] for x, y in zip(
                range(len(line)),
                range(row, len(lines))
            )
        )
        c += s.count('XMAS') + s.count('SAMX')
        # Half of diagonals going up right
        s = ''.join(
            lines[y][x] for x, y in zip(
                range(row, -1, -1),
                range(len(lines[0]))
            )
        )
        c += s.count('XMAS') + s.count('SAMX')

    for col in range(len(lines[0])):
        # Straight up-down
        s = ''.join(l[col] for l in lines)
        c += s.count('XMAS') + s.count('SAMX')
        # So we don't double dip the diagonals
        if col > 0:
            # Other half of diagonals down-right
            s = ''.join(
                lines[y][x] for x, y in zip(
                range(col, len(lines[0])),
                range(len(lines))
                )
            )
            c += s.count('XMAS') + s.count('SAMX')
            # Other half of diagonals up-right
            s = ''.join(
            lines[y][x] for x, y in zip(
                range(len(lines) - 1, -1, -1),
                range(col, len(lines[0]))
                )
            )
            c += s.count('XMAS') + s.count('SAMX')

    print(c)

def p2(lines):
    # Both diagonals around 'A' should have the characters 'A', 'M', and 'S',
    # sorted alphabetically
    key = ['A', 'M', 'S']
    c = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            if lines[y][x] == 'A':
                s1 = sorted(lines[y + i][x + i] for i in range(-1, 2))
                s2 = sorted(lines[y - i][x + i] for i in range(-1, 2))
                if s1 == key and s2 == key:
                    c += 1
    print(c)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
