import hashlib, time

t = time.process_time()
with open('input.txt') as f:
    key = f.readline().rstrip()

i = 1
p1 = -1
p2 = -1
done = False
while not done:
    k = "%s%d" % (key, i)
    m = hashlib.md5()
    m.update(k.encode('utf-8'))
    s = m.hexdigest()
    if s.startswith('00000') and p1 == -1:
        p1 = i
    if s.startswith('000000'):
        p2 = i
        break
    i += 1

t = time.process_time() - t    
print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
print("Time elapsed: %f s"%t)
