from functools import cache

def parse_input():
    with open(0) as f:
        lines = [l.strip().split() for l in f.readlines()]
    springs = [tuple((s, tuple(map(int, nums.split(','))))) for s, nums in lines]
    return springs

@cache
def recurse(s, nums):
    if len(s) == 0: # We gobbled up the whole string
        return int(len(nums) == 0) # If we also managed to gobble up nums we win
    if s.startswith('.'): # Gobble up any '.' both in beginning and end
        return recurse(s.strip('.'), nums)
    if s.startswith('?'): # Split into two recursions
        return recurse('.'+s[1:], nums) + recurse('#'+s[1:], nums)
    if len(nums) == 0: # At this point we know the string starts with '#'
        return 0
    if len(s) < nums[0]: # Shorter string than the segment needs to be
        return 0
    if '.' in s[0:nums[0]]: # Check for hole in the potential segment
        return 0
    # At this point we know string starts with a segment that is _at least_ long enough
    if len(nums) > 1: # If we have more nums left we need to check that first segment ends properly
        # Check that s is long enough 
        if len(s) < nums[0] + 1 or s[nums[0]] == '#': # And that segment is not too long
            return 0
        return recurse(s[nums[0] + 1:], nums[1:]) # Gobble s and nums
    # If we are on our last segment, no need to check if it's long enough
    # We will gobble up the nums, and if we have characters left in s we fail later
    else: 
        return recurse(s[nums[0]:], nums[1:]) # Gobble gobble

def p1(springs):
    my_sum = sum(recurse(s, nums) for s, nums in springs)
    print(my_sum)

def p2(springs):
    my_sum = sum(recurse('?'.join([s]*5), nums*5) for s, nums in springs)
    print(my_sum)

springs = parse_input()

p1(springs[:])
p2(springs[:])
