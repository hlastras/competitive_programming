n = int(input())
mem = [0] * (n+1)
mem[0] = 1
mem[1] = 1

for i in range(2, n+1):
  for d in range(1,7):
    if i-d >=0:
      mem[i] += mem[i-d]
  mem[i] %= 1000000007

print(mem[n])
