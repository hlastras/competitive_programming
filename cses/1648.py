from sys import stdin, stdout  
import math
n, q = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))

# Generate Segment tree fill end of array to get a power of 2
rq = [0] * (n)
rq.extend(numbers)
rq.extend([0] * (2**int(math.ceil(math.log(n,2))) - n))
for i in range(n-1, 0, -1):
  rq[i] = rq[2*i] + rq[2*i+1]

for _ in range(q):
  o, a, b = map(int, stdin.readline().split())
  if o == 1: # Update
    k = a+n-1
    diff = b - rq[k]
    while k >= 1:
      rq[k] += diff
      k //= 2
  else: # Query
    a += n-1
    b += n-1
    s = 0
    while a <= b:
      if a%2 == 1:
        s += rq[a]
        a += 1
      if b%2 == 0:
        s += rq[b]
        b -= 1
      a //= 2
      b //= 2
    stdout.write("%d\n" % (s))