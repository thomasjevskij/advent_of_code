from time import process_time as pt

class TuringMachine:
    def __init__(self, program, a = 0, b = 0):
        self.program = program
        self.position = 0
        self.registers = {'a': a, 'b': b}
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
    def run(self):
        while self.position >= 0 and self.position < len(self.program):
            i, args = self.program[self.position].rstrip().split(maxsplit = 1)
            self.instructions[i](args)
        print("Register %s: %d\nRegister %s: %d"%('a', self.registers['a'],
                                                  'b', self.registers['b']))

t = pt()
with open('input.txt') as f:
    TC = TuringMachine(list(f.readlines()))
TC.run()
TC2 = TuringMachine(TC.program, a = 1)
TC2.run()
t = pt() - t
print('Process time: %d µs'%int(t*1000000))
