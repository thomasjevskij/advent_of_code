import itertools, time

t = time.process_time()
with open('input.txt') as f:
    buckets = list(map(int, f.readlines()))

sums = []
volume = 150
p1 = 0
for i in range(1, len(buckets)):
    for c in itertools.combinations(buckets, i):
        p1 += int(sum(c) == volume)
    if p1 > 0:
        sums.append(p1)

t = time.process_time() - t
print("Problem 1: %d"%p1)
print("Problem 2: %d"%sums[0])
print("Time elapsed: %d ms"%(int(t*1000)))
