

dp = []
row = []
for i in range(25):
    row.append([i,1])
dp.append(row)



for i in range(2,50):
    row = [dp[-1][0]]
    for x in range(1,len(dp[-1])):
        values = dp[-1][x-1]
        # if values[0] >= 4 and values[1] == i-1:
        if values[0] >= 4:
            option1 = [values[0] - 4 + values[1], values[1] + 1]
            option2 = row[-1].copy()
            option2[0] += option2[1]

            if option1[1] > option2[1]:
                row.append(option1)
            elif option2[0] > option1[0]:
                row.append(option2)
            else:
                row.append(option1)
        else:
            values = dp[-1][x]
            row.append([values[0], values[1]])

    dp.append(row)

for r in dp:
    print(r)