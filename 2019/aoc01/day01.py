def parse_input():
    with open(0) as f:
        lines = [int(l.strip()) for l in f.readlines()]
    return lines

def p1(masses):
    s = sum(int(m / 3)-2 for m in masses)
    print(s)

def p2(masses):
    def get_fuel(mass):
        fuel = 0
        while mass > 6:
            mass = int(mass / 3) - 2
            fuel += mass
        return fuel
    s = sum(get_fuel(m) for m in masses)
    print(s)

masses = parse_input()

p1(masses)
p2(masses)
