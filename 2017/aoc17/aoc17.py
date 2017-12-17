import time

t = time.process_time()

L = 2018
buffer = [0]
jump_size = 329
cur_pos = 0

for i in range(1, L):
    cur_pos = (cur_pos + jump_size) % len(buffer)
    buffer.insert(cur_pos + 1, i)
    cur_pos += 1

t = time.process_time() - t
print(f'Problem 1: {buffer[cur_pos + 1]}')
print(f"Time elapsed: {t:.2f} s")
t = time.process_time()

cur_len = len(buffer)
p2 = buffer[1]
for i in range(L, 5*10**7):
    cur_pos = (cur_pos + jump_size) % cur_len
    if cur_pos == 0:
        p2 = i
    cur_pos += 1
    cur_len += 1

t = time.process_time() - t
print(f'Problem 2: {p2}')
print(f"Time elapsed: {t:.2f} s")