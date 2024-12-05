from collections import defaultdict
from more_itertools import consume

def parse_input(filename=0):
    with open(filename) as f:
        rules, updates = [x.split('\n') for x in f.read().split('\n\n')]
    return [r.split('|') for r in rules], updates

def validate_update(rules, update):
    rule_dict = defaultdict(list)
    for before, after in rules:
        if before in update and after in update:
            rule_dict[after].append(before)
    
    for u in update:
        if not rule_dict[u]:
            consume(rule_dict[k].remove(u) for k in rule_dict if u in rule_dict[k])
        else:
            return 0
    
    return int(update[len(update) // 2])

def fix_update(rules, update):
    rule_dict = defaultdict(list)

    for before, after in rules:
        if before in update and after in update:
            rule_dict[after].append(before)
    
    update.sort(key=lambda x: len(rule_dict[x]))

    return int(update[len(update) // 2])

def p1(rules, updates):
    s = sum(validate_update(rules, u.split(',')) for u in updates)
    print(s)
    return(s)
    
def p2(rules, updates):
    updates = [u for u in updates if validate_update(rules, u.split(',')) == 0]
    s = sum(fix_update(rules, u.split(',')) for u in updates)
    print(s)

puzzle_input = parse_input()

p1(*puzzle_input[:])
p2(*puzzle_input[:])
