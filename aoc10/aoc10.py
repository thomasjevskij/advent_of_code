def look_say(s):
    current = s[0]
    count = 0
    new = ''
    for c in s:
        if c != current:
            new += str(count) + current
            current = c
            count = 0
        count += 1
    new += str(count) + current
    return new
    
with open('input.txt') as f:
    s = f.readline().rstrip()
for i in range(40):
    s = look_say(s)
print("Problem 1: %d"%len(s))
for i in range(10):
    s = look_say(s)
print("Problem 2: %d"%len(s))
