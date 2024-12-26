from operator import and_, or_, xor

def parse_input(filename=0):
    with open(filename) as f:
        wire_lines, gate_lines = f.read().split('\n\n')
    wires = {}
    gates = []
    for w in wire_lines.split('\n'):
        wire, val = w.split(': ')
        wires[wire] = int(val)
    for gate in gate_lines.split('\n'):
        gates.append(tuple(x for x in gate.split() if x != '->'))
    return wires, gates

def p1(wires, gates):
    ops = {'AND': and_, 'OR': or_, 'XOR': xor}
    key = lambda x: x[0] in wires and x[2] in wires
    workspace = gates.copy()
    while workspace:
        gate = max(workspace, key=key)
        workspace.remove(gate)
        w1, op, w2, target = gate
        wires[target] = ops[op](wires[w1], wires[w2])
    num = sum(wires[w] * 2 ** e for e, w in
              enumerate(sorted(w for w in wires if w.startswith('z'))))
    print(num)
    return num

def p2(gates):
    int_xors = list(filter(
        lambda g: g[1] == 'XOR'
        and all(w[0] in 'xy' for w in (g[0], g[2]))
        and g[-1] != 'z00',
        gates
    ))
    inp_xors = list(filter(
        lambda g: g[1] == 'XOR'
        and not any(w[0] in 'xy' for w in (g[0], g[2])),
        gates
    ))
    ors = list(filter(
        lambda g: g[1] == 'OR',
        gates
    ))
    ands = list(filter(
        lambda g: g[1] == 'AND'
        and not any(w in (g[0], g[2]) for w in ('x00', 'y00')),
        gates
    ))
    xor_ops = set(w for w, _, _, _ in int_xors)
    xor_ops.update(w for _, _, w, _ in int_xors)
    or_ops = set(w for w, _, _, _ in ors)
    or_ops.update(w for _, _, w, _ in ors)
    and_ops = set(w for w, _, _, _ in ands)
    and_ops.update(w for _, _, w, _ in ands)

    err = list(filter(
        lambda g: not g[-1].startswith('z'),
        inp_xors
    ))
    err.extend(list(filter(
        lambda g: g[-1] not in and_ops,
        int_xors
    )))
    err.extend(list(filter(
        lambda g: g[-1] not in and_ops
        and g[-1] != 'z45',
        ors
    )))
    err.extend(list(filter(
        lambda g: g[-1] not in or_ops,
        ands
    )))
    s = ','.join(sorted(set(g[-1] for g in err)))
    print(s)

puzzle_input = parse_input()

p1(*puzzle_input)
p2(puzzle_input[1])