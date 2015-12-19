import time, random

def backtrack(s, rep):
    count = 0
    old_s = ''
    keys = list(rep.keys())
    random.shuffle(keys)
    while old_s != s:
        old_s = s
        for key in keys:
            while key in s:
                count += s.count(key)
                s = s.replace(key, rep[key])
    return int(s == 'e') * count

t = time.process_time()
rep = {}
inv_rep = {}
s = ''
with open('input.txt') as f:
    for line in f.readlines():
        if '=>' in line:
            key, val = line.rstrip().split(' => ')
            inv_rep[val] = key
            if key in rep:
                rep[key].append(val)
            else:
                rep[key] = [val]
        else:
            s = line.rstrip()
changes = set()
for key in rep.keys():
    i = s.find(key, 0)
    while i != -1:        
        for val in rep[key]:
            changes.add(s[0:i]+val+s[i+len(key):])
        i = s.find(key, i+1)    

print("Problem 1: %d"%len(changes))

p2 = 0
while p2 == 0:
    p2 = backtrack(s, inv_rep)
t = time.process_time() - t
print("Problem 2: %d"%p2)
print("Time elapsed: %d µs"%int(t*1000000))
