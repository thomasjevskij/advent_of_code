import time
from math import cos, pi

t = time.process_time()
        
firewall = list()
with open('in') as f:
    for line in f:
        offset, period = map(int, line.strip().split(': '))
        f = lambda t, offset, period: int(0.5+0.5*cos(2*pi*(t+offset)/(period*2-2)))
        firewall.append((f, offset, period))

t = time.process_time() - t    
print("Problem 1: {}".format(sum(o*p*f(0, o, p) for f, o, p in firewall)))
print("Time elapsed: {0:.2f} s".format(t))
t = time.process_time()

delay = 0
while True:
    delay += 1
    if sum(f(delay, o, p) for f, o, p in firewall) == 0:
        break
    
t = time.process_time() - t    
print("Problem 2: {}".format(delay))
print("Time elapsed: {0:.2f} s".format(t))
