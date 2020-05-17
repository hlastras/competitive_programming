import bisect
from sys import stdin
n = int(stdin.readline())

t = []
for _ in range(n):
  a, b, v = [int(x) for x in stdin.readline().split()]
  t.append((a,b,v))
t.sort(key=lambda x: x[1])

a = list(map(lambda x: x[0], t))
b = list(map(lambda x: x[1], t))
v = list(map(lambda x: x[2], t))

best = [0] * n
best[0] = v[0]

for i in range(1,n):
  pos = bisect.bisect_right(b, a[i]-1)
  if pos > 0:
    val = best[pos-1] + v[i]
  else:
    val = v[i]
  best[i] = max(val, best[i-1])

print(best[-1])