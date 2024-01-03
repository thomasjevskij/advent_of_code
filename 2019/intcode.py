from collections import deque, defaultdict

class IntcodeComputer:
    def __init__(self, program):
        self.program = tuple(program[:])
        self.input_stream = deque()
        self.output_stream = deque()
        self.memory = defaultdict(int)
        self.memory.update({i: c for i, c in enumerate(self.program)})
        self.current = 0
        self.relative_base = 0
        self.opcodes = {1: self.add, 2: self.mul, 3: self.inp, 4: self.out,
                        5: self.jump_if_true, 6: self.jump_if_false,
                        7: self.lt, 8: self.equals, 9: self.adj_base}
        self.strings = {1: ('Add', 4), 2: ('Mul', 4), 3: ('Input', 2),
                        4: ('Output', 2), 5: ('Jump if true', 3),
                        6: ('Jump if false', 3), 7: ('Less than', 4),
                        8: ('Equals', 4), 9: ('Adjust relative base', 2),
                        99: ('Terminate', 1)}
        

    def reset(self):
        self.memory.clear()
        self.memory.update({i: c for i, c in enumerate(self.program)})
        self.current = 0
        self.relative_base = 0
        self.input_stream.clear()
        self.output_stream.clear()
        return self

    def get_modes(self):
        code = self[self.current] // 100
        return (code % 10, (code // 10) % 10, (code // 100) % 10)

    def get_address(self, address, mode):
        match mode:
            case 0:
                return address
            case 2:
                return self.relative_base + address

    def add(self):
        modes = self.get_modes()
        terms = [self[i] for i in range(self.current + 1, self.current + 3)]
        term1, term2 = [t if m == 1 else self[self.get_address(t, m)] 
                        for t, m in zip(terms, modes)]
        target = self.get_address(self[self.current + 3], modes[2])
        self[target] = term1 + term2
        self.current += 4
        return True

    def mul(self):
        modes = self.get_modes()
        factors = [self[i] for i in range(self.current+1, self.current+3)]
        factor1, factor2 = [f if m == 1 else self[self.get_address(f, m)] 
                            for f, m in zip(factors, modes)]
        target = self.get_address(self[self.current + 3], modes[2])
        self[target] = factor1 * factor2
        self.current += 4
        return True

    def inp(self):
        if not self.input_stream:
            return False
        val = self.input_stream.popleft()
        mode = self.get_modes()[0]
        target = self.get_address(self[self.current + 1], mode)
        self[target] = val
        self.current += 2
        return True

    def out(self):
        val = self[self.current + 1]
        mode = self.get_modes()[0]
        val = val if mode == 1 else self[self.get_address(val, mode)]
        self.output_stream.append(val)
        self.current += 2
        return True

    def jump_if_true(self):
        args = [self[i] for i in range(self.current+1, self.current+3)]
        condition, jump_to = [a if m == 1 else self[self.get_address(a, m)] 
                              for a, m in zip(args, self.get_modes())]
        if condition != 0:
            self.current = jump_to
        else:
            self.current += 3
        return True

    def jump_if_false(self):
        args = [self[i] for i in range(self.current+1, self.current+3)]
        condition, jump_to = [a if m == 1 else self[self.get_address(a, m)] 
                              for a, m in zip(args, self.get_modes())]
        if condition == 0:
            self.current = jump_to
        else:
            self.current += 3
        return True

    def lt(self):
        modes = self.get_modes()
        args = [self[i] for i in range(self.current+1, self.current+3)]
        arg1, arg2 = [a if m == 1 else self[self.get_address(a, m)] 
                      for a, m in zip(args, modes)]
        target = self.get_address(self[self.current + 3], modes[2])
        self[target] = int(arg1 < arg2)
        self.current += 4
        return True

    def equals(self):
        modes = self.get_modes()
        args = [self[i] for i in range(self.current+1, self.current+3)]
        arg1, arg2 = [a if m == 1 else self[self.get_address(a, m)] 
                      for a, m in zip(args, modes)]
        target = self.get_address(self[self.current + 3], modes[2])
        self[target] = int(arg1 == arg2)
        self.current += 4
        return True
    
    def adj_base(self):
        arg = self[self.current + 1]
        mode = self.get_modes()[0]
        arg = arg if mode == 1 else self[self.get_address(arg, mode)]
        self.relative_base += arg
        self.current += 2
        return True

    def step(self, verbose):
        i = self.current
        fun = self.memory[i] % 100
        if verbose:
            f, length = self.strings[fun]
            print(f'{i} {f}: {[self[i] for i in range(self.current+1, self.current+length)]}')
        return self.opcodes[fun]()

    def run(self, verbose=False, input_stream = []):
        self.input_stream.extend(input_stream)
        while (self[self.current]) != 99:
            if not self.step(verbose):
                break
        return self
    
    def popleft(self):
        return self.output_stream.popleft()
    
    def append(self, val):
        self.input_stream.append(val)
        return self
    
    def is_finished(self):
        return self[self.current] == 99

    def __getitem__(self, key):
        if key < 0:
            raise IndexError
        return self.memory[key]
    def __setitem__(self, key, value):
        if key < 0:
            raise IndexError
        self.memory[key] = value