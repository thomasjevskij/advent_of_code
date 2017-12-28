import time
from collections import defaultdict

class TM:
    def __init__(self, filename):
        self.tape = defaultdict(int)
        self.states = {}
        self.cursor = 0
        with open(filename) as f:
            line = f.readline().rstrip('.\n')
            self.currentState = line.split()[-1]
            self.steps = int(f.readline().split()[-2])
            f.readline()
            while True:
                line = f.readline()
                if line == '':
                    break
                if line.startswith('In state'):
                    state = {}
                    stateKey = line.rstrip(':\n').split()[-1]
                    f.readline()
                    falseVal = int(f.readline().rstrip('.\n').split()[-1])
                    direction = -1 if f.readline().rstrip('.\n').split()[-1] == 'left' else 1
                    nextKey = f.readline().rstrip('.\n').split()[-1]
                    state[0] = (falseVal, direction, nextKey)
                    f.readline()
                    trueVal = int(f.readline().rstrip('.\n').split()[-1])
                    direction = -1 if f.readline().rstrip('.\n').split()[-1] == 'left' else 1
                    nextKey = f.readline().rstrip('.\n').split()[-1]
                    state[1] = (trueVal, direction, nextKey)
                    self.states[stateKey] = state
    def run(self):
        for _ in range(self.steps):
            val = self.tape[self.cursor]
            nextVal, direction, nextKey = self.states[self.currentState][val]
            self.tape[self.cursor] = nextVal
            self.cursor += direction
            self.currentState = nextKey
        return sum(self.tape.values())

t = time.process_time()

machine = TM('in')

print(f"Problem 1: {machine.run()}")
t = time.process_time() - t
print(f"Time elapsed: {t:.2f} s")
