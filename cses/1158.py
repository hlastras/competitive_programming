n, x = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]
pages = [int(x) for x in input().split()]

books = list(zip(prices, pages))

a = [0] * (x+1)
b = [0] * (x+1)

for book in books:
  for i in range(x+1):
    if i < book[0]:
      b[i] = a[i]
    else:
      b[i] = max(a[i], a[i-book[0]]+book[1])

  a, b = b, a

print(a[x])