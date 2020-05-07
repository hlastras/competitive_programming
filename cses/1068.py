n = int(input())
result = [n]
while n > 1:
  if n&1:
    n = (n*3)+1
  else:
    n = n >> 1
  result.append(n)

print(" ".join(str(x) for x in result))