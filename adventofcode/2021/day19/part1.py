import sys
import math
lines = sys.stdin.read().split("\n")[:-1]

def distance(p, p1):
    return math.sqrt((p1[0]-p[0])**2 + (p1[1]-p[1])**2 + (p1[2]-p[2])**2)

def angle(p, p1, p2):
    p12 = distance(p, p1)
    p13 = distance(p, p2)
    p23 = distance(p1, p2)
    return math.acos((p12**2 + p13**2 - p23**2) / (2 * p12 * p13))

def same(p1, p2):
    # I can't explain this
    for x in p1:
        if x in p2:
            return True
    return False

def characteristic_to_string(da, db, an):
    return str(max(da, db)) +'-'+ str(min(da, db)) +'-'+ str(an)

# Parse input
scanners = []
s = []
for l in lines:
    if l != '' and '---' in l:
        scanners.append(s)
        s = []
    elif l != '':
        coord = l.split(",")
        p = (int(coord[0]), int(coord[1]), int(coord[2]))
        s.append(p)
scanners.append(s)
scanners = scanners[1:]

# For each point (p) we will find all combinations of two other points (a and b) and buld an string with:
# distance(p to a) - distance(p to b) - angle form by this two vectors
scanner_list = []
for s in scanners:
    point_list = []
    for i, p in enumerate(s):
        point_characteristics = set()
        for j, x1 in enumerate(s):
            for k, x2 in enumerate(s):
                if i != j and i != k and j != k:
                    da = distance(p, x1)
                    db = distance(p, x2)
                    an = angle(p, x1, x2)

                    point_characteristics.add(characteristic_to_string(da, db, an))
        
        point_list.append(point_characteristics)
    scanner_list.append(point_list)


points = scanner_list[0]
for s in scanner_list[1:]:
    to_add = []
    for p1 in s:
        seen = False
        for p2 in points:
            if same(p2, p1):
                p2.update(p1)
                seen = True
                break
        if not seen:
            to_add.append(p1)
    points.extend(to_add)

print(len(points))
