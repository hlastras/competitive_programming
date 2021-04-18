import sys

class FenwickTree:
  def __init__(self, length):
    self.memory = [0]*(length+1)
    self.bit = [0]*(length+1)

  def update(self, index, value):
    diff = value - self.memory[index]
    self.memory[index] = value
    while index < len(self.memory):
      self.bit[index] += diff
      index += index & -index

  def get_value(self, index):
    return self.memory[index]

  def query(self, l, r):
    return self._query(r) - self._query(l-1)

  def _query(self, index):
    ans = 0
    while index > 0:
      ans += self.bit[index]
      index -= index & -index
    return ans




lines = sys.stdin.read().split("\n")
lcount = 0

n, k = [int(x) for x in lines[lcount].split()]
lcount += 1

tree = FenwickTree(n)


res = []

for _ in range(k):
  z = lines[lcount].split()
  lcount += 1

  if z[0] == "F":
    index = int(z[1])
    if tree.get_value(index) == 0:
      tree.update(index, 1)
    else:
      tree.update(index, 0)
  else:
    a = int(z[1])
    b = int(z[2])

    res.append(str(tree.query(a,b)))
    
print("\n".join(res))

