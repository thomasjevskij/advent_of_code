from itertools import islice

def parse_input(filename=0):
    with open(filename) as f:
        disk_map = [int(c) for c in f.read().strip()]
    return disk_map

def batched(iterable, n, *, strict=False):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch

def p1(disk_map):
    disk = []
    for i, nums in enumerate(batched(disk_map, 2)):
        if len(nums) == 2:
            file, free = nums
            disk.extend([i] * file)
            disk.extend([-1] * free)
        else:
            file = nums[0]
            disk.extend([i] * file)
    i = 0
    while i < len(disk):
        if all(d == -1 for d in disk[i:]):
            disk = disk[:i]
            break
        if disk[i] == -1:
            num = disk.pop()
            while num == -1:
                num = disk.pop()
            disk[i] = num
        i += 1
    s = sum(i * n for i, n in enumerate(disk))
    print(s)

def p2(disk_map):
    disk = []
    for i, nums in enumerate(batched(disk_map, 2)):
        if len(nums) == 2:
            file, free = nums
            disk.append((i,) * file)
            disk.append((-1,) * free)
        else:
            file = nums[0]
            disk.append((i,) * file)
    for i, nums in enumerate(batched(disk_map[::-1], 2)):
        if len(nums) == 2:
            l_file, _ = nums
            ii = len(disk_map) // 2 - i
            file = (ii,) * l_file
            i_file = disk.index(file)
            for i_empty, empty in enumerate(disk[:i_file]):
                if -1 in empty and len(empty) >= l_file:
                    disk.insert(i_file, (-1,) * l_file)
                    disk.remove(file)
                    disk.remove(empty)
                    disk.insert(i_empty, (-1,) * (len(empty) - l_file))
                    disk.insert(i_empty, file)
                    break
    s = 0
    i = 0
    for d in disk:
        s += sum(j * num for j, num in enumerate(d, start=i) if num != -1)
        i += len(d)
    print(s)

puzzle_input = parse_input()

p1(puzzle_input[:])
p2(puzzle_input[:])