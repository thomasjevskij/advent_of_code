import time
from collections import defaultdict

t = time.process_time()

with open('in') as f:
    program = f.readlines()

registers = defaultdict(int)

snd = []
rcv = 0
pc = 0
while pc >= 0 and pc < len(program):
    inst, args = program[pc].strip().split()[0], program[pc].strip().split()[1:]
    if inst == 'snd':
        snd.append(registers[args[0]] if args[0].isalpha() else int(args[0]))
    if inst == 'set':
        registers[args[0]] = registers[args[1]] if args[1].isalpha() else int(args[1])
    if inst == 'add':
        registers[args[0]] += registers[args[1]] if args[1].isalpha() else int(args[1])
    if inst == 'mul':
        registers[args[0]] *= registers[args[1]] if args[1].isalpha() else int(args[1])
    if inst == 'mod':
        registers[args[0]] %= registers[args[1]] if args[1].isalpha() else int(args[1])
    if inst == 'rcv':
        arg = registers[args[0]] if args[0].isalpha() else int(args[0])
        rcv = snd[-1] if arg != 0 else rcv
        if arg != 0:
            break
    if inst == 'jgz':
        arg = registers[args[1]] if args[1].isalpha() else int(args[1])
        pc += arg if registers[args[0]] > 0 else 1
        continue
    
    pc += 1


t = time.process_time() - t
print(f"Problem 1: {rcv}")
print(f"Time elapsed: {t:.2f} s")