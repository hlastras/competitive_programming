def median(array, sub):
  z = [
    [array[sub[0]-1], sub[0], 0], 
    [array[sub[1]-1], sub[1], 1], 
    [array[sub[2]-1], sub[2], 2]
  ]
  z.sort(key=lambda x: x[0])
  return z[1][2]

import random
array = list(range(1,12))
random.shuffle(array)
# array = [2, 1, 8, 4, 5, 6, 7, 3]
# array = [7, 3, 4, 1, 5, 2, 6]
print(array)
n = 7
s = []
c = [1, 2, 3]
m = median(array, c)
s.append(c[(m-1)%3])
s.append(c[m])
s.append(c[(m+1)%3])


for i in range(4, len(array)+1):
  print(">", s)
  s.append(i)
  index = i

  should_end = False
  while True:
    m = median(array, s[index-3:index])
    if m == 0:
      # pasar al principio y deslizas
      s[index-1], s[index-2], s[index-3] = s[index-2], s[index-3], s[index-1]
      index -= 2
      print(index)
    elif m == 1:
      # Colocado, terminar
      break
    else:
      # Mover al centro y terminar
      s[index-1], s[index-2] = s[index-2], s[index-1]
      break

    if index < 3:
      if index == 2:
        should_end = True
      break

  if should_end:
    m = median(array, s[:3])
    if m == 0:
      s[0], s[1] = s[1], s[0]
  print(s)
  j = list(map(lambda x: array[x-1], s))


print(s)
print(list(map(lambda x: array[x-1], s)))
print(median(array, [2,3,4]))
