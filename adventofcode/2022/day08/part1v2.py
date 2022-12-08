import sys
lines = sys.stdin.read().split("\n")

def is_visible(i, j, grid):
    v = grid[i][j]
    top = all(grid[x][j] < v for x in range(i-1, -1, -1))
    bottom = all(grid[x][j] < v for x in range(i+1, len(grid)))
    left = all(grid[i][x] < v for x in range(j-1, -1, -1))
    right = all(grid[i][x] < v for x in range(j+1, len(grid[0])))
    return any([top, bottom, left, right])

grid = []
for line in lines:
    grid.append([int(x) for x in line])

total = len(grid)*2 + len(grid[0])*2 - 4
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        if is_visible(i, j, grid):
            total += 1
print(total)