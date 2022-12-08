import sys
lines = sys.stdin.read().split("\n")

def is_visible(i, j, grid):
    v = grid[i][j]
    visible_left = True
    visible_right = True
    visible_top = True
    visible_down = True
    
    for x in range(i-1, -1, -1):
        if grid[x][j] >= v:
            visible_top = False
            break

    for x in range(i+1, len(grid)):
        if grid[x][j] >= v:
            visible_down = False
            break

    for x in range(j-1, -1, -1):
        if grid[i][x] >= v:
            visible_left = False
            break        

    for x in range(j+1, len(grid[0])):
        if grid[i][x] >= v:
            visible_right = False
            break  

    return visible_left or visible_right or visible_top or visible_down

grid = []
for line in lines:
    grid.append([int(x) for x in line])

total = len(grid)*2 + len(grid[0])*2 - 4
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        if is_visible(i, j, grid):
            total += 1
print(total)