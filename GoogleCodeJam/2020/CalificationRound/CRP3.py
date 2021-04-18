T = int(input())

for case in range(T):
  N = int(input())

  tasks = []
  for i in range(N):
    task = [int(x) for x in input().split()]
    task.append(i)
    tasks.append(task)

  tasks.sort()

  a_free = 0
  b_free = 0
  impossible = False
  results = [''] * N
  for task in tasks:
    if a_free <= task[0]:
      a_free = task[1]
      results[task[2]] = "C"
    elif b_free <= task[0]:
      b_free = task[1]
      results[task[2]] = "J"
    else:
      impossible = True
      break

  result = "IMPOSSIBLE" if impossible else "".join(results)
    
  print("Case #%d: %s" % (case+1, result))