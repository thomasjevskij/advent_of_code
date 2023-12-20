from collections import defaultdict
from collections import deque
from itertools import count
from functools import reduce

HIGH = True
LOW = False

class FlipFlop:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.on = False
    def recv_pulse(self, pulse, origin):
        if pulse == HIGH:
            return []
        if not self.on:
            l = [(HIGH, n, self.name) for n in self.neighbors]
            self.on = True
            return l
        l = [(LOW, n, self.name) for n in self.neighbors]
        self.on = False
        return l
    def reset(self):
        self.on = False
    def register_input(self, modules):
        return True
    def __repr__(self):
        return f'ID: {self.name}, is on: {self.on}, neighbors: {self.neighbors}'
    
class Conj:
    def __init__(self, name, neighbors):
        self.name = name
        self.memory = {}
        self.neighbors = neighbors
    def reset(self):
        for k in self.memory:
            self.memory[k] = LOW
    def register_input(self, modules):
        for m in modules:
            self.memory[m] = LOW
    def recv_pulse(self, pulse, origin):
        self.memory[origin] = pulse
        if all(self.memory[k] == HIGH for k in self.memory):
            l = [(LOW, n, self.name) for n in self.neighbors]
            self.pulse = LOW
            return l
        l = [(HIGH, n, self.name) for n in self.neighbors]
        self.pulse = HIGH
        return l
    def __repr__(self):
        return f'ID: {self.name}, memory: {self.memory}, neighbors: {self.neighbors}'
    
class Broadcaster:
    def __init__(self, name, neighbors):
        self.name = 'broadcaster'
        self.neighbors = neighbors
    def reset(self):
        pass
    def recv_pulse(self, pulse, origin):
        return [(pulse, n, self.name) for n in self.neighbors]
    def __repr__(self):
        return f'ID: {self.name}, neighbors: {self.neighbors}'
    
class Empty:
    def __init__(self, name):
        self.name = name
        self.pulse = HIGH
        self.memory = {}
    def register_input(self, modules):
        for m in modules:
            self.memory[m] = LOW
    def reset(self):
        for k in self.memory:
            self.memory[k] = LOW
    def recv_pulse(self, pulse, origin):
        self.pulse = pulse
        return []
    def __repr__(self):
        return f'ID: {self.name}'

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    modules = {}
    inputs = defaultdict(list)
    types = {'%': FlipFlop, '&': Conj, 'b': Broadcaster}
    for l in lines:
        t = l[0]
        if t in '%&':
            start = 1
        else:
            start = 0
        name, neighbors = l[start:].split(' -> ')
        neighbors = neighbors.split(', ')
        modules[name] = types[t](name, neighbors)
        for n in neighbors:
            inputs[n].append(name)
    for name in inputs:
        try:
            modules[name].register_input(inputs[name])
        except KeyError:
            modules[name] = Empty(name)
            modules[name].register_input(inputs[name])
    return modules

def p1(modules):
    c = {HIGH: 0, LOW: 0}
    for _ in range(1000):
        pulses = deque()
        pulses.append((LOW, 'broadcaster', 'button'))
        while pulses:
            pulse, receiver, sender = pulses.popleft()
            c[pulse] += 1
            pulses.extend(modules[receiver].recv_pulse(pulse, sender))
    print(c[LOW]*c[HIGH])

# Will not work on test input
def p2(modules):
    # rx gets pulse from mg and mg only
    # mg will send low pulse if it remembers high pulses from
    # its inputs
    cycles = []
    for target in modules['mg'].memory:
        for k in modules:
            modules[k].reset()
        for c in count(start=1):
            pulses = deque()
            pulses.append((LOW, 'broadcaster', 'button'))
            found = False
            while pulses:
                pulse, receiver, sender = pulses.popleft()
                if sender == target and pulse == HIGH:
                    found=True
                    cycles.append(c)
                    break
                pulses.extend(modules[receiver].recv_pulse(pulse, sender))
            if found:
                break
    print(reduce(lambda x, y: x*y, cycles))

modules = parse_input()

p1(modules)
p2(modules)
