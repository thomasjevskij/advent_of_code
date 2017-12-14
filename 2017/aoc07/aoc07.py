import time

t = time.process_time()

class Node:
    def __init__(self, name):
        self.name = name
        self.weight = -1
        self.parent = None
        self.children = []

    def add_parent(self, parent):
        parent.children.append(self)
        if parent == 'gyxo':
            print(parent)
        self.parent = parent

    def weight_children(self):
        weight = self.weight
        if len(self.children) == 0:
            return weight
        for c in self.children:
            weight += c.weight_children()
        return weight

with open('in') as f:
    tower_in = f.readlines()

tree = dict()
for p in tower_in:
    args = p.replace(',','').split()
    parent, weight = args[0:2]
    if parent not in tree:
        tree[parent] = Node(parent)
    tree[parent].weight = int(weight[1:-1])
    if len(args) > 2:
        children = args[3:]
        for c in children:
            if c not in tree:
                tree[c] = Node(c)
            tree[c].add_parent(tree[parent])

p = tree[parent]
while p is not None:
    root = p.name
    p = p.parent
print(root)
bins = dict()
for c in tree[root].children:
    print(c.name, c.weight_children())
# I traversed the tree manually because the question was confusing

t = time.process_time() - t
print("Time elapsed: {0:.2f} s".format(t))
