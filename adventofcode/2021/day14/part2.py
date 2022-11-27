import sys
import functools
from collections import defaultdict

lines = sys.stdin.read().split("\n")[:-1]
inp = lines[0]

data = {}
for l in lines[2:]:
    k, v = l.split(' -> ')
    data[k] = v


@functools.cache
def recursive(pair, depth):
    if depth <= 1:
        d = defaultdict(int)
        d[pair[0]] += 1
        d[pair[1]] += 1
        d[data[pair]] += 1
        
        return d

    new_char = data[pair]
    part1 = recursive(pair[0]+new_char, depth-1)
    part2 = recursive(new_char+pair[1], depth-1)

    result = defaultdict(int)
    for k, v in part1.items():
        result[k] = v
    for k, v in part2.items():
        result[k] += v

    result[new_char] -= 1

    return result


result = {}
for idx in range(len(inp)-1):
    pair = inp[idx:idx+2]
    x = recursive(pair, 40)
    
    for k, v in x.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    result[pair[1]] -= 1
result[inp[-1]] += 1


print(max(result.values()) - min(result.values()))