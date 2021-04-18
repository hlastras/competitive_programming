from sys import stdin, stdout 
from collections import defaultdict
from heapq import heappush, heappop

N, T = map(int, stdin.readline().split()) 

s = defaultdict(list)
for _ in range(N):
  money, deadline = map(int, stdin.readline().split()) 
  s[deadline].append(money)

amounts_to_consider = []
sum_total = 0

for t in range(T)[::-1]:
  for price in s[t]:
    heappush(amounts_to_consider, -price)
    
  if amounts_to_consider:
    sum_total += heappop(amounts_to_consider)

stdout.write(str(-sum_total)+'\n')