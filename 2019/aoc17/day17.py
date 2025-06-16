import sys

sys.path.append('..')
from intcode import IntcodeComputer

def parse_input(file=0):
    with open(file) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

def get_neighbors(z):
    'Utility to look around a complex coordinate.'
    yield from (z + 1j ** i for i in range(4))

def parse_bot_output(lines):
    '''Return a dict with coordinates given a list of strings (output line
    by line).'''
    return {
        (x + y * 1j): c for y, line in enumerate(lines)
        for x, c in enumerate(line) if c != '.'
    }

def walk(path):
    '''Walk straight ahead until you have to turn, then keep going until
    you hit a dead end. Return the full sequence of moves.'''
    pos = [x for x in path if path[x] == '^'][0]
    s = ''
    d = -1j
    steps = 0
    while True:
        if pos + d not in path:
            s += f'{steps},'
            steps = 0
            if pos + d * 1j in path:
                s += 'R,'
                d *= 1j
            elif pos + d * -1j in path:
                s += 'L,'
                d *= -1j
            else:
                return s.strip('0,')
        else:
            pos += d
            steps += 1

def p1(opcodes):
    '''Fairly simple, just parse the bot output. Using a dict to make
    neighbor checking a bit more convenient.'''
    bot = IntcodeComputer(opcodes[:])
    bot.run()
    data = ''.join(map(chr, bot.output_stream)).strip()
    path = parse_bot_output(data.split('\n'))
    print(
        sum(
            int(z.real * z.imag) for z in path
            if all(n in path for n in get_neighbors(z))
        )
    )

def p2(opcodes):
    '''The trick is that if you look at the map, you'll see that it's
    all a single path. So if you walk along it and only turn when you
    have to, you will have visited every space. So I solved this by hand
    by passing the path (as defined in p1) to the walk function and then
    trying various splits. The strategy to find the splits was to look
    from one end of the walk sequence and try substrings with len <= 20.
    Then using str.replace, str.split and str.strip we can have a look
    at the remaining sequence and do it two more times. You could do
    some tree search I guess but it was easy enough by hand.'''
    bot = IntcodeComputer(opcodes[:])
    bot[0] = 2
    seq = 'B,A,B,C,B,A,C,C,B,A'
    A = 'R,12,R,8,L,8,L,12'
    B = 'R,8,L,10,R,8'
    C = 'L,12,L,10,L,8'
    video_feed = 'n\n'
    tot = '\n'.join([seq, A, B, C, video_feed])
    bot.run()
    bot.run(input_stream=[ord(c) for c in tot])
    print(bot.output_stream[-1])

opcodes = parse_input()

p1(opcodes[:])
p2(opcodes[:])
