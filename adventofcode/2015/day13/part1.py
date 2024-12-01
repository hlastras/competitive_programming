from collections import defaultdict
import sys
lines = sys.stdin.read().split("\n")

data = defaultdict(dict)
for line in lines:
    l = line[:-1].split()
    a = l[0]
    act = l[2]
    value = int(l[3])
    b = l[10]
    if act == "lose":
        value = -value

    data[a][b]= value

names = list(data.keys())
seen = [0] * len(names)
pairs = []
for i in range(len(names)):
    for j in range(i+1,len(names)):
        v1 = data[names[i]][names[j]]
        v2 = data[names[j]][names[i]]
        pairs.append((v1+v2, i, j))
        
pairs.sort(key= lambda x: x[0], reverse=True)

result = 0
total = 0
target = len(names) * 2
while total < target and len(pairs) > 0:
    v, i, j = pairs[0]
    pairs = pairs[1:]
    
    if seen[i] < 2 and seen[j] < 2:
        seen[i] += 1
        seen[j] += 1
        total += 2
        result += v

print(result)