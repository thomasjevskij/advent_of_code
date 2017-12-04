problem1 = 0
problem2 = 0
with open('input.txt') as f:
    for line in f.readlines():
        passphrase = line.split()
        if len(passphrase) == len(set(passphrase)):
            problem1+= 1
        if len(passphrase) == len(set(''.join(sorted(word)) for word in passphrase)):
            problem2+= 1
print(problem1)
print(problem2)
