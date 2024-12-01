cost = [
    [(4, 0)],
    [(2, 0)],
    [(3, 0,), (14, 1)],
    [(2, 0,), (7, 2)]
]

cost = [
    [(4, 0)],
    # [(2, 0)],
    # [(3, 0,), (14, 1)],
    # [(2, 0,), (7, 2)]
]


def calculate(row, idx, idx_stop, maximum):
    if row[idx][0] < 4:
        return row[idx]

    current = row[idx][0]
    m = row[idx][1]
    for _ in range(idx, idx_stop):
        added = 0
        if current >= 4 and m + (current // 4) <= maximum:
            added = (current // 4)
            current -= (current // 4) * 4
        current += m
        m += added

    return [current, m]


dp = []
row = []
for i in range(25):
    row.append([i,1])
dp.append(row)

# robot_cost = cost[0]

for i in range(2,50):
    row = [dp[-1][0]]
    for x in range(1,len(dp[-1])):
        best = dp[-1][x]
        for j in range(0, x):
            val = calculate(dp[-1], j, x, i)
            if val[0] > best[0]:
                best = val
        row.append(best)
    dp.append(row)





for r in dp:
    print(r)