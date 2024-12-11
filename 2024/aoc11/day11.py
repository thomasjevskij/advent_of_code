from functools import cache

def parse_input(filename=0):
    with open(filename) as f:
        numbers = [int(n) for n in f.read().strip().split()]
    return numbers

def blink(number):
    if number == 0:
        return [1]
    s = f'{number}'
    l = len(s)
    if l % 2 == 0:
        return [int(n) for n in [s[:l//2], s[l//2:]]]
    return [number * 2024]

@cache
def count_splits(number, blinks):
    if blinks == 0:
        return 1
    return sum(count_splits(n, blinks - 1) for n in blink(number))

def p1(numbers):
    stones = sum(count_splits(n, 25) for n in numbers)
    print(stones)

def p2(numbers):
    stones = sum(count_splits(n, 75) for n in numbers)
    print(stones)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])
