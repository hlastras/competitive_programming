from collections import defaultdict
pattern = input()

pieces = [
    [
        [True, True, True, True]
    ],
    [
        [False, True, False],
        [True, True, True],
        [False, True, False]
    ],
    [
        [True, True, True],
        [False, False, True],
        [False, False, True]
    ],
    [
        [True],
        [True],
        [True],
        [True]
    ],
    [
        [True, True],
        [True, True]
    ]

]

matrix = [[True, False, False, False, False, False, False, False, True] for _ in range(4)]
matrix.append([True]*9)

coincidences = defaultdict(list)
totals = []
count = 0
last_empty_line = 4
patter_idx = 0
for round in range(202200):
    # Try to search a cycle
    if (round%len(pieces), patter_idx%len(pattern)) in coincidences:
        count += 1
        item = coincidences[(round%len(pieces), patter_idx%len(pattern))]
        
        item.append((round, len(matrix)-1-last_empty_line))
        totals.append(len(matrix)-1-last_empty_line)

        if len(item) >= 3: 
            if item[-1][0] - item[-2][0] == item[-2][0] - item[-3][0]:
                if item[-1][0] - item[-2][0] <= count:
                    cicle_lenght = item[-1][0] - item[-2][0]
                    cycle_increase = totals[-1] - totals[-1-cicle_lenght]
                    old_round = round - cicle_lenght
                    x = 1000000000000 - old_round
                    remain = x%cicle_lenght
                    print((x//cicle_lenght)*cycle_increase + totals[old_round-1] + (totals[old_round+remain] - totals[old_round-1]))
                    exit()
    else:
        count = 0
        coincidences[(round%len(pieces), patter_idx%len(pattern))].append((round, len(matrix)-1-last_empty_line))
        totals.append(len(matrix)-1-last_empty_line)



    piece = pieces[round%len(pieces)]

    for _ in range(4-last_empty_line):
        matrix.insert(0, [True, False, False, False, False, False, False, False, True])
        last_empty_line += 1

    x = 0
    y = 3
    while True:
        if pattern[patter_idx%len(pattern)] == '>':
            # Check if piece can be moved to the right
            collide = False
            for row in range(len(piece)-1, -1, -1):
                for col in range(len(piece[0])-1, -1, -1):
                    if piece[row][col]:
                        if x-row >= 0 and matrix[x-row][y+col+1] :
                            collide = True
                        break
            
            if not collide:
                y += 1

        else:
            # Check if piece can be moved to the left
            collide = False
            for row in range(len(piece)):
                for col in range(len(piece[0])):
                    if piece[row][col]:
                        if x-row >= 0 and matrix[x-row][y+col-1] :
                            collide = True
                        break
            
            if not collide:
                y -= 1

        patter_idx += 1

        
        # Check if piece can be moved down
        collide = False
        for col in range(len(piece[0])):
            for row in range(len(piece)):
                if piece[row][col]:
                    if matrix[x+1-row][y+col]:
                        collide = True
                    break
        
        if collide:
            for col in range(len(piece[0])):
                for row in range(len(piece)):
                    matrix[x-row][y+col] = matrix[x-row][y+col] or piece[row][col]
            break
        else:
            x += 1

    last_empty_line = min(last_empty_line, x-len(piece)+1)

print(len(matrix) - last_empty_line - 1)
