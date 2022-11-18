i = list(range(1,101))*3
steps = []
for x in range(0, 300, 3):
    s = i[x] + i[x+1] + i[x+2]
    steps.append(s)

pos_p1 = 7
pos_p2 = 8
score_p1 = 0
score_p2 = 0

r = 0
while score_p1 < 1000 and score_p2 < 1000:
    if r % 2 == 0:
        # Player 1 turn
        p = steps[r%len(steps)]
        pos_p1 = (pos_p1 + p) % 10
        if pos_p1 == 0:
            pos_p1 = 10
        score_p1 += pos_p1

        
    else:
        # Player 2 turn
        p = steps[r%len(steps)]
        pos_p2 = (pos_p2 + p) % 10
        if pos_p2 == 0:
            pos_p2 = 10
        score_p2 += pos_p2

    r += 1

print(r*3*min(score_p1, score_p2))