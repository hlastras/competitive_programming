
row = [
    [0,1],
    [1,1],
    [2,1],
    [3,1],
    [4,1],
    [5,1],
    [6,1],
    [7,1],
    [8,1],
    [9,1],
    [11,2],
    [13,2],
    [15,2],
    [17,2],
    [19,2],
    ]


def calculate(row, idx, idx_stop, maximum):
    if row[idx][0] < 4:
        return row[idx]

    current = row[idx][0]
    m = row[idx][1]
    for i in range(idx, idx_stop):
        added = 0
        if current >= 4 and m < maximum:
            added = (current // 4)
            current -= (current // 4) * 4
        current += m
        m += added

    return [current, m]

print(calculate(row, 4, 13, 3))