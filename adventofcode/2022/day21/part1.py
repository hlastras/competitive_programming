import sys
lines = sys.stdin.read().split("\n")

class Node:
    def __init__(self, name):
        self.name = name
        self.operation = None
        self.value = None
        self.left = None
        self.right = None

def process(node):
    if node.value != None:
        return node.value

    left_value = process(node.left)
    right_value = process(node.right)
    if node.operation == "+":
        node.value = left_value + right_value
    elif node.operation == "-":
        node.value = left_value - right_value
    elif node.operation == "*":
        node.value = left_value * right_value
    elif node.operation == "/":
        node.value = left_value // right_value
    else:
        print(node.operation)
    
    return node.value

data = {}
for line in lines:
    x = line.split()

    name = x[0][:-1]
    if name not in data:
        data[name] = Node(name)
    node = data[name]

    if len(x) == 2:
        node.value = int(x[1])
    else:
        if x[1] not in data:
            data[x[1]] = Node(x[1])
        if x[3] not in data:
            data[x[3]] = Node(x[3])

        node.left = data[x[1]]
        node.right = data[x[3]]
        node.operation = x[2]


print(process(data["root"]))
