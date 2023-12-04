def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    result = []
    for l in lines:
        winning, ticket = l.split(': ')[1].split(' | ')
        winning = frozenset(int(n) for n in winning.split())
        ticket = frozenset(int(n) for n in ticket.split())
        result.append([winning, ticket, 1])
    return result

def p1(cards):
    def points(winning, ticket):
        return 2 ** (len(winning & ticket) - 1)
    
    s = sum(points(w, t) for w, t, _ in cards if len(w & t))
    print(s)

def p2(cards):
    for i, (winning, ticket, copies) in enumerate(cards):
        if matches := len(winning & ticket):
            start = min(i + 1, len(cards) - 1)
            end = min(i + 1 + matches, len(cards))
            for ii in range(start, end):
                cards[ii][2] += copies

    s = sum(copies for _, _, copies in cards)
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
