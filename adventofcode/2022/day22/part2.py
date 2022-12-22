import sys
import re
data, code = sys.stdin.read().split("\n\n")

zones = [
    [[0,49], [50,99]],
    [[0,49], [100,149]],
    [[50,99], [50,99]],
    [[100,149], [50,99]],
    [[100,149], [0,49]],
    [[150,199], [0,49]]
]

functions = {
    0:{
        2: lambda x, y: [149-x, 0, 0],
        3: lambda x, y: [y+100, 0, 0]
    },
    1:{
        0: lambda x, y: [149-x, 99, 2],
        1: lambda x, y: [y-50, 99, 2],
        3: lambda x, y: [199, y-100, 3]
    },
    2:{
        0: lambda x, y: [49, x+50, 3],
        2: lambda x, y: [100, x-50, 1]
    },
    3:{
        0: lambda x, y: [149-x, 149, 2],
        1: lambda x, y: [y+100, 49, 2]
    },
    4:{
        2: lambda x, y: [149-x, 50, 0],
        3: lambda x, y: [y+50, 50, 0]
    },
    5:{
        0: lambda x, y: [149, x-100, 3],
        1: lambda x, y: [0, y+100, 1],
        2: lambda x, y: [0, x-100, 1]
    },
}


def next(mapa, point):
    new_point = point.copy()
    if point[2] == 0:
        # right
        new_point[1] += 1
    elif point[2] == 1:
        # down
        new_point[0] += 1
    elif point[2] == 2:
        # left
        new_point[1] -= 1
    elif point[2] == 3:
        # up
        new_point[0] -= 1

    if (new_point[0] >= 0 and 
        new_point[0] < len(mapa) and 
        new_point[1] >= 0 and 
        new_point[1] < len(mapa[new_point[0]]) and 
        mapa[new_point[0]][new_point[1]] != ' '):
            return new_point

    # Point out of map, calculate next
    for i, x in enumerate(zones):
        if point[0] >= x[0][0] and point[0] <= x[0][1] and point[1] >= x[1][0] and point[1] <= x[1][1]:
            func = functions[i][point[2]]
            return func(point[0], point[1])

mapa = data.split("\n")



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





