import sys
lines = sys.stdin.read().split("\n")

class Node:
    def __init__(self, is_folder, name, size, parent):
        self.is_folder = is_folder
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
    
    def add_child(self, child):
        if self.is_folder:
            self.children.append(child)
            self.increase_size(child.size)

    def increase_size(self, size):
        if self.is_folder:
            self.size += size
            if self.parent != None:
                self.parent.increase_size(size)
    
    def get_child(self, name):
        if self.is_folder:
            for node in self.children:
                if node.name == name:
                    return node
        return None

root = Node(True, "/", 0, None)
current = root

for line in lines:
    if line[0] == "$":
        # Is command
        if line[2:4] == "cd" and line[5:] == "/":
            current == root
        elif line[2:4] == "cd" and line[5:] == "..":
            current = current.parent
        elif line[2:4] == "cd":
            current = current.get_child(line[5:])
    else:
        # Is the output of a $ ls
        if line[:3] == "dir":
            # Create dir
            n = Node(True, line[4:], 0, current)
            current.add_child(n)
        else:
            # Create file
            size, name = line.split()
            size = int(size)
            n = Node(False, name, size, current)
            current.add_child(n)

queue = [root]
total = 0
while len(queue) > 0:
    node = queue[0]
    queue = queue[1:]
    
    if node.size <= 100000:
        total += node.size

    for c in node.children:
        if c.is_folder:
            queue.append(c)
print(total)
