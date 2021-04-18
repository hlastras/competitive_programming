class Node:
    def __init__(self, value):
        self.input = 0
        self.output = 0
        self.childs = set()
        self.value = value

    def add_child(self, child):
        if child not in self.childs:
            self.output += 1
            self.childs.add(child)
            child.add_parent()

    def add_parent(self):
        self.input += 1

    def __repr__(self):
        return str(self.value)+" -> "+str(self.input)+"/"+str(self.output)


def add(inputs, node):
    inp = node.input
    if inp not in inputs:
        inputs[inp] = set()
    inputs[inp].add(node)

def decrease(inputs, node):
    n_input = node.input
    a = inputs[n_input]
    a.remove(node)
    node.input -= 1

    if node.input not in inputs:
        inputs[node.input] = set()

    inputs[node.input].add(node)


n_curses, m_lines = [int(x) for x in raw_input().split(" ")]

inputs = {}
nodes = {}
for i in range(1, n_curses+1):
    node = Node(i)
    nodes[i] = node


for _ in range(m_lines):
    a, b = [int(x) for x in raw_input().split(" ")]

    node_a = nodes[a]
    node_b = nodes[b]

    node_a.add_child(node_b)
    # node_b.add_parent()

for key, value in nodes.iteritems():
    n = nodes[key]
    add(inputs, n)

l = []
while True:
    # print l
    if 0 in inputs and len(inputs[0]) > 0:
        without_input_set = inputs[0]
        ch = []
        for node in without_input_set:
            l.append(node.value)
            for a in node.childs:
                ch.append(a)
            # ch = ch.union(node.childs)
        inputs[0] = set()
        for node in ch:
            decrease(inputs, node)

    else:
        break

if len(l) == n_curses:
    print ' '.join(str(x) for x in l)
else:
    print "IMPOSSIBLE"
