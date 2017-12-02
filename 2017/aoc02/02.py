s = 0
s2 = 0
with open('input.txt') as f:
    for line in f.readlines():
        r = list(sorted(map(int, line.strip().split())))
        s += max(r)-min(r)
        for i in range(len(r)):
            t = list(r[j]//r[i] for j in range(i+1, len(r)) if r[j]/r[i] - r[j]//r[i]==0)
            if len(t) > 0:
                s2 += t[0]
                break
        
print(s)
print(s2)
