class IntcodeComputer:
    def __init__(self, program):
        self.program = tuple(program)
        self.memory = program
        self.current = 0
        self.opcodes = {1: self.add, 2: self.mul}
        self.strings = {1: ('Add', 4), 2: ('Mul', 4), 99: ('Terminate', 1)}
    def reset(self):
        self.memory = list(self.program)
        self.current = 0
    def add(self):
        term1, term2, target = self.memory[self.current + 1:self.current + 4]
        self.memory[target] = self.memory[term1] + self.memory[term2]
        self.current += 4
    def mul(self):
        term1, term2, target = self.memory[self.current + 1:self.current + 4]
        self.memory[target] = self.memory[term1] * self.memory[term2]
        self.current += 4
    def step(self, verbose):
        i = self.current
        opcode = self.memory[i]
        if verbose:
            f, length = self.strings[opcode]
            print(f'{i} {f}: {self.memory[i + 1:i + length]}')
        self.opcodes[opcode]()
    def run(self, verbose=False):
        while (self.memory[self.current]) != 99:
            self.step(verbose)
        return self

    def __getitem__(self, key):
        return self.memory[key]
    def __setitem__(self, key, value):
        self.memory[key] = value