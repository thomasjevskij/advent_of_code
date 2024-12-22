from collections import deque, defaultdict
from itertools import pairwise

def parse_input(filename=0):
    with open(filename) as f:
        numbers = [int(l.strip()) for l in f.readlines()]
    return numbers

prune = 16777216

def secret(num):
    num ^= (num * 64)
    num %= prune
    num ^= (num // 32)
    num %= prune
    num ^= (num * 2048)
    num %= prune
    return num

def p1(numbers):
    for i in range(len(numbers)):
        for _ in range(2000):
            numbers[i] = secret(numbers[i])
    print(sum(numbers))

def p2(numbers):
    get_ones = lambda x: x % 10
    make_diffs = lambda x: tuple(s - f for f, s in
                                 pairwise(map(get_ones, x)))
    bananas = defaultdict(int)
    for num in numbers:
        Q = deque([num])
        visited = set()
        for _ in range(3):
            Q.append(num := secret(num))
        for _ in range(1997):
            Q.append(num := secret(num))
            if diffs := make_diffs(Q) not in visited:
                visited.add(diffs)
                bananas[diffs] += get_ones(num)
            Q.popleft()
    print(max(bananas.values()))

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
