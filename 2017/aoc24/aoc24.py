import time

class Node:
    def __init__(self, val, components, connector, depth = 0, parent = None):
        self.parent = parent
        self.val = val
        self.children = []
        self.depth = depth
        possibleChildren = list(x for x in components if connector in x)
        if len(possibleChildren) > 0:
            for c in possibleChildren:
                newComponents = components[:]
                nextConnector = c[0] if c[1] == connector else c[1]
                newComponents.remove(c)
                self.children.append(Node(c, newComponents, nextConnector, depth + 1, self))
    def strength(self):
        if len(self.children) == 0:
            return sum(self.val)
        return sum(self.val) + max(x.strength() for x in self.children)
    def deepest(self, nodes): # Empirically figured out deepest depth
        if len(self.children) > 0:
            for c in self.children:
                c.deepest(nodes)
        if self.depth == 39:
            nodes.append(self)
        return
    def strength_upwards(self):
        if self.parent is None:
            return sum(self.val)
        return sum(self.val) + self.parent.strength_upwards()
        
t = time.process_time()

with open('in') as f:
    components = f.read().split('\n')

components = list(map(lambda x: tuple(map(int, x.split('/'))), (c for c in components)))
zeroes = list(x for x in components if 0 in x)
m = -1
deepest = []
for z in zeroes:
    newComponents = components[:]
    connector = z[0] if z[1] == 0 else z[1]
    newComponents.remove(z)
    n = Node(z, newComponents, connector)
    m = max(m, n.strength())
    temp = []
    n.deepest(temp)
    deepest.extend(temp)

print(f"Problem 1: {m}")
print(f"Problem 2: {max(n.strength_upwards() for n in deepest)}")
t = time.process_time() - t
print(f"Time elapsed: {t:.2f} s")
