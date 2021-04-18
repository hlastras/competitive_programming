def calculate(x, y, pos, inc):
  l = []
  if x != 'X':
    if pos == 0:
      l.append(x+inc)
    else:
      l.append(x)
  if y != 'X':
    if pos == 1:
      l.append(y+inc)
    else:
      l.append(y)
  return min(l)


cases = int(input())
for case in range(1, cases+1):
  x = input().split()
  cj_inc = int(x[0])
  jc_inc = int(x[1])
  string = x[2]


  pos_c = 0
  pos_j = 1

  a = [0, 0]
  b = [0, 0]
  if string[0] == 'C':
    a[pos_j] = 'X'
    b[pos_j] = 'X'
  elif string[0] == 'J':
    a[pos_c] = 'X'
    b[pos_c] = 'X'

  for i in range(1, len(string)):
    if string[i] == 'C':
      b[0] = calculate(a[0], a[1], 1, jc_inc)
      b[1] = 'X'
    elif string[i] == 'J':
      b[0] = 'X'
      b[1] = calculate(a[0], a[1], 0, cj_inc)
    else:
      b[0] = calculate(a[0], a[1], 1, jc_inc)
      b[1] = calculate(a[0], a[1], 0, cj_inc)

    a, b = b, a

  solution = min(list(filter(lambda x: x != "X", a)))
  print(f'Case #{str(case)}: {str(solution)}')