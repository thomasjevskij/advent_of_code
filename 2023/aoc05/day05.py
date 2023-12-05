def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    
    seeds = list(int(s) for s in lines.pop(0).split(': ')[1].split())
    lines.pop(0)
    maps = []
    while lines:
        l = lines.pop(0)
        if l.endswith('map:'):
            current = []
            continue
        if l == '':
            maps.append(current)
            continue
        current.append(tuple(int(n) for n in l.split()))
    maps.append(current)
    return seeds, maps

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def p1(seeds, maps):
    def map_seed(seed, map_list):
        for dest, source, range_len in map_list:
            offset = dest - source
            if seed >= source and seed < source + range_len:
                return seed + offset
        return seed
    
    for i in range(len(seeds)):
        for m in maps:
            seeds[i] = map_seed(seeds[i], m)
    print(min(seeds))

def p2(seeds, maps):
    def map_range(seed_range, map_list):
        result = []
        seed_start, seed_len = seed_range
        for dest, source, range_len in sorted(map_list, key=lambda x:x[1]):
            offset = dest - source
            if seed_start >= source and seed_start < source + range_len:
                res_start = seed_start + offset
                
                if source + range_len >= seed_start + seed_len:
                    result.append((res_start, seed_len))
                else:
                    new_seed_len = seed_start + seed_len - source - range_len
                    result.append((res_start, seed_len - new_seed_len))
                    seed_len = new_seed_len
                    seed_start = source + range_len
        if not result:
            result.append(seed_range)
        return result
    
    my_list = []
    for sp in pairwise(seeds):
        seed_ranges = [sp]
        for m in maps:
            new_s = []
            for s in seed_ranges:
                new_s.extend(map_range(s, m))
            seed_ranges = new_s[:]
        my_list.append(min(x for x, _ in seed_ranges))
    print(min(my_list))

seeds, maps = parse_input()

p1(seeds[:], maps[:])
p2(seeds[:], maps[:])
