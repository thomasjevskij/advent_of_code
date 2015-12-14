import re

# a == 97
# z == 122

def inc(s):
    a = bytearray(s, 'ascii')
    for i in range(len(a)):
        i += 1
        a[-i] += 1
        if a[-i] == 123:
            a[-i] = 97
        else:
            break

    return a.decode('ascii')

def check_straight(s):
    a = bytearray(s, 'ascii')
    length = 0
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] == 1:
            length += 1
            if length == 2:
                return True
        else:
            length = 0
    return False

def check_contain(s):
    if s.find('i') == -1 and s.find('o') == -1 and s.find('l') == -1:
        return True
    return False

def check_double(s):
    r = re.compile(r'(.)\1{1,}')
    if len(r.findall(s)) >= 2:
        return True
    return False

with open('input.txt') as f:
    s = f.readline().rstrip()

while not (check_straight(s) and check_contain(s) and check_double(s)):
    s = inc(s)

print("Problem 1: %s"%s)
s = inc(s)
while not (check_straight(s) and check_contain(s) and check_double(s)):
    s = inc(s)

print("Problem 2: %s"%s)




