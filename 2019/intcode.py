from collections import deque

class IntcodeComputer:
    def __init__(self, program):
        self.program = tuple(program)
        self.memory = list(program)
        self.current = 0
        self.opcodes = {1: self.add, 2: self.mul, 3: self.inp, 4: self.out,
                        5: self.jump_if_true, 6: self.jump_if_false, 
                        7: self.lt, 8: self.equals}
        self.strings = {1: ('Add', 4), 2: ('Mul', 4), 3: ('Input', 2),
                        4: ('Output', 2), 5: ('Jump if true', 3), 
                        6: ('Jump if false', 3), 7: ('Less than', 4), 
                        8: ('Equals', 4), 99: ('Terminate', 1)}
        self.input_stream = deque()
        self.output_stream = deque()

    def reset(self):
        self.memory = list(self.program)
        self.current = 0
        self.input_stream.clear()
        self.output_stream.clear()

    def get_modes(self):
        code = self[self.current] // 100
        return (code % 10 == 1, (code // 10) % 10 == 1, (code // 100) % 10 == 1)


    def add(self):
        terms = self[self.current + 1:self.current + 3]
        target = self[self.current + 3]
        term1, term2 = (t if m else self[t] for t, m in zip(terms, self.get_modes()))
        self[target] = term1 + term2
        self.current += 4

    def mul(self):
        factors = self[self.current + 1:self.current + 3]
        target = self[self.current + 3]
        factor1, factor2 = (f if m else self[f] for f, m in zip(factors, self.get_modes()))
        self[target] = factor1 * factor2
        self.current += 4

    def inp(self):
        val = self.input_stream.popleft()
        target = self[self.current + 1]
        self[target] = val
        self.current += 2

    def out(self):
        val = self[self.current + 1]
        mode, _, _ = self.get_modes()
        val = val if mode else self[val]
        self.output_stream.append(val)
        self.current += 2

    def jump_if_true(self):
        args = self[self.current + 1: self.current + 3]
        condition, target = (a if m else self[a] for a, m in zip(args, self.get_modes()))
        if condition != 0:
            self.current = target
        else:
            self.current += 3

    def jump_if_false(self):
        args = self[self.current + 1: self.current + 3]
        condition, target = (a if m else self[a] for a, m in zip(args, self.get_modes()))
        if condition == 0:
            self.current = target
        else:
            self.current += 3

    def lt(self):
        args = self[self.current + 1: self.current + 3]
        target = self[self.current + 3]
        arg1, arg2 = (a if m else self[a] for a, m in zip(args, self.get_modes()))
        self[target] = int(arg1 < arg2)
        self.current += 4

    def equals(self):
        args = self[self.current + 1: self.current + 3]
        target = self[self.current + 3]
        arg1, arg2 = (a if m else self[a] for a, m in zip(args, self.get_modes()))
        self[target] = int(arg1 == arg2)
        self.current += 4

    def step(self, verbose):
        i = self.current
        fun = self.memory[i] % 100
        if verbose:
            f, length = self.strings[fun]
            print(f'{i} {f}: {self[i + 1:i + length]}')
        self.opcodes[fun]()

    def run(self, verbose=False, input_stream = []):
        self.input_stream.extend(input_stream)
        while (self[self.current]) != 99:
            self.step(verbose)
        return self

    def __getitem__(self, key):
        return self.memory[key]
    def __setitem__(self, key, value):
        self.memory[key] = value