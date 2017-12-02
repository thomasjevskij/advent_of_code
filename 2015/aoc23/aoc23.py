from time import process_time as pt

class Computer:
    def __init__(self):
        self.position = 0
        self.registers = {'a': 0, 'b': 0}
        self.instructions = {'hlf': self.half,
                             'tpl': self.triple,
                             'inc': self.increment,
                             'jmp': self.jump,
                             'jie': self.jump_even,
                             'jio': self.jump_one}

    def half(self, args):
        self.registers[args] //= 2
        self.position += 1
    def triple(self, args):
        self.registers[args] *= 3
        self.position += 1
    def increment(self, args):
        self.registers[args] += 1
        self.position += 1
    def jump(self, args):
        self.position += int(args)
    def jump_even(self, args):
        r, off = args.split(', ')
        offset = int(off)
        if self.registers[r] % 2 == 0:
            self.position += offset
            return
        self.position += 1
    def jump_one(self, args):
        r, off = args.split(', ')
        offset = int(off)
        if self.registers[r] == 1:
            self.position += offset
            return
        self.position += 1
    def run(self, program, a = 0, b = 0):
        self.registers['a'] = a
        self.registers['b'] = b
        self.position = 0
        while self.position >= 0 and self.position < len(program):
            i, args = program[self.position].rstrip().split(maxsplit = 1)
            self.instructions[i](args)

t = pt()
with open('input.txt') as f:
    program = list(f.readlines())
C = Computer()
C.run(program)
print("Problem 1: %d"%C.registers['b'])
C.run(program, a = 1)
t = pt() - t
print("Problem 2: %d"%C.registers['b'])
print('Process time: %d µs'%int(t*1000000))
