import time

t = time.process_time()

def spin(s, args):
    X = int(args)
    return s[-X:]+s[:-X]
def exchange(s, args):
    x, y = map(int, args.split('/'))
    return s.replace(s[x], '_').replace(s[y], s[x]).replace('_', s[y])
def partner(s, args):
    x, y = args.split('/')
    return s.replace(x, '_').replace(y, x).replace('_', y)
def dance(dance_moves, programs, moves):
    for move in dance_moves.split(','):
        s, args = move[0], move[1:]
        programs = moves[s](programs, args)
    return programs

moves = {'s' : spin, 'x' : exchange, 'p' : partner}
programs = 'abcdefghijklmnop'

with open('in') as f:
    dance_moves = f.read().strip()

programs = dance(dance_moves, programs, moves)

t = time.process_time() - t 
print(f'Problem 1: {programs}')
print(f"Time elapsed: {t:.2f} s")

t = time.process_time()
visited = [programs]
while True:
    programs = dance(dance_moves, programs, moves)
    if programs not in visited:
        visited.append(programs)
    else:
        break

t = time.process_time() - t
print(f'Problem 2: {visited[int("9"*9) % len(visited)]}')
print(f"Time elapsed: {t:.2f} s")