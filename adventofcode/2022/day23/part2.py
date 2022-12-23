import sys
mapa = sys.stdin.read().split("\n")

def increase_map(mapa):
    new_map = []
    new_map.append(['.'] * (len(mapa)+2))
    for row in mapa:
        new_row = ['.']
        new_row.extend(row)
        new_row.append('.')
        new_map.append(new_row)
    new_map.append(['.'] * (len(mapa)+2))

    return new_map

def any_around(mapa, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if x != i or y != j:
                if mapa[i][j] == '#':
                    return True
    return False

def where_move(moves, mapa, x, y):
    for m in moves:
        if m == 'N':
            if mapa[x-1][y-1] == "." and mapa[x-1][y] == "." and mapa[x-1][y+1] == ".":
                return (x-1, y)
        elif m == 'S':
            if mapa[x+1][y-1] == "." and mapa[x+1][y] == "." and mapa[x+1][y+1] == ".":
                return (x+1, y)
        elif m == 'W':
            if mapa[x-1][y-1] == "." and mapa[x][y-1] == "." and mapa[x+1][y-1] == ".":
                return (x, y-1)
        elif m == 'E':
            if mapa[x-1][y+1] == "." and mapa[x][y+1] == "." and mapa[x+1][y+1] == ".":
                return (x, y+1)

moves = ['N', 'S', 'W', 'E']

c = 0
any_move = True
expand = True
while any_move:
    c += 1
    if expand:
        mapa = increase_map(mapa)
    expand = False
    any_move = False
    
    positions = {}
    for x in range(1,len(mapa)-1):
        for y in range(1, len(mapa[0])-1):
            if mapa[x][y] == "#":
                if any_around(mapa, x, y):
                    move_to = where_move(moves, mapa, x, y)
                    if move_to == None:
                        move_to = (x, y)

                    if move_to not in positions:
                        positions[move_to] = (x, y)
                    else:
                        old = positions.pop(move_to)
                        positions[old] = old
                        positions[(x,y)] = (x,y)
                else:
                    positions[(x,y)] = (x,y)
    
    moves.append(moves[0])
    moves = moves[1:]

    for x in range(len(mapa)):
        for y in range(len(mapa[0])):
            mapa[x][y] = '.'

    for key in positions:
        if positions[key] != key:
            any_move = True
        if key[0] == 1 or key[0] == len(mapa)-1 or key[1] == 1 or key[1] == len(mapa[0])-1:
            expand = True
        mapa[key[0]][key[1]] = '#'

print(c)

