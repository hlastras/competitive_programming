import math
cases = int(input())

for i in range(cases):
  message = input()

  l = len(message)
  m = math.ceil(math.sqrt(l))

  result = []
  for col in range(m):
    for row in reversed(range(m)):
      if row*m+col < l:
        result.append(message[row*m+col])
        
  print("".join(result))