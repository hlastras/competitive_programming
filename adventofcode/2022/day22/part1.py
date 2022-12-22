import sys
import re
data, code = sys.stdin.read().split("\n\n")

def next(mapa, point):
    new_point = point.copy()
    if point[2] == 0:
        # right
        while True:
            new_point[1] = (new_point[1] + 1) % len(mapa[point[0]])
            if mapa[new_point[0]][new_point[1]] != ' ':
                return new_point
    elif point[2] == 1:
        # down
        while True:
            new_point[0] = (new_point[0] + 1) % len(mapa)
            if mapa[new_point[0]][new_point[1]] != ' ':
                return new_point
    elif point[2] == 2:
        # left
        while True:
            new_point[1] = (new_point[1] - 1) % len(mapa[point[0]])
            if mapa[new_point[0]][new_point[1]] != ' ':
                return new_point
    elif point[2] == 3:
        # up
        while True:
            new_point[0] = (new_point[0] - 1) % len(mapa)
            if mapa[new_point[0]][new_point[1]] != ' ':
                return new_point

mapa = data.split("\n")

# expand each line with spaces until max
m = 0
for line in mapa:
    m = max(m, len(line))
for i in range(len(mapa)):
    x = m-len(mapa[i])
    to_add = [' '] * x
    y = list(mapa[i])
    y.extend(to_add)
    mapa[i] = y

point = [0, 0, 0]
for i, c in enumerate(mapa[0]):
    if c == '.':
        point[1] = i
        break


for ins in re.findall(r"([\d]+|[LR])", code):
    if ins == 'R':
        point[2] = (point[2] + 1) % 4
    elif ins == 'L':
        point[2] = (point[2] - 1) % 4
    else:
        value = int(ins)
        for _ in range(value):
            n = next(mapa, point)
            if mapa[n[0]][n[1]] != "#":
                point = n
            else:
                break

print((point[0]+1)*1000 + (point[1]+1)*4 + point[2])