from sys import stdin, stdout 

import math

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
querys = list(map(int, stdin.readline().split()))

# build segment tree
l = 2**int(math.ceil(math.log(len(numbers),2)))
st = [0] * l + [1]*len(numbers) + ([0] * (l - len(numbers)))
for i in range(l-1, 0, -1):
  st[i] = st[2*i] + st[2*i+1]

res = []
for q in querys:
  pos = 1
  while pos < l:
    pos *= 2
    if q > st[pos]:
      q -= st[pos]
      pos += 1

  res.append(numbers[pos-l])
  st[pos] = 0
  pos //= 2
  while pos >= 1:
    st[pos] = st[2*pos] + st[2*pos+1]
    pos //= 2

print(" ".join(str(x) for x in res))