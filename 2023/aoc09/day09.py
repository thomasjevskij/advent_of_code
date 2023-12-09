def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    sequences = [[int(n) for n in l.split()] for l in lines]
    return sequences

def p1(sequences):
    def process_seq(seq):
        seqs = [seq]
        while True:
            diff_seq = []
            for ii in range(1, len(seqs[0])):
                diff_seq.append(seqs[0][ii]-seqs[0][ii-1])
            seqs.insert(0, diff_seq)
            if len(set(diff_seq)) == 1:
                break
        for i in range(len(seqs)-1):
            seqs[i+1].append(seqs[i][-1]+seqs[i+1][-1])
        return seqs[-1][-1]
    s = sum(process_seq(s[:]) for s in sequences)
    print(s)

def p2(sequences):
    def process_seq(seq):
        seqs = [seq]
        while True:
            diff_seq = []
            for ii in range(1, len(seqs[0])):
                diff_seq.append(seqs[0][ii]-seqs[0][ii-1])
            seqs.insert(0, diff_seq)
            if len(set(diff_seq)) == 1:
                break
        for i in range(len(seqs)-1):
            seqs[i+1].insert(0, seqs[i+1][0]-seqs[i][0])
        return seqs[-1][0]
    s = sum(process_seq(s[:]) for s in sequences)
    print(s)

sequences = parse_input()
p1(sequences[:])
p2(sequences[:])
