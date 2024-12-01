import sys
lines = sys.stdin.read().split("\n")

time = 2503
r = []
for line in lines:
    data = line.split()
    speed = int(data[3])
    fly = int(data[6])
    rest = int(data[13])

    l = [speed] * fly
    l.extend([0] * rest)
    r.append(l)

points = [0] * len(r)
distances = [0] * len(r)
for i in range(time):
    for j in range(len(r)):
        distances[j] += r[j][i%len(r[j])]

    best_distance = 0
    idx_best = []
    for j, distance in enumerate(distances):
        if distance > best_distance:
            best_distance = distance
            idx_best = [j]
        elif distance == best_distance:
            idx_best.append(j)
    for j in idx_best:
        points[j] += 1

print(max(points))

