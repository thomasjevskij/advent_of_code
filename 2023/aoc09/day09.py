from itertools import pairwise
from functools import reduce
from operator import sub

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    sequences = tuple([int(n) for n in l.split()] for l in lines)
    return sequences

def diff(seq):
    seqs = [seq]
    while True:
        seqs.insert(0, tuple(s2 - s1 for s1, s2 in pairwise(seqs[0])))
        if len(set(seqs[0])) == 1:
            return seqs

def p1(sequences):
    s = sum(sum(ss[-1] for ss in diff(seq)) for seq in sequences)
    print(s)

def p2(sequences):
    s = sum(sum(ss[-1] for ss in diff(seq[::-1])) for seq in sequences)
    print(s)

sequences = parse_input()
p1(sequences[:])
p2(sequences[:])
