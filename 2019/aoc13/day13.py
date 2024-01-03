import sys

sys.path.append('..')
from intcode import IntcodeComputer

def parse_input():
    with open(0) as f:
        lines = eval(f'[{f.read().strip()}]')
    return lines

def p1(opcodes):
    game = IntcodeComputer(opcodes[:])
    game.run()
    c = 0
    while game.output_stream:
        _, _, tile_id = game.popleft(), game.popleft(), game.popleft()
        if tile_id == 2:
            c += 1
    print(c)

def p2(opcodes):
    game = IntcodeComputer(opcodes[:])
    state = {'ball': 0, 'paddle': 0, 'score': 0}
    def update():
        while game.output_stream:
            x, _, tile_id = game.popleft(), game.popleft(), game.popleft()
            if tile_id == 4:
                state['ball'] = x
            if tile_id == 3:
                state['paddle'] = x
            if x == -1:
                state['score'] = tile_id

    game[0] = 2
    game.run()
    update()
    while not game.is_finished():
        if state['ball'] < state['paddle']:
            game.append(-1)
        elif state['ball'] > state['paddle']:
            game.append(1)
        else:
            game.append(0)
        game.run()
        update()

    print(state['score'])

opcodes = parse_input()

p1(opcodes)
p2(opcodes)
