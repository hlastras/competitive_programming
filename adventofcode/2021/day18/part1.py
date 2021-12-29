import sys
lines = sys.stdin.read().split("\n")[:-1]

iter_array = []
def build_iter_array(i):
  global iter_array
  if i >= 32:
    iter_array.append(i)
  else:
    build_iter_array(i*2)
    build_iter_array(i*2+1)
    iter_array.append(i)

def parse(x):
  result = [-2] * 64
  parse_aux(x, 1, result)
  return result

def parse_aux(x, index, array):
  left = x[0]
  right = x[1]
  array[index] = -1
  if isinstance(left, int):
    array[index*2] = left
  else:
    parse_aux(left, index*2, array)

  if isinstance(right, int):
    array[index*2+1] = right
  else:
    parse_aux(right, index*2+1, array)

def sum(a, b):
  result = [-2, -1]
  for i in range(5):
    start = 2**i
    for x in range(start, start*2):
      result.append(a[x])
    for x in range(start, start*2):
      result.append(b[x])
  return result

def reduce(x):
  global iter_array
  
  # Search explode
  for i in range(32, 64, 2):
    if x[i] >= 0:
      index_left = iter_array.index(i)
      index_right = iter_array.index(i+1)
      for l in range(index_left-1, -1, -1):
        if x[iter_array[l]] >= 0:
          x[iter_array[l]] += x[i]
          break
      for r in range(index_right+1, 63, 1):
        if x[iter_array[r]] >= 0:
          x[iter_array[r]] += x[i+1]
          break
      x[i] = -2
      x[i+1] = -2
      x[i//2] = 0
      reduce(x)
      return
  
  # Search split
  for i in iter_array:
    if x[i] >= 10:
      x[i*2] = x[i] // 2
      x[i*2+1] = (x[i]+1) // 2
      x[i] = -1
      reduce(x)
      return

def printNumber(x, i):
  if x[i] == -1:
    print("[", end='')
    printNumber(x, i*2)
    print(",", end='')
    printNumber(x, i*2+1)
    print("]", end='')
  else:
    print(x[i], end='')
  if i == 1:
    print()


build_iter_array(1)
total = parse(eval(lines[0]))
for line in lines[1:]:
  total = sum(total, parse(eval(line)))
  reduce(total)

# printNumber(total, 1)

# calculate magnitude break the original tree
for i in iter_array:
  if total[i] == -1:
    total[i] = 3*total[i*2] + 2*total[i*2+1]

print(total[1])