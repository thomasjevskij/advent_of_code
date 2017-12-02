import re, time

def get_lights(start, stop):
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            yield "%d,%d"%(x,y)

t1 = time.process_time()
p1 = set()
l = {}
finder = re.compile(r'([0-9]*),([0-9]*)')

with open('input.txt') as f:
    for s in f.readlines():
        t = finder.findall(s)

        for light in get_lights((int(t[0][0]),int(t[0][1])),(int(t[1][0]),int(t[1][1]))):
            if s.startswith("turn on"):
                if light in l:
                    l[light] += 1
                else:
                    l[light] = 1
                p1.add(light)
            if s.startswith("turn off"):
                if light in l:
                    l[light] = max(0, l[light]-1)
                else:
                    l[light] = 0
                p1.discard(light)
            if s.startswith("toggle"):
                if light in l:
                    l[light] += 2
                else:
                    l[light] = 2
                if light in p1:
                    p1.remove(light)
                else:
                    p1.add(light)

t1 = time.process_time() - t1
print("Problem 1: %d"%len(p1))
print("Problem 2: %d"%sum(l[light] for light in l))
print("Time elapsed: %f s"%t1)
