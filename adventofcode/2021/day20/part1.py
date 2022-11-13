import sys
lines = sys.stdin.read().split("\n")[:-1]

def build_next_matrix(image, c):
    # Expand the current image fill with the current infinite character
    lenght = len(image) + 2
    new_image = [[c for _ in range(lenght)] for _ in range(lenght)]
    return new_image

def calculate_index(image, x, y, default):
    exp = 8
    total = 0
    for i in range(x-2, x+1):
        for j in range(y-2, y+1):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                # We ar out of previous image
                if default == '#':
                    total += 2**exp
            else:
                # We are inside of previous image
                if image[i][j] == '#':
                    total += 2**exp
            exp -= 1
    return total

iea = lines[0]
rounds = 2 
lenght = len(lines[2])

image = lines[2:]

current_c = '.'
for r in range(rounds):
    new_image = build_next_matrix(image, current_c)

    for x in range(len(new_image)):
        for y in range(len(new_image[0])):
            idx = calculate_index(image, x, y, current_c)
            new_image[x][y] = iea[idx]

    image = new_image
    if current_c == '.':
        current_c = iea[0]
    else: 
        current_c = iea[-1]


total = 0
for l in image:
    for c in l:
        if c == '#':
            total += 1

print(total)