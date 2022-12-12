import math
import sys
lines = sys.stdin.read().split("\n")

head = [0,0]
tail = [0,0]

visited = set(["0,0"])

for line in lines:
    d, n = line.split()

    for _ in range(int(n)):
        if d == "R":
            head[0] += 1
        elif d == "L":
            head[0] -= 1
        elif d == "U":
            head[1] += 1
        elif d == "D":
            head[1] -= 1

        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            guess = [[head[0]-1,head[1]], [head[0]+1,head[1]], [head[0],head[1]-1], [head[0],head[1]+1]]
            best_d = -1
            best_p = None

            for p in guess:
                dist = math.sqrt((p[0] - tail[0])**2 + (p[1] - tail[1])**2)
                if best_d == -1 or dist < best_d:
                    best_d = dist
                    best_p = p
            tail = best_p

            visited.add(str(tail[0])+","+str(tail[1]))

print(len(visited))
