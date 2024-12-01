cost = [
    [(4, 0)],
    [(2, 0)],
    [(3, 0,), (14, 1)],
    [(2, 0,), (7, 2)]
]

cost = [
    [(4, 0)],
    [(2, 0)]
]


def calculate(matrix, idx, idx_stop, maximum, robot_cost, ri):
    current = []
    m = []
    for row in matrix:
        current.append(row[idx][0])
        m.append(row[idx][1])

    for _ in range(idx, idx_stop):
        added = [0] * len(matrix)
        valid = True

        for amount, robot_idx in robot_cost:
            if current[robot_idx] >= amount and m[robot_idx] + (current[robot_idx] // amount) <= maximum:
                added[robot_idx] = current[robot_idx] // amount
                current[robot_idx] -= (current[robot_idx] // amount) * amount
            else:
                valid = False

        for idx, m_value in enumerate(m):
            current[idx] += m_value

        if valid:
            for idx, a in enumerate(added):
                m[idx] += a

    print(current, m, [current[ri], m[ri]])
    return [current[ri], m[ri]]

# Build initial dp table(cube)
dp = []
matrix = []
row = []
for i in range(25):
    row.append([i,1])
matrix.append(row)

for _ in range(len(cost)-1):
    row = []
    for i in range(25):
        row.append([0, 0])
    matrix.append(row)
dp.append(matrix)



for i in range(2,30):
    matrix = []
    for r_idx, robot_cost in enumerate(cost):
        # print(r_idx, robot_cost)
        previous_robot_line = dp[-1][r_idx]
        row = [previous_robot_line[0]]
        for x in range(1,len(previous_robot_line)):
            best = previous_robot_line[x]
            for j in range(0, x):
                val = calculate(dp[-1], j, x, i, robot_cost, r_idx)
                print(r_idx, robot_cost, x, val, best)
                if val[0] > best[0]:
                    best = val
            row.append(best)
        matrix.append(row)
    dp.append(matrix)





for i in range(len(cost)):
    for matrix in dp:
        print(matrix[i])
    print()