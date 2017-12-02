import re, json, time

def all_numbers(data):
    if isinstance(data, int):
        yield data

    if isinstance(data, list):
        for value in data:
            yield from all_numbers(value)

    if isinstance(data, dict):
        for value in data.values():
            if 'red' in data.values():
                return
            yield from all_numbers(value)

t = time.process_time()
with open('input.txt') as f:
    data = f.readline().rstrip()
data1 = re.findall(r'-?\d+', data)
data2 = re.findall(r'-?\d+', str(json.loads(data, object_hook = lambda x: {} if "red" in x.values() else x)))

p1 = sum(int(a) for a in data1)
p2 = sum(int(a) for a in data2)

t = time.process_time() - t
print("Problem 1: %d"%p1)
print("Problem 2: %d"%p2)
print("Time elapsed: %d ms"%int(t * 1000))
