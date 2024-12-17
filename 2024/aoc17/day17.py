from itertools import count

class Computer:
    def __init__(self, ABC, program):
        self.A, self.B, self.C = ABC
        self.program = program
        self.i = 0
        self.output = []
        self.instructions = [self.adv, self.bxl, self.bst, self.jnz, self.bxc,
                            self.out, self.bdv, self.cdv]

    def _combo(self, operand):
        if operand < 4:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        raise KeyError(f'Reserved operand: {operand}')

    def adv(self, operand):
        op = self._combo(operand)
        self.A //= (2 ** op)
        self.i += 2

    def bxl(self, operand):
        self.B ^= operand
        self.i += 2

    def bst(self, operand):
        op = self._combo(operand)
        self.B = op % 8
        self.i += 2

    def jnz(self, operand):
        if self.A != 0:
            self.i = operand
        else:
            self.i += 2

    def bxc(self, operand):
        self.B ^= self.C
        self.i += 2

    def out(self, operand):
        op = self._combo(operand)
        self.output.append(op % 8)
        self.i += 2

    def bdv(self, operand):
        op = self._combo(operand)
        self.B = self.A // (2 ** op)
        self.i += 2

    def cdv(self, operand):
        op = self._combo(operand)
        self.C = self.A // (2 ** op)
        self.i += 2

    def run(self):
        while self.i < len(self.program):
            f = self.instructions[self.program[self.i]]
            operand = self.program[self.i + 1]
            f(operand)

def parse_input(filename=0):
    with open(filename) as f:
        registers, program = f.read().split('\n\n')
    ABC = [int(line.split()[-1]) for line in registers.split('\n')]
    program = [int(x) for x in program.split()[-1].split(',')]
    return ABC, program

def run_program(A, program):
    c = Computer([A, 0, 0], program)
    c.run()
    return c.output

def dfs(program, pointer, num):
    for i in range(8):
        if run_program(num * 8 + i, program) == program[pointer:]:
            if pointer == 0:
                return num * 8 + i
            ret = dfs(program, pointer - 1, num * 8 + i)
            if ret is not None:
                return ret
    return None

def p1(ABC, program):
    c = Computer(ABC, program)
    c.run()
    print(','.join(map(str, c.output)))

def p2(ABC, program):
    num = dfs(program, len(program) - 1, 0)
    print(num)

puzzle_input = parse_input()

p1(*puzzle_input[:])
p2(*puzzle_input[:])
