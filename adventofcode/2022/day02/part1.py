import sys
lines = sys.stdin.read().split("\n")

points = {'R': 1, 'P': 2, 'S': 3}
trans = {'X': 'R', 'A': 'R', 'Y': 'P', 'B': 'P', 'Z': 'S', 'C': 'S'}
draw = 3
win = 6
score = 0
for line in lines:
    x, y = line.split()
    x = trans[x]
    y = trans[y]
    score += points[y]

    if x == 'R':
        if y == 'R':
            score += draw
        elif y == 'P':
            score += win
    elif x == 'P':
        if y == 'P':
            score += draw
        elif y == 'S':
            score += win
    else:
        if y == 'S':
            score += draw
        elif y == 'R':
            score += win

print(score)