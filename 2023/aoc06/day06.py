from functools import reduce
from operator import mul

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    return tuple([n for n in l.split(':')[1].split()] for l in lines)

def ways_to_win(time, distance):
    return sum(speed * (time - speed) > distance for speed in range(1, time))

def p1(times, distances):
    print(reduce(mul, (ways_to_win(t, d) for t, d in zip(map(int, times), map(int, distances)))))

def p2(times, distances):
    print(ways_to_win(int(''.join(times)), int(''.join(distances))))

times, distances = parse_input()

p1(times[:], distances[:])
p2(times[:], distances[:])
