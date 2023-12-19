from collections import namedtuple

Part = namedtuple('Part', ['x', 'm', 'a', 's'])

def parse_input():
    with open(0) as f:
        rules, parts = map(lambda x: x.split('\n'), f.read().split('\n\n'))
    part_list = []
    for p in parts:
        args = p[1:-1].split(',')
        x, m, a, s = (int(aa.split('=')[-1]) for aa in args)
        part_list.append(Part(x=x, m=m, a=a, s=s))
        rule_dict = {'A':'A', 'R':'R'}
    for r in rules:
        label, flow = r[:-1].split('{')
        rule_dict[label] = flow
    return rule_dict, part_list

def p1(rules, parts):
    accepted = []
    for p in parts:
        cur = 'in'
        done = False
        while not done:
            for step in rules[cur].split(','):
                if step == 'A':
                    done = True
                    accepted.append(p)
                if step == 'R':
                    done = True
                    break
                if '<' in step:
                    num, target = step[2:].split(':')
                    num = int(num)
                    if getattr(p, step[0]) < num:
                        cur = target
                        break
                if '>' in step:
                    num, target = step[2:].split(':')
                    num = int(num)
                    if getattr(p, step[0]) > num:
                        cur = target
                        break
                cur = step
    s = sum(sum(p) for p in accepted)
    print(s)

def p2(rules):
    # IDEA:
    # Similar to day 8 (?) where you send ranges instead
    # Send one range_part with
    # x = [1, 4000], m = [1, 4000], a = [1, 4000] and s = [1, 4000]
    # For every rule, split the range and pass on.
    # What ends up in accepted, do combinatorics on each one, sum them
    # They can only be combined within the part
    mother_part = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    parts = [('in', mother_part)]
    print('Not done yet.')

rules, parts = parse_input()

p1(rules.copy(), parts[:])
p2(rules.copy())
