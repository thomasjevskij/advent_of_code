def parse_input(filename=0):
    with open(filename) as f:
        ranges = f.readlines()[0].split(',')
    return ranges

def p1(ranges):
    count = 0
    for r in ranges:
        start, stop = map(int, r.split('-'))
        for d in range(start, stop+1):
            id = str(d)
            if (len(id) % 2 == 0 and
                id[:len(id) // 2] == id[len(id) // 2:]):
                count += d
    print(count)

def p2(ranges):
    count = 0
    for r in ranges:
        start, stop = map(int, r.split('-'))
        for d in range(start, stop+1):
            id = str(d)
            for i in range(1, len(id) // 2 + 1):
                subseq = id[:i]
                if id.replace(subseq, '') == '':
                    count += d
                    break
    print(count)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
