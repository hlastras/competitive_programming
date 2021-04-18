n, k = [int(x) for x in input().split()]

a = 1
b = 1
fib = [1, 1,]
for _ in range(n):
  s = a + b
  a = b
  b = s
  fib.append(b)

n -= 1

while n >= 2:
  if k > fib[n-2]:
    k -= fib[n-2]
    n -= 1
  else:
    n -= 2

if n == 0:
  print("N")
else:
  print("A")
