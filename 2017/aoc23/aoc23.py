import time
from collections import defaultdict
from math import sqrt

class Program:
    def __init__(self, code):
        self.code = code
        self.registers = defaultdict(int)
        self.done = False
        self.instructions = {'set':self.setval, 'sub':self.sub, 
                             'mul':self.mul, 'jnz':self.jnz}
    def run(self):
        if self.registers['pc'] < 0 or self.registers['pc'] >= len(self.code):
            self.done = True
            return self.registers['pc']
        inst, args = self.code[self.registers['pc']].split()[0], self.code[self.registers['pc']].split()[1:]
        self.instructions[inst](args)
        return self.registers['pc']
    def setval(self, args):
        self.registers[args[0]] = self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.registers['pc'] += 1
    def mul(self, args):
        self.registers[args[0]] *= self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.registers['pc'] += 1
        self.registers['mc'] += 1
    def sub(self, args):
        self.registers[args[0]] -= self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.registers['pc'] += 1
    def jnz(self, args):
        jmp = self.registers[args[1]] if args[1].isalpha() else int(args[1])
        if args[0].isalpha():
            self.registers['pc'] += jmp if self.registers[args[0]] != 0 else 1
        else:
            self.registers['pc'] += jmp if int(args[0]) != 0 else 1
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
    

t = time.process_time()

with open('in') as f:
    code = f.read().split('\n')

p1 = Program(code)

while not p1.done:
    p1.run()

t = time.process_time() - t
print(f"Problem 1: {p1.registers['mc']}")
print(f"Time elapsed: {t:.2f} s")
t = time.process_time()

h = 0
b = 57 * 100 + 100000
for i in range(b, b+17001, 17):
    if not is_prime(i):
        h += 1

t = time.process_time() - t
print(f"Problem 2: {h}")
print(f"Time elapsed: {t:.2f} s")
