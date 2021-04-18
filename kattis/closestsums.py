import sys
lines = sys.stdin.read().split("\n")[:-1]
lines.reverse()

count = 1
while len(lines) > 0:
  len_numbers = int(lines.pop())
  numbers = []
  for _ in range(len_numbers):
    numbers.append(int(lines.pop()))

  len_querys = int(lines.pop())
  querys = []
  for _ in range(len_querys):
    querys.append(int(lines.pop()))

  print("Case " + str(count) + ":")
  for x in querys:
    distance = 10000000000
    best = -1
    for i, v1 in enumerate(numbers):
      for j, v2 in enumerate(numbers):
        if i != j:
          tot = v1 + v2
          if distance > (abs(tot-x)):
            distance = abs(tot-x)
            best = tot

    print("Closest sum to " + str(x) +" is " + str(best) + ".")

  count += 1