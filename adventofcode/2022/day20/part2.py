import sys
lines = sys.stdin.readlines()

class Item:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

 
items = []
for line in lines:
    value = int(line) * 811589153
    item = Item(value)
    if len(items) > 0:
        item.prev = items[-1]
        items[-1].next = item
    items.append(item)

items[-1].next = items[0]
items[0].prev = items[-1]

first = items[0]

length = len(items)-1

for _ in range(10):
    for item in items:
        if item.value == 0:
            continue

        if item == first:
            first = item.next

        item.prev.next = item.next
        item.next.prev = item.prev

        if item.value > 0:
            # Right
            it = item.next
            for x in range(1, item.value%length):
                it = it.next
            nx = it.next
            it.next = item
            item.prev = it
            item.next = nx
            nx.prev = item

        else:
            # Left
            it = item.prev
            for x in range(-1, item.value%(-length), -1):
                it = it.prev
            pv = it.prev
            it.prev = item
            item.next = it
            item.prev = pv
            pv.next = item


# Search first Zero
item = first
while item != None:
    if item.value == 0:
        break
    item = item.next

# sum values 1000, 2000, and 3000 from zero
total = 0
for i in range(1,3001):
    item = item.next
    if i%1000 == 0:
        total += item.value

print(total)

