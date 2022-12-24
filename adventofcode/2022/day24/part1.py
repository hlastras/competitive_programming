import sys
mapa = sys.stdin.read().split("\n")

for i in range(len(mapa)):
    mapa[i] = [str(x) for x in mapa[i]]

def can_move(mapa, x, y):
    if x < 0 or y < 0 or x >= len(mapa) or y >= len(mapa[0]):
        return False
    return mapa[x][y] == '.'

count = 0
bliz = {}
for x in range(1, len(mapa)-1):
    for y in range(1,len(mapa[0])-1):
        if mapa[x][y] != '.':
            bliz[count] = [x, y, mapa[x][y]]
            count += 1

target = (len(mapa)-1, len(mapa[0])-2)
positions = {(0,1): 0}
while True:
    for x in range(1, len(mapa)-1):
        for y in range(1,len(mapa[0])-1):
            mapa[x][y] = '.'

    for k, v in bliz.items():
        if v[2] == '>':
            v[1] += 1
            if v[1] == len(mapa[0])-1:
                v[1] = 1
        elif v[2] == '<':
            v[1] -= 1
            if v[1] == 0:
                v[1] = len(mapa[0]) - 2 
        elif v[2] == 'v':
            v[0] += 1
            if v[0] == len(mapa) - 1:
                v[0] = 1
        elif v[2] == '^':
            v[0] -= 1
            if v[0] == 0:
                v[0] = len(mapa) - 2

        if mapa[v[0]][v[1]] != '.':
            if type(mapa[v[0]][v[1]]) == int:
                mapa[v[0]][v[1]] += 1
            else:
                mapa[v[0]][v[1]] = 2
        else:
            mapa[v[0]][v[1]] = v[2]


    next_positions = {}
    for pos, v in positions.items():
        if mapa[pos[0]][pos[1]] == '.':
            # Stay
            next_positions[(pos[0], pos[1])] = v+1
        
        if can_move(mapa, pos[0]-1, pos[1]):
            # Up
            next_positions[(pos[0]-1, pos[1])] = v+1
        
        if can_move(mapa, pos[0]+1, pos[1]):
            # down
            next_positions[(pos[0]+1, pos[1])] = v+1
        
        if can_move(mapa, pos[0], pos[1]-1):
            # left
            next_positions[(pos[0], pos[1]-1)] = v+1
        
        if can_move(mapa, pos[0], pos[1]+1):
            # right
            next_positions[(pos[0], pos[1]+1)] = v+1
    
    positions = next_positions
    if target in positions:
        print(positions[target])
        break

    


