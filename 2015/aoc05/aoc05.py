import re, time

def nice(s):
    vowels = re.compile('[aeiou]')
    repeats = re.compile(r'(.)\1{1,}')
    forbidden = re.compile('ab|cd|pq|xy')

    if len(vowels.findall(s)) < 3:
        return 0
    if len(repeats.findall(s)) == 0:
        return 0
    if len(forbidden.findall(s)) > 0:
        return 0
    return 1

def new_nice(s):
    pair = re.compile(r'(\w\w)\w*\1{1,}')
    repeats = re.compile(r'(\w)\w\1')

    if len(pair.findall(s)) == 0:
        return 0
    if len(repeats.findall(s)) == 0:
        return 0
    return 1

t = time.process_time()  
p1 = 0
p2 = 0

with open('input.txt') as f:
    for s in f.readlines():
        p1 += nice(s)
        p2 += new_nice(s)

t = time.process_time() - t
print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
print("Time elapsed: %d ms"%int(t * 1000))
