from sys import stdin, stdout 

n = int(stdin.readline())

numbers = []

while len(numbers) < n**2:
  num = list(map(int, stdin.readline().split()))
  numbers.extend(num)

matrix = []
for i in range(0, n**2, n):
  matrix.append(numbers[i:i+n])

for r in range(n):
  for c in range(n):
    if c > 0:
      matrix[r][c] += matrix[r][c-1]

curr = (100*100*(-127))-10
for l in range(n):
  for r in range(l, n):
    poss = 0
    for row in range(n):
      if l > 0:
        poss += matrix[row][r] - matrix[row][l-1]
      else:
        poss += matrix[row][r]

      if poss < 0:
        poss = 0

      if poss > curr:
        curr = poss
stdout.write("%d\n" % curr)

