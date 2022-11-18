import sys
lines = sys.stdin.read().split("\n")[:-1]

def parse(line):
    action, coord_raw =  line.split()
    coord_x_raw, coord_y_raw, coord_z_raw = coord_raw.split(",")
    x_from, x_to = coord_x_raw[2:].split("..")
    y_from, y_to = coord_y_raw[2:].split("..")
    z_from, z_to = coord_z_raw[2:].split("..")

    # Plus 1 to the end because 10..10 means 1 cube, so I transform it into range 10..11 (As example)
    return action, [int(x_from), int(x_to)+1], [int(y_from), int(y_to)+1], [int(z_from), int(z_to)+1]

def compare(x, y):
    # | * | * --> 0
    # * | * | --> 1
    # | * * | --> 2
    # * | | * --> 3
    if x[1] <= y[0] or y[1] <= x[0]:
        # don't collide 
        return -1

    if x[0] < y[0]:
        if x[1] > y[1]:
            return 2
        else:
            return 0
    else:
        if x[1] > y[1]:
            return 1
        else:
            return 3

def collide(cuboid_original, cuboid_new):
    x1, y1, z1 = cuboid_original
    x2, y2, z2 = cuboid_new

    x = compare(x1, x2)
    y = compare(y1, y2)
    z = compare(z1, z2)

    if min([x, y , z]) == -1:
        return [cuboid_original]

    result = []

    # Axis X
    x3 = []
    if x == 0:
        result.append([[x1[0], x2[0]], y1, z1])
        x3 = [x2[0], x1[1]]
    elif x == 1:
        result.append([[x2[1], x1[1]], y1, z1])
        x3 = [x1[0], x2[1]]
    elif x == 2:
        result.append([[x1[0], x2[0]], y1, z1])
        result.append([[x2[1], x1[1]], y1, z1])
        x3 = x2
    else:
        x3 = x1

    # Axis Y
    y3 = []
    if y == 0:
        result.append([x3, [y1[0], y2[0]], z1])
        y3 = [y2[0], y1[1]]
    elif y == 1:
        result.append([x3, [y2[1], y1[1]], z1])
        y3 = [y1[0], y2[1]]
    elif y == 2:
        result.append([x3, [y1[0], y2[0]], z1])
        result.append([x3, [y2[1], y1[1]], z1])
        y3 = y2
    else:
        y3 = y1

    # Axis Z
    if z == 0:
        result.append([x3, y3, [z1[0], z2[0]]])
    elif z == 1:
        result.append([x3, y3, [z2[1], z1[1]]])
    elif z == 2:
        result.append([x3, y3, [z1[0], z2[0]]])
        result.append([x3, y3, [z2[1], z1[1]]])

    return result


cuboids = []
for line in lines:
    action, x_range, y_range, z_range = parse(line)

    new_cuboids = []
    for c in cuboids:
        splited = collide(c, [x_range, y_range, z_range])
        new_cuboids.extend(splited)
    if action == 'on':
        new_cuboids.append([x_range, y_range, z_range])
    cuboids = new_cuboids


total = 0
for c in cuboids:
    x, y, z = c
    total += (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])

print(total)


