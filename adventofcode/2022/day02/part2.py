import sys
lines = sys.stdin.read().split("\n")

points = {'X': 1, 'Y': 2, 'Z': 3}
score = 0
for line in lines:
    x, y = line.split()

    if x == 'A':
        if y == 'X':
            score += points['Z']
        elif y == 'Y':
            score += points['X'] + 3
        else:
            score += points['Y'] + 6
    elif x == 'B':
        if y == 'X':
            score += points['X']
        elif y == 'Y':
            score += points['Y'] + 3
        else:
            score += points['Z'] + 6
    else:
        if y == 'X':
            score += points['Y']
        elif y == 'Y':
            score += points['Z'] + 3
        else:
            score += points['X'] + 6

print(score)