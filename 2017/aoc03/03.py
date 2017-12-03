from math import sqrt
from collections import defaultdict
p = 277678

#sqrt(p) is even, odd sqrts are bottom right corners
#from bottom right corners, distance is the root - 1
distance = int(sqrt(p)+1)**2 - p
#distance is the distance of the number from the corner,
#supposing they are on the same row

print(int(sqrt(p))-distance)

#generate cartesian coordinates in a spiral
def spiral(N, M):
    x,y = 0,0   
    dx, dy = 0, -1

    for dumb in range(N*M):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
            dx, dy = -dy, dx            # corner, change direction

        if abs(x)>N/2 or abs(y)>M/2:    # non-square
            dx, dy = -dy, dx            # change direction
            x, y = -y+dx, x+dy          # jump

        yield x, y
        x, y = x+dx, y+dy

A = 9
data = defaultdict(int)
data[(0, 0)] = 1
for a, b in spiral(A, A):
    data[(a, b)] = sum(data[(a+x,b+y)] for x in range(-1, 2) for y in range(-1, 2))
    if data[(a,b)] > p:
        print(data[(a,b)])
        break
