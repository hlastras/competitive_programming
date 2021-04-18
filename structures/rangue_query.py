import math

class RangueQuery:
  def __init__(self, length, initual_value):
    self.memory = [initual_value]*length
    self.bucket_size = math.ceil(math.sqrt(length))
    self.buckets_length = math.ceil( length/ self.bucket_size)
    self.buckets = [initual_value * self.bucket_size] * buckets_length


  def update(self, pos, new_value):
    increment = new_value - self.memory[pos]
    self.memory[pos] = new_value
    bucket_p = pos // self.bucket_size
    self.buckets[bucket_p] += increment

  def get_position(self, pos):
    return self.memory[pos]

  def query(self, init, end):
    total = 0
    next_bucket = math.ceil(init/self.bucket_size)*self.bucket_size
    pos = init
    while pos < next_bucket and pos <= end:
      total += self.memory[pos]
      pos += 1

    while pos+self.bucket_size < end:
      total += self.buckets[pos// self.bucket_size]
      pos += self.bucket_size

    while pos <= b:
      total += memory[pos]
      pos += 1

    return  total

