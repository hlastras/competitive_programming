cases = int(input())
for case in range(1, cases+1):
  l, s = list(map(int, input().split()))

  maximum = sum(range(2, l+1))
  minimum = l-1

  solution = "IMPOSSIBLE"
  if s >= minimum and s <= maximum:
    z = list(range(l, 1, -1))
    pos = 0
    for _ in range(maximum-s):
      if z[pos] == 1:
        pos += 1
      z[pos] -= 1
    
    a = list(range(1, l+1))
    for i in range(l-2, -1, -1):
      a[i:i+z[i]] = a[i:i+z[i]][::-1]

    solution = " ".join(map(str, a))

  print(f'Case #{str(case)}: {str(solution)}')