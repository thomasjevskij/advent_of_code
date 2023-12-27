import sys
from itertools import permutations

sys.path.append('..')
from intcode import IntcodeComputer

def parse_input():
    with open(0) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

def p1(opcodes):
    computers = tuple(IntcodeComputer(opcodes[:]) for _ in range(5))

    def run_sequence(phase_settings):
        for computer, phase_setting in zip(computers, phase_settings):
            computer.reset()
            computer.input_stream.append(phase_setting)
        computers[0].input_stream.append(0)

        for i, computer in enumerate(computers):
            computer.run(input_stream=[*computers[i-1].output_stream])

        return computers[-1].output_stream.popleft()
    
    s = max(run_sequence(phase_settings) for phase_settings in permutations(range(5), 5))
    print(s)

def p2(opcodes):
    computers = tuple(IntcodeComputer(opcodes[:]) for _ in range(5))

    def run_sequence(vals):
        for c, v in zip(computers, vals):
            c.reset()
            c.input_stream.append(v)
        computers[0].input_stream.append(0)
        
        cur = 0
        while not all(comp.is_finished() for comp in computers):
            computers[cur].run(input_stream=[*computers[cur-1].output_stream])
            computers[cur-1].output_stream.clear()
            cur += 1
            cur %= 5

        return c.output_stream.popleft()
    
    s = max(run_sequence(vals) for vals in permutations(range(5, 10), 5))
    print(s)

opcodes = parse_input()

p1(opcodes)
p2(opcodes)
