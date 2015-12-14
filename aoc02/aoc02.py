tot = 0
rib = 0
with open('input.txt') as f:
    for p in f.readlines():
        lwh = p.split('x')
        l = int(lwh[0])
        w = int(lwh[1])
        h = int(lwh[2])
        tot += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
        rib += 2*(l+w+h) - 2*max(l,w,h) + l*w*h

print("Problem 1: %d"%tot)
print("Problem 2: %d"%rib)
