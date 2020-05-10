n, x = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

m = [0] * (x+1)
m[0] = 1

for c in coins:
  for i in range(c, x+1):
    m[i] += m[i-c]
    m[i] %= 1000000007

print(m[x])