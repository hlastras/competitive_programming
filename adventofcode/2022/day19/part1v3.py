
def generate_options(row, x):
    result = [row[x].copy()]
    for i in range(x-1, 0, -1):
        if row[i][0] >= 4:
            inc = (x-i-1) * (row[i][0] // 4 + row[i][1]) + row[i][1] 
            item = [row[i][0] + inc, row[i][1] + 1]
            print(item, inc, (x-i-1), (row[i][0] // 4 + row[i][1]), (row[i][0] // 4) * 4,  row[i][1], row[i][0])
            result.append(item)
    return result


dp = []
row = []
for i in range(25):
    row.append([i,1])
dp.append(row)



for i in range(2,4):
    row = [dp[-1][0]]
    for x in range(1,len(dp[-1])):
        values = dp[-1][x-1]
        # if values[0] >= 4 and values[1] == i-1:
        if values[0] >= 4:
            options = generate_options(dp[-1], x)
            # option1 = [values[0] - 4 + values[1], values[1] + 1]
            # option2 = row[-1].copy()
            # option2[0] += option2[1]
            # options = [option1, option2]

            best = options[0]
            for op in options:
                if op[0] > best[0]:
                    best = op
                if op[0] == best[0] and op[1] < best[1]:
                     best = op

            print(options)
            print(best)
            row.append(best)
        else:
            values = dp[-1][x]
            row.append([values[0], values[1]])

    dp.append(row)

for r in dp:
    print(r)