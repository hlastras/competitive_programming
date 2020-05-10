input()
numbers = [int(x) for x in input().split()]

actual = numbers[0]
total = 0
for n in numbers:
  if n < actual:
    total += (actual-n)
  else:
    actual = n

print(total)
    