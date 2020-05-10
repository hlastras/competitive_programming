n, x = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

m = [0] * (x+1)
m[0] = 1

for i in range(x):
  if m[i] > 0:
    for c in coins:
      if i+c <= x:
        m[i+c] += m[i]
        m[i+c] %= 1000000007

print(m[x])