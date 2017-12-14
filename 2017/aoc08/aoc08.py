import time
from collections import defaultdict

t = time.process_time()

registers = defaultdict(int)
incdec = {'inc':'+=', 'dec':'-='}
m = 0

with open('in') as f:
    for line in f:
        symbols = line.split()
        symbols[1] = incdec[symbols[1]]
        if eval('registers["{}"]'.format(symbols[-3])+line[line.find(symbols[-2]):]):
            exec(' '.join(('registers["{}"]'.format(symbols[0]), symbols[1], symbols[2])))
            m = max(m, max(registers.values()))

print("Problem 1: {}".format(max(registers.values())))
print("Problem 2: {}".format(m))
t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
