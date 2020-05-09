from collections import defaultdict

def subsetsSums(elements, acc, mem, target):
  if acc > target:
    return mem
  if len(elements) == 0:
    mem[acc] += 1
    return mem
  subsetsSums(elements[1:], acc, mem, target)
  subsetsSums(elements[1:], acc+elements[0], mem, target)
  return mem
  
n, x = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
sets1 = subsetsSums(numbers[:n//2], 0, defaultdict(int), x)
sets2 = subsetsSums(numbers[n//2:], 0, defaultdict(int), x)

result = 0
for k, v in sets1.items():
  if (x-k) in sets2:
    result += sets2[(x-k)] * v

print(result)
