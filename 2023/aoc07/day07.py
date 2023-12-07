def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    result = []
    for l in lines:
        hand, bid = l.split()
        result.append((hand, int(bid)))
    return result

def score(hand):
    hand_set = frozenset(hand)
    longest = max(hand.count(c) for c in hand_set)
    if len(hand_set) == 5:
        return 'a'
    if len(hand_set) == 4:
        return 'b'
    if len(hand_set) == 3 and longest == 2:
        return 'c'
    if len(hand_set) == 3 and longest == 3:
        return 'd'
    if len(hand_set) == 2 and longest == 3:
        return 'e'
    if len(hand_set) == 2 and longest == 4:
        return 'f'
    return 'g'
    
def p1(hands):
    def tiebreak(hand):
        mapping = {'2': 'a', '3': 'b', '4': 'c', '5': 'd', '6': 'e',
                    '7': 'f', '8': 'g', '9': 'h', 'T': 'i', 'J': 'j', 
                    'Q': 'k', 'K': 'l', 'A': 'm'}
        return ''.join(mapping[c] for c in hand)

    s = sum(i * bid for i, (_, bid) in 
            enumerate(
                sorted(
                    hands, key=lambda x: score(x[0])+tiebreak(x[0])
                    ), 
                start=1
                )
            )
    print(s)

def p2(hands):
    def tiebreak(hand):
        mapping = {'J': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', 
                   '6': 'f', '7': 'g', '8': 'h', '9': 'i', 'T': 'j', 
                   'Q': 'k', 'K': 'l', 'A': 'm'}
        return ''.join(mapping[c] for c in hand)
    def jokerify(hand):
        if hand != 'JJJJJ':
            c_longest, _ = max(((c, hand.count(c)) for c in hand if not c == 'J'), key=lambda x:x[1])
            hand = hand.replace('J', c_longest)
        return hand
    s = sum(i * bid for i, (_, bid) in 
            enumerate(
                sorted(
                    hands, key=lambda x: score(jokerify(x[0])) + tiebreak(x[0])
                    ), 
                start=1
                )
            )

    print(s)
    

hands = parse_input()

p1(hands[:])
p2(hands[:])
