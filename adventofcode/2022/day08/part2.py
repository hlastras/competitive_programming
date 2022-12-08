import sys
lines = sys.stdin.read().split("\n")

def scenic_score(i, j, grid):
    v = grid[i][j]
    visible_left = j
    visible_right = len(grid[0]) - j - 1
    visible_top = i
    visible_down = len(grid) - i - 1
    
    for x in range(i-1, -1, -1):
        if grid[x][j] >= v:
            visible_top = i-x
            break

    for x in range(i+1, len(grid)):
        if grid[x][j] >= v:
            visible_down = x-i
            break

    for x in range(j-1, -1, -1):
        if grid[i][x] >= v:
            visible_left = j-x
            break        

    for x in range(j+1, len(grid[0])):
        if grid[i][x] >= v:
            visible_right = x-j
            break

    return visible_left * visible_right * visible_top * visible_down

grid = []
for line in lines:
    grid.append([int(x) for x in line])

best = -1
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        best = max(best, scenic_score(i, j, grid))
print(best)
