import time
from collections import defaultdict

class Program:
    def __init__(self, code, pid):
        self.code = code
        self.pc = 0
        self.registers = defaultdict(int)
        self.registers['p'] = pid
        self.rcv_queue = []
        self.snd_queue = None
        self.snd_counter = 0
        self.waiting = False
        self.done = False
        self.instructions = {'snd':self.snd, 'set':self.setval, 'add':self.add, 
                             'mul':self.mul, 'mod':self.mod, 'rcv':self.rcv,
                             'jgz':self.jgz}
    def run(self):
        if self.pc < 0 or self.pc >= len(self.code):
            self.done = True
            return
        inst, args = self.code[self.pc].split()[0], self.code[self.pc].split()[1:]
        self.instructions[inst](args)
        return self.pc
    def set_snd_queue(self, snd_queue):
        self.snd_queue = snd_queue
    def snd(self, args):
        self.snd_queue.append(self.registers[args[0]] if args[0].isalpha() else int(args[0]))
        self.snd_counter += 1
        self.pc += 1
    def setval(self, args):
        self.registers[args[0]] = self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.pc += 1
    def add(self, args):
        self.registers[args[0]] += self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.pc += 1
    def mul(self, args):
        self.registers[args[0]] *= self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.pc += 1
    def mod(self, args):
        self.registers[args[0]] %= self.registers[args[1]] if args[1].isalpha() else int(args[1])
        self.pc += 1
    def rcv(self, args):
        if len(self.rcv_queue) == 0:
            self.waiting = True
            return
        self.waiting = False
        self.registers[args[0]] = self.rcv_queue.pop(0)
        self.pc += 1
    def jgz(self, args):
        jmp = self.registers[args[1]] if args[1].isalpha() else int(args[1])
        if args[0].isalpha():
            self.pc += jmp if self.registers[args[0]] > 0 else 1
        else:
            self.pc += jmp if int(args[0]) > 0 else 1
    

t = time.process_time()

with open('in') as f:
    code = f.read().split('\n')

p0 = Program(code, 0)
p1 = Program(code, 1)
p0.set_snd_queue(p1.rcv_queue)
p1.set_snd_queue(p0.rcv_queue)
programs = [p0, p1]

while True:
    for p in programs:
        while not p.done:
            p.run()
            if p.waiting:
                break
    if sum(p.waiting and not len(p.rcv_queue) for p in programs) == 2:
        break

t = time.process_time() - t
print(f"Problem 2: {p1.snd_counter}")
print(f"Time elapsed: {t:.2f} s")