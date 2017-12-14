print(sum(len(l.split())==len(set(l.split())) for l in open('in')), sum(len(l.split())==len(set(tuple(sorted(w)) for w in l.split())) for l in open('in')), sep='\n')
