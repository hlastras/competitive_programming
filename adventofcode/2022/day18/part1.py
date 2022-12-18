import sys
lines = sys.stdin.read().split("\n")

cubes = []
total = 0
for line in lines:
    x, y, z = [int(x) for x in line.split(",")]
    total += 6
    for x2, y2, z2 in cubes:
        if abs(x-x2) + abs(y-y2) + abs(z-z2) == 1:
            total -= 2
    cubes.append((x, y, z))
print(total)