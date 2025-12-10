from z3 import Optimize, Int, Sum

def parse_input(filename=0):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def toggle(light, button):
    return tuple(
        l if i not in button else not l
        for i, l in enumerate(light)
    )

def bfs(end, buttons):
    Q = []
    visited = set()
    start = (False,) * len(end)
    Q.append((start, 0))
    visited.add(start)
    while Q:
        v, presses = Q.pop(0)
        if v == end:
            return presses
        for neighbor in [
            toggle(v, b) for b in buttons
        ]:
            if neighbor not in visited:
                visited.add(neighbor)
                Q.append((neighbor, presses + 1))

def p1(lines):
    lights = []
    button_sets = []
    for l in lines:
        light, *buttons, _ = l.split()
        lights.append(
            tuple(
                c == '#' for c in light[1:-1]
            )
        )
        button_sets.append(
            [tuple(map(int, b[1:-1].split(','))) for b in buttons]
        )
    s = sum(
        bfs(light, buttons)
        for light, buttons in zip(lights, button_sets)
    )
    print(s)

def solve(joltage, buttons):
    opt = Optimize()

    # Sets up variables for number of button presses
    # Names them c_0-c_end
    press_counts = [Int(f'c_{i}') for i in range(len(buttons))]
    # Add constraint that no press count can be negative
    for count in press_counts:
        opt.add(count >= 0)
    
    # For each joltage, find which buttons affect it.
    # Add constraints that the sum of the button presses
    # has to equal the provided joltage level.
    for pos, jol in enumerate(joltage):
        affects = [
            press_counts[i] for i, button in enumerate(buttons)
            if pos in button
        ]
        opt.add(Sum(affects) == jol)

    opt.minimize(Sum(press_counts))

    # Can't get the model before doing opt.check()
    opt.check()
    model = opt.model()
    return sum(model[c].as_long() for c in press_counts)

def p2(lines):
    joltages = []
    button_sets = []
    for l in lines:
        _, *buttons, joltage = l.split()
        joltages.append(eval(f'({joltage[1:-1]})'))
        button_sets.append(
            [tuple(map(int, b[1:-1].split(','))) for b in buttons]
        )
    s = sum(
        solve(joltage, buttons)
        for joltage, buttons in zip(joltages, button_sets)
    )
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
