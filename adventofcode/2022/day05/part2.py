import sys
lines = sys.stdin.read().split("\n")

i = 0
data = [[] for _ in range(len(lines[0])//4+1)] 
while True:
    if lines[i][1] == "1":
        lines = lines[i+2:]
        break

    for j in range(1, len(lines[i]), 4):
        if lines[i][j] != " ":
            data[j//4].append(lines[i][j])
    i += 1

for col in data:
    col.reverse()

for line in lines:
    values = line.split()
    amount = int(values[1])
    f = int(values[3])-1
    t = int(values[5])-1

    x = data[f][-amount:]
    data[t].extend(x)
    data[f] = data[f][:-amount]

result = []
for col in data:
    result.append(col[-1])

print(''.join(result))