import re

def parse_input(filename=0):
    with open(filename) as f:
        ranges, IDs = f.read().split('\n\n')
    ranges = list(
        map(
            lambda x: [int(x[0]), int(x[1])],
            re.findall(r'(\d+)-(\d+)', ranges)
        )
    )
    IDs = [int(ID) for ID in IDs.split('\n')]
    return ranges, IDs

def p1(ranges, IDs):
    s = sum(
        any(
            lower <= ID <= upper for lower, upper in ranges
        ) for ID in IDs
    )
    print(s)

def p2(ranges):
    while True:
        ranges.sort()
        before = len(ranges)
        final_ranges = [ranges[0]]
        for lower, upper in ranges[1:]:
            merged = False
            for fr in final_ranges:
                if fr[0] <= lower <= fr[1]:
                    if fr[0] <= upper <= fr[1]:
                        # Do nothing, gets eaten up by bigger
                        # range (1)
                        merged = True
                        continue
                    else:
                        # Extend range upwards (2)
                        fr[1] = upper
                        merged = True
                        continue
                if fr[0] <= upper <= fr[1]:
                    # Case (1) already handled
                    # Extend range downwards (3)
                    fr[0] = lower
                    merged = True
            if not merged:
                # Range was outside of all current ranges (4)
                final_ranges.append([lower, upper])
        if len(final_ranges) == before:
            break
        ranges = final_ranges[:]

    total = sum(
        upper - lower for lower, upper in final_ranges
    ) + len(final_ranges)
    print(total)

puzzle_input = parse_input()

p1(*puzzle_input)
p2(puzzle_input[0][:])
