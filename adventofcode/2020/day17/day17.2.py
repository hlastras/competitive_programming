import sys
lines = sys.stdin.read().strip().split("\n")
n = 6 + len(lines) + 6

data = [False for _ in range(n*n*n*n)]
data2 = [False for _ in range(n*n*n*n)]
access = [list() for _ in range(n*n*n*n)]

# Copy input into data
for x, line in enumerate(lines):
  for y, c in enumerate(line):
    if c == "#":
      data[n*n*n*(n//2) + n*n*(n//2) + n*(x+6) + (y+6)] = True


for x in range(n):
  for y in range(n):
    for z in range(n):
      for w in range(n):
        pos = n*n*n*x + n*n*y + n*z + w
    
        for a in range(x-1, x+2):
          for b in range(y-1, y+2):
            for c in range(z-1, z+2):
              for d in range(w-1, w+2):
                if a>=0 and a<n and b>=0 and b<n and c>=0 and c<n and d>=0 and d<n:
                  if not (a==x and b==y and c==z and d==w):
                    access[pos].append(n*n*n*a + n*n*b + n*c +d)


for _ in range(6):

  for i in range(len(data)):
    count = 0
    for pos in access[i]:
      if data[pos]:
        count += 1
    
    if data[i]:
      if count == 2 or count == 3:
        data2[i] = True
      else:
        data2[i] = False
    else:
      if count == 3:
        data2[i] = True
      else:
        data2[i] = False

  data, data2 = data2, data


total = 0
for v in data:
  if v:
    total += 1

print(total)



