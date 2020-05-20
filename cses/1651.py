from sys import stdin, stdout  
import math

def build_segment_tree(numbers):
  l = 2**int(math.ceil(math.log(len(numbers),2)))
  st = [0] * l
  st.extend(numbers)
  st.extend([0] * (l - len(numbers)))
  for i in range(l-1, 0, -1):
    st[i] = st[2*i] + st[2*i+1]
  return st

def increase_item(segment_tree, position, value):
  n = len(segment_tree) // 2
  k = position + n
  while k >= 1:
    segment_tree[k] += value
    k //= 2

def sum_range(segment_tree, a, b):
  n = len(segment_tree) // 2
  a += n
  b += n
  s = 0
  while a <= b:
    if a % 2 == 1:
      s += segment_tree[a]
      a += 1
    if b % 2 == 0:
      s += segment_tree[b]
      b -= 1

    a //= 2
    b //= 2
  return s

n, q = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))
for i in range(n-1,0,-1):
  numbers[i] -= numbers[i-1]

st = build_segment_tree(numbers)

for _ in range(q):
  data = list(map(int, stdin.readline().split()))
  if data[0] == 1: # Update
    a = data[1]
    b = data[2]
    inc = data[3]
    increase_item(st, a-1, inc)
    if b < n:
      increase_item(st, b, -inc)
  else: # Query
    s = sum_range(st, 0, data[1]-1)
    stdout.write("%d\n" % (s))
