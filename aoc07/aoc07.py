import re, time

def get_val(s, wires):
    #literal
    if wires[s].isdigit():
        return wires[s]

    args = wires[s].split()
    #AND statement: a AND b, a and b can be both wires and literals
    if re.search(r'AND', wires[s]):
        if args[0].isdigit():
            args[0] = int(args[0])
        else:
            args[0] = int(get_val(args[0], wires))
        if args[2].isdigit():
            args[2] = int(args[2])
        else:
            args[2] = int(get_val(args[2], wires))

        wires[s] = "%d"%(args[0] & args[2])
        return wires[s]
    #OR statement: a OR b, a and b can be both wires and literals
    if re.search(r'OR', wires[s]):
        if args[0].isdigit():
            args[0] = int(args[0])
        else:
            args[0] = int(get_val(args[0], wires))
        if args[2].isdigit():
            args[2] = int(args[2])
        else:
            args[2] = int(get_val(args[2], wires))

        wires[s] = "%d"%(args[0] | args[2])
        return wires[s]
    #SHIFT statements: a XSHIFT n, a is always wire, n is always literal
    if re.search(r'LSHIFT', wires[s]):
        wires[s] = "%d"%(int(get_val(args[0], wires)) << int(args[2]))
        return wires[s]

    if re.search(r'RSHIFT', wires[s]):
        wires[s] = "%d"%(int(get_val(args[0], wires)) >> int(args[2]))
        return wires[s]
    #NOT statement: NOT a, a is always a wire (probably
    if re.search(r'NOT', wires[s]):
        wires[s] = "%d"%(65535 & ~int(get_val(args[1], wires)))
        return wires[s]
    wires[s] = get_val(wires[s], wires)
    return wires[s]

t = time.process_time()
w = {}    
with open('input.txt') as f:
    for line in f.readlines():
        args = line.split(' -> ')
        w[args[1].strip()] = args[0].strip()

a = get_val('a', w)
t = time.process_time() - t
print("Problem 1: %s"%a)
print("Time elapsed: %d ms"%int(t * 1000))

t = time.process_time()
w.clear()
with open('input.txt') as f:
    for line in f.readlines():
        args = line.split(' -> ')
        w[args[1].strip()] = args[0].strip()
w['b'] = a

t = time.process_time() - t
print("Problem 2: %s"%get_val('a', w))
print("Time elapsed: %d µs"%int(t * 1000000))
