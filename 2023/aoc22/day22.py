from collections import defaultdict, deque

def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    bricks = []
    for l in lines:
        start, stop = l.split('~')
        xs, ys, zs = (int(c) for c in start.split(','))
        xe, ye, ze = (int(c) for c in stop.split(','))
        bricks.append(((xs, xe), (ys, ye), (zs, ze)))
    return bricks

def intersection(interval1, interval2):
    new_min = max(interval1[0], interval2[0])
    new_max = min(interval1[1], interval2[1])
    return new_min <= new_max

def p1(bricks):
    landed = []
    supports = defaultdict(list)
    rests_on = defaultdict(list)
    while bricks:
        # Find brick closest to bottom
        b = min(bricks, key=lambda x: x[2][0])
        bricks.remove(b)
        bottom = 1
        candidates = []
        for l in landed:
            if intersection(l[0], b[0]) and intersection(l[1], b[1]):
                if l[2][1] + 1 >= bottom:
                    bottom = l[2][1] + 1
                    candidates.append(l)

        x, y, (zs, ze) = b
        diff = ze-zs
        b = (x, y, (bottom, bottom + diff))
        landed.append(b)
        for c in candidates:
            if c[2][1] + 1 == bottom:
                supports[c].append(b)
                rests_on[b].append(c)

    s = 0
    for l in landed:
        for sup in supports[l]:
            if len(rests_on[sup]) == 1:
                break
        else:
            s+=1
    print(s)
    
    return landed, supports, rests_on
        

def p2(landed, supports, rests_on):
    m = 0
    for root in landed:
        q = deque()
        # Same check as in p1 but here we _want_ those bricks
        for sup in supports[root]:
            if len(rests_on[sup]) == 1:
                q.append(sup)
        # Keep track of which bricks we collapse
        collapsed = set()
        # Count root as collapsed.. for now
        collapsed.add(root)
        while q:
            # Current brick
            brick = q.popleft()
            # We collapse it
            collapsed.add(brick)
            # Check all the bricks it supports
            for sup in supports[brick]:
                # If a brick has lost all its supporting bricks
                # add it here
                if all(r in collapsed for r in rests_on[sup]):
                    q.append(sup)
        # Remember we added the original, disintegrated brick.
        # Don't count it!
        m += len(collapsed) - 1
    print(m)

bricks = parse_input()

stuff = p1(bricks[:])
p2(*stuff)
