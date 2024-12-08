from collections import defaultdict
from itertools import combinations
from more_itertools import consume

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    antennae = defaultdict(list)
    xlim = len(lines[0])
    ylim = len(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '.':
                pos = x + y * 1j
                antennae[c].append(pos)
    return antennae, xlim, ylim

def p1(antennae, xlim, ylim):
    antinodes = set()
    inside = lambda z: 0 <= z.real < xlim and 0 <= z.imag < ylim
    for c in antennae:
        consume(
            antinodes.add(z) for a1, a2 in combinations(antennae[c], 2) 
            for z in (2 * a2 - a1, 2 * a1 - a2) if inside(z)
        )
    print(len(antinodes))

def p2(antennae, xlim, ylim):
    antinodes = set()
    # Helper functions
    inside = lambda z: 0 <= z.real < xlim and 0 <= z.imag < ylim
    def make_line(slope, point):
        lim = max(xlim, ylim)
        for n in range(-lim, lim):
            if inside(z := point + n * slope):
                yield z
    # So we can make this into a really ugly consume() call
    for c in antennae:
        consume(
            antinodes.add(z) for a1, a2 in combinations(antennae[c], 2)
            for z in make_line(a1 - a2, a1)
        )
    print(len(antinodes))

puzzle_input = parse_input()

p1(*puzzle_input[:])
p2(*puzzle_input[:])
