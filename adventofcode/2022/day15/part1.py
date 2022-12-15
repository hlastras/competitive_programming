import re
import sys
lines = sys.stdin.read().split("\n")

sensors = []
beacons = set()
for line in lines:
    sx, sy, bx, by = [int(x) for x in re.findall(r"(\d+)", line)]
    
    distance = abs(sx-bx)+abs(sy-by)
    sensors.append((sx, sy, distance))
    beacons.add((bx, by))

total = 0
target = 2000000
ranges = set()
for sx, sy, d in sensors:
    if abs(sy - target) <= d:
        x = d - abs(sy - target)
        r = (sx-x, sx+x)
        cont = True
        while cont:
            cont = False
            for r2 in ranges:
                if r2[0] <= r[1] and r2[1] >= r[0]:
                    ranges.remove(r2)
                    cont = True
                    r = (min(r[0], r2[0]), max(r[1], r2[1]))
                    break
        ranges.add(r)

for x, y in ranges:
    total += (y-x)
print(total)

