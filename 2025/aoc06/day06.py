def parse_input(filename=0):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def p1(lines):
    lines = [l.split() for l in lines]
    total = sum(
        eval(operator.join(operands))
        for *operands, operator in zip(*lines)
    )
    print(total)

def p2(lines):
    total = 0
    operands = []
    for *digits, operator in zip(*[line.rstrip('\n')[::-1] for line in lines]):
        if all(d == ' ' for d in digits) and operator == ' ':
            continue
        operands.append(''.join(digits))
        if operator in '*+':
            total += eval(operator.join(operands))
            operands.clear()
    print(total)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
