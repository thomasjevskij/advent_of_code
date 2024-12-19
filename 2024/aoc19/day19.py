from functools import cache

def parse_input(filename=0):
    with open(filename) as f:
        towels, designs = f.read().split('\n\n')
    return frozenset(towels.split(', ')), designs.split('\n')

@cache
def search(towels, design):
    ans = int(design in towels) + \
        sum(
            search(towels, design[i:]) 
            for i in range(len(design)) 
            if design[:i] in towels
        )
    return ans

def p1(towels, designs):
    s = sum(search(towels, d) > 0 for d in designs)
    print(s)

def p2(towels, designs):
    s = sum(search(towels, d) for d in designs)
    print(s)

puzzle_input = parse_input()

p1(*puzzle_input[:])
p2(*puzzle_input[:])
