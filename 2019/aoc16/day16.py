from itertools import accumulate

def parse_input():
    'Turn input into a list of integers.'
    with open(0) as f:
        signal = [int(c) for c in f.read().strip()]
    return signal

def pattern(i, length):
    "First tried with iterators and stuff but it's fairly easy to compute."
    i += 1
    i //= length
    i %= 4
    return [0, 1, 0, -1][i]

def phase(signal):
    'Just follow the instructions from the problem.'
    return [
        abs(sum(x * pattern(i, length)
                for i, x in enumerate(signal[length-1:], start=length-1))) % 10
        for length in range(1, len(signal) + 1)
    ]

def p1(signal):
    for _ in range(100):
        signal = phase(signal)
    print(''.join(str(n) for n in signal[:8]))

def p2(signal):
    '''The trick is that the pattern for signal[offset:] is just a series of
    1s, meaning we can ignore it and just sum. And from there we can use
    partial sums with accumulate, so we don't redo a bunch of work. Learned
    about the accumulate function from reddit which makes it very neat.'''
    offset = sum(x * 10 ** i for i, x in enumerate(signal[6::-1]))
    signal = (signal * 10000)[offset:][::-1]

    for _ in range(100):
        signal = list(accumulate(signal, lambda x, y: (x + y) % 10))
    print(''.join(map(str, signal[::-1][:8])))

signal = parse_input()

p1(signal)
p2(signal)