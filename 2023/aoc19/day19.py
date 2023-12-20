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
    accepted = []
    while parts:
        cur, p = parts.pop()
        for step in rules[cur].split(','):
            if step == 'A':
                accepted.append(p)
                break
            if step == 'R':
                break
            if '<' in step:
                num, target = step[2:].split(':')
                num = int(num)
                c = step[0]
                r_min, r_max = p[c]
                # If the higher end of the range is less than num, the whole range passes
                # Then we don't check further steps so we BREAK
                if r_max < num:
                    parts.append((target, p))
                    break
                # Else, if the lower end is inside, split the range. Add a new one to the 
                # list, update the old one and pass it on to the next step, CONTINUE
                if r_min < num:
                    new_part = p.copy()
                    new_part[c] = (r_min, num - 1)
                    parts.append((target, new_part))
                    p[c] = (num, r_max)
                    continue
                # Else, if the whole range fails the check, we just continue, do nothing
            if '>' in step:
                num, target = step[2:].split(':')
                num = int(num)
                c = step[0]
                r_min, r_max = p[c]
                # If the lower end of the range passes, the whole range passes
                # Then we don't check further steps so we BREAK
                if r_min > num:
                    parts.append(target, p)
                    break
                # Else, if the upper end passes (but not lower), split the range
                # Add a new one to the list, update the old one and CONTINUE
                if r_max > num:
                    new_part = p.copy()
                    new_part[c] = (num + 1, r_max)
                    parts.append((target, new_part))
                    p[c] = (r_min, num)
                    continue
                # Else, if the whole range fails the check, we just continue, do nothing
            else: # in case there's just a plain destination here
                parts.append((step, p))
    s = 0
    for a in accepted:
        p = 1
        for key in a:
            span = a[key][1]-a[key][0]+1
            p *= span
        s += p
    print(s)

rules, parts = parse_input()

p1(rules.copy(), parts[:])
p2(rules.copy())
