import sys
lines = sys.stdin.read().split("\n")

matrix = [['.'] * 600 for _ in range(200)]

paths = []
for line in lines:
    path = [[int(value) for value in point.split(",")] for point in line.split(" -> ")]
    paths.append(path)

end = 0
for path in paths:
    current = path[0]
    for point in path[1:]:
        end = max(end, current[1])
        
        if current[0] == point[0]:
            direction = 1
            if current[1] > point[1]:
                direction = -1
            for x in range(current[1], point[1]+direction, direction):
                matrix[x][point[0]] = "#"
        
        elif current[1] == point[1]:
            direction = 1
            if current[0] > point[0]:
                direction = -1
            for y in range(current[0], point[0]+direction, direction):
                matrix[point[1]][y] = "#"

        current = point
       

i = 0
while True:
    x = 0
    y = 500

    while True:
        if x > end:
            # for row in matrix:
            #     print(''.join(row[450:]))
            print(i)
            exit(0)
        if matrix[x+1][y] == ".":
            x += 1
        elif matrix[x+1][y-1] == ".":
            x += 1
            y -= 1
        elif matrix[x+1][y+1] == ".":
            x += 1
            y += 1
        else:
            matrix[x][y]="o"
            break
    i+=1

