import re, operator, time

t = time.process_time()
real_sue = {'children': (3, operator.eq),
            'cats': (7, operator.gt),
            'samoyeds': (2, operator.eq),
            'pomeranians': (3, operator.lt),
            'akitas': (0, operator.eq),
            'vizslas': (0, operator.eq),
            'goldfish': (5, operator.lt),
            'trees': (3, operator.gt),
            'cars': (2, operator.eq),
            'perfumes': (1, operator.eq) }

with open('input.txt') as f:
    for s in f.readlines():
        args = re.search(r'(.*\d+): (\w+: \d+), (\w+: \d+), (\w+: \d+)', s.rstrip()).groups()
        truth_1 = 0
        truth_2 = 0
        for i in args[1:]:
            comp = i.split(': ')
            if int(comp[1]) == real_sue[comp[0]][0]:
                truth_1 += 1
            if real_sue[comp[0]][1](int(comp[1]), real_sue[comp[0]][0]):
                truth_2 += 1
        if truth_1 == len(args[1:]):
            print("Problem 1: %s"%args[0])
        if truth_2 == len(args[1:]):
            print("Problem 2: %s"%args[0])
            
t = time.process_time() - t
print("Time elapsed: %d ms"%int(t * 1000))
