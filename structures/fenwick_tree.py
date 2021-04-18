class FenwickTree:
  def __init__(self, length):
    self.memory = [0]*(length+1)
    self.bit = [0]*(length+1)

  def update(self, index, value):
    diff = value - self.memory
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