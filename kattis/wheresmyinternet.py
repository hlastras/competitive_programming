import time
import sys

class UnionFind():
  def __init__(self, n):
    self.parent = []
    for i in range(n):
      self.parent.append(i)

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

  def union(self, x, y):
    self.parent[self.find(x)] = self.find(y)
  


lines = sys.stdin.read().split("\n")
count = 0

n, m = [int(x) for x in lines[count].split()]
count += 1

data = UnionFind(n)
for i in range(m):
  a, b = [int(x) for x in lines[count].split()]
  data.union(a-1, b-1)
  count += 1
output = []
internet = data.find(0)
see = True
for i in range(1,n):
  if data.find(i) != internet:
    output.append(str(i+1))
    see = False
if see:
  print("Connected")
else:
  print("\n".join(output))
