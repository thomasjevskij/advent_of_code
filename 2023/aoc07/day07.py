def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    result = []
    for l in lines:
        hand, bid = l.split()
        result.append((hand, int(bid)))
    return result

def p1(hands):
    def score(hand):
        score = ''
        hand_set = set(hand)
        longest = max(hand.count(c) for c in hand_set)
        mapping = {'2': 'a', '3': 'b', '4': 'c', '5': 'd', '6': 'e',
            '7': 'f', '8': 'g', '9': 'h', 'T': 'i', 'J': 'j', 
            'Q': 'k', 'K': 'l', 'A': 'm'}
        if len(hand_set) == 5:
            score += 'a'
        elif len(hand_set) == 4:
            score += 'b'
        elif len(hand_set) == 3 and longest == 2:
            score += 'c'
        elif len(hand_set) == 3 and longest == 3:
            score += 'd'
        elif len(hand_set) == 2 and longest == 3:
            score += 'e'
        elif len(hand_set) == 2 and longest == 4:
            score += 'f'
        elif len(hand_set) == 1:
            score += 'g'
        for c in hand:
            score += mapping[c]
        return score

    s = sum(i * bid for i, (_, bid) in enumerate(sorted(hands, key=lambda x: score(x[0])), start=1))
    print(s)

def p2(hands):
    def score(hand):
        if hand != 'JJJJJ':
            c_longest, longest = max(((c, hand.count(c)) for c in hand if not c == 'J'), key=lambda x:x[1])
            j_hand = hand.replace('J', c_longest)
            hand_set = set(j_hand)
            longest = max(j_hand.count(c) for c in hand_set)
        else:
            hand_set = set(hand)
            longest = max(hand.count(c) for c in hand_set)
        mapping = {'J': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', 
                   '6': 'f', '7': 'g', '8': 'h', '9': 'i', 'T': 'j', 
                   'Q': 'k', 'K': 'l', 'A': 'm'}
        score = ''
        if len(hand_set) == 5:
            score += 'a'
        elif len(hand_set) == 4:
            score += 'b'
        elif len(hand_set) == 3 and longest == 2:
            score += 'c'
        elif len(hand_set) == 3 and longest == 3:
            score += 'd'
        elif len(hand_set) == 2 and longest == 3:
            score += 'e'
        elif len(hand_set) == 2 and longest == 4:
            score += 'f'
        elif len(hand_set) == 1:
            score += 'g'
        for c in hand:
            score += mapping[c]
        return score
    s = sum(i * bid for i, (_, bid) in enumerate(sorted(hands, key=lambda x: score(x[0])), start=1))

    print(s)
    

hands = parse_input()

p1(hands[:])
p2(hands[:])
