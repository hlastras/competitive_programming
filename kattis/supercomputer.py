import sys
import math

class SegmentTreeNode:

  def __init__(self, _from, _to):
    self.left = None
    self.right = None
    self._from = _from
    self._to = _to
    self.value = 0
class SegmentTree:

  def __init__(self, arr):
    self.tree = self.build(arr, 0, len(arr)-1)

  def build(self, arr, l, r):
    if l > r:
      return None
    
    root = SegmentTreeNode(l, r)
    if l == r:
      root.value = arr[l]
    else:
      m = (l + r) // 2
      root.left = self.build(arr, l, m)
      root.right = self.build(arr, m+1, r)
      if root.left:
        root.value += root.left.value
      if root.right:
        root.value += root.right.value
    
    return root

  def query(self, l, r):
    return self._query(self.tree, l, r)

  def _query(self, tree, l, r):
    if tree == None:
      return 0

    if l <= tree._from and tree._to <= r:
      return tree.value
    if tree._to < l:
      return 0
    if r < tree._from:
      return 0

    return self._query(tree.left, l, r) + self._query(tree.right, l, r)

  def update(self, i, val):
    return self._update(self.tree, i, val)

  def _update(self, tree, i , val):
    if tree == None:
      return 0
    if tree._to < i:
      return tree.value
    if i < tree._from:
      return tree.value
    if tree._from == tree._to and tree._from == i:
      tree.value = val
    else:
      tree.value = self._update(tree.left, i, val) + self._update(tree.right, i, val)

    return tree.value


lines = sys.stdin.read().split("\n")
lcount = 0

n, k = [int(x) for x in lines[lcount].split()]
lcount += 1

st = SegmentTree([0]*n)
memory = [0]*n

res = []

for _ in range(k):
  z = lines[lcount].split()
  lcount += 1

  if z[0] == "F":
    position = int(z[1])-1
    if memory[position] == 0:
      st.update(position, 1)
      memory[position] = 1
    else:
      st.update(position, 0)
      memory[position] = 0
  else:
    a = int(z[1])-1
    b = int(z[2])-1

    res.append(str(st.query(a,b)))
  
print("\n".join(res))