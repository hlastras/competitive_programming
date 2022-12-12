import sys
lines = sys.stdin.read().split("\n")

matrix = []
for line in lines:
    matrix.append([ord(x) for x in line])


start = (-1, -1)
end = (-1, -1)
for i, row in enumerate(matrix):
    for j, c in enumerate(row):
        if c == ord("S"):
            start = (i, j)
        if c == ord("E"):
            end = (i, j)

matrix[start[0]][start[1]] = ord("a")
matrix[end[0]][end[1]] = ord("z")


to_check = []
for i, row in enumerate(matrix):
    for j, c in enumerate(row):
        if c == ord("a"):
            to_check.append((i, j))

best = -1

for start in to_check:
    distances = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
    distances[start[0]][start[1]] = 0
    queue = [start]
    while len(queue) > 0:
        x, y = queue[0]
        queue = queue[1:]
        value = matrix[x][y]
        dist = distances[x][y]

        # Up
        if x-1 >= 0 and distances[x-1][y] == -1 and matrix[x-1][y]<=value+1:
            queue.append((x-1, y))
            distances[x-1][y] = dist+1

        # down
        if x+1 < len(matrix) and distances[x+1][y] == -1 and matrix[x+1][y]<=value+1:
            queue.append((x+1, y))
            distances[x+1][y] = dist+1

        # left
        if y-1 >= 0 and distances[x][y-1] == -1 and matrix[x][y-1]<=value+1:
            queue.append((x, y-1))
            distances[x][y-1] = dist+1

        # left
        if y+1 < len(matrix[0]) and distances[x][y+1] == -1 and matrix[x][y+1]<=value+1:
            queue.append((x, y+1))
            distances[x][y+1] = dist+1

    if distances[end[0]][end[1]] >0 and (best == -1 or distances[end[0]][end[1]] < best):
        best = distances[end[0]][end[1]]
    
print(best)