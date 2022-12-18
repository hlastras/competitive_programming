import sys
lines = sys.stdin.read().split("\n")


def neigbours(x,y,z, seen):
    result = 0
    if (x+1,y,z) in seen:
        result += 1
    if (x-1,y,z) in seen:
        result += 1
    if (x,y+1,z) in seen:
        result += 1
    if (x,y-1,z) in seen:
        result += 1
    if (x,y,z+1) in seen:
        result += 1
    if (x,y,z-1) in seen:
        result += 1
    
    return result


cubes = []
total = 0
top = 0
down = 100
seen = set()
for line in lines:
    x, y, z = [int(x) for x in line.split(",")]
    total += 6
    for x2, y2, z2 in cubes:
        if abs(x-x2) + abs(y-y2) + abs(z-z2) == 1:
            total -= 2
    cubes.append((x, y, z))
    top = max(top, x, y, z)
    down = min(down, x, y, z)
    seen.add((x, y , z))


empty = set()
processed = set()
for x in range(down-2, top+2):
    for y in range(down-2, top+2):
        for z in range(down-2, top+2):
            if (x,y,z) not in seen:
                empty.add((x,y,z))

queue = [(down-2,down-2,down-2)]
while len(queue) > 0:
    x, y, z = queue[0]
    queue = queue[1:]

    if (x,y,z) in processed:
        continue

    if (x+1,y,z) in empty:
        queue.append((x+1,y,z))
    if (x-1,y,z) in empty:
        queue.append((x-1,y,z))
    if (x,y+1,z) in empty:
        queue.append((x,y+1,z))
    if (x,y-1,z) in empty:
        queue.append((x,y-1,z))
    if (x,y,z+1) in empty:
        queue.append((x,y,z+1))
    if (x,y,z-1) in empty:
        queue.append((x,y,z-1))

    empty.remove((x,y,z))
    processed.add((x,y,z))

for x, y, z in empty:
    total -= neigbours(x, y, z, seen)
print(total)