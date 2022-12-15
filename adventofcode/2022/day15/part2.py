import re
import sys
lines = sys.stdin.read().split("\n")
from collections import defaultdict

def add_to_ranges(ranges, r):
    cont = True
    while cont:
        cont = False
        for r2 in ranges:
            if r2[0] <= r[1] and r2[1] >= r[0]:
                ranges.remove(r2)
                cont = True
                r = [min(r[0], r2[0]), max(r[1], r2[1])]
                break
    ranges.append(r)

ranges = defaultdict(list)
for line in lines:
    sx, sy, bx, by = [int(x) for x in re.findall(r"(\d+)", line)]
    
    d = abs(sx-bx)+abs(sy-by)
    rang = [sx-d, sx+d]
    for i in range(d+1):
        add_to_ranges(ranges[sy-i], [sx-d+i, sx+d-i])
        add_to_ranges(ranges[sy+i], [sx-d+i, sx+d-i])

keys = list(ranges.keys())
keys.sort()
for k in keys:
    r = ranges[k]
    r.sort()


for k in keys:
    r = ranges[k]
    if len(r) > 1:
        for i in range(len(r)-1):
            if r[i+1][0] - r[i][1] == 2:
                # Single point, try to validate
                point = r[i][1]+1
                prev = ranges[k-1]
                next = ranges[k+1]

                in_prev = False
                for p in prev:
                    if p[0]<= point and p[1] >= point:
                        in_prev = True
                        break

                in_next = False
                for n in next:
                    if n[0]<= point and n[1] >= point:
                        in_next = True
                        break

                if in_next and in_prev:
                    print(point*4000000 + k)
                    exit()

