cases = int(input())
for case in range(1, cases+1):
  cj, jc, string = input().split()
  cj = int(cj)
  jc = int(jc)


  c = 0
  j = 0
  if string[0] == 'C':
    j = 'X'
  elif string[0] == 'J':
    c = 'X'

  for i in range(1, len(string)):
    if string[i] == 'C':
      l = []
      if c != 'X':
        l.append(c)
      if j != 'X':
        l.append(j+jc)
      c = min(l)
      j = 'X'
    elif string[i] == 'J':
      l = []
      if c != 'X':
        l.append(c+cj)
      if j != 'X':
        l.append(j)
      c = 'X'
      j = min(l)
    else:
      l = []
      if c != 'X':
        l.append(c)
      if j != 'X':
        l.append(j+jc)
      temp_c = min(l)

      l = []
      if c != 'X':
        l.append(c+cj)
      if j != 'X':
        l.append(j)
      temp_j = min(l)
      c = temp_c
      j = temp_j


  sol = min(list(filter(lambda x: x != "X", [c, j])))


  print(f'Case #{str(case)}: {str(sol)}')