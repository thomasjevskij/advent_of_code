import time

class Animal:
    def __init__(self, s):
        args = s.split()
        self.speed = int(args[3])
        self.times = [int(args[-2]), int(args[6])]
        self.current_state = 1
        self.countdown = self.times[self.current_state]
        self.pos = self.points = 0

    def move(self):
        self.countdown -= 1
        self.pos += self.speed * self.current_state
        if self.countdown <= 0:
            self.current_state = (self.current_state + 1) % 2
            self.countdown = self.times[self.current_state]

t = time.process_time()
reindeer = []
with open('input.txt') as f:
    for l in f.readlines():
        reindeer.append(Animal(l.rstrip()))

input_time = 2503
for i in range(input_time):
    m = -1
    for r in reindeer:
        r.move()
        m = max(r.pos, m)
    for r in reindeer:
        r.points += int(r.pos == m) * 1

t = time.process_time() - t  
print("Problem 1: %d" % max(reindeer, key = lambda r: r.pos).pos)
print("Problem 2: %d" % max(reindeer, key = lambda r: r.points).points)
print("Time elapsed: %d ms"%int(t * 1000))


