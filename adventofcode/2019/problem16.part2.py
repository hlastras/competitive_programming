import math
numbers = [int(x) for x in input()]
numbers *= 10000
print(len(numbers))


bp = [0, 1, 0, -1]
def build_pat(i, l):
  p = []
  pos = 0
  while len(p) < l:
    for _ in range(i):
      p.append(bp[pos])
    pos += 1
    pos %= 4
  return p[1:]

paterns = []

for i in range(1, len(numbers)+1):
  patern = build_pat(i, len(numbers)+1)
  paterns.append(patern)
  print(patern)

print(paterns[-1])
exit()
  
for i in range(1, 101):
  for i, n in enumerate(numbers):
    p = paterns[i]
    print(p)
    total = 0
    for j, n in enumerate(numbers):
      total += (n*p[j])
    numbers[i] = abs(total) % 10

offset = []
for x in numbers[:2]:
  offset.append(str(x))
offset = int("".join(offset))
print(numbers[offset:offset+8])


