sequence = input()
sequence += " "
actual = ""
actualL = 1
best = 1
for c in sequence:
  if c == actual:
    actualL += 1
    best = max(best, actualL)
  else:
    actual = c
    actualL = 1
print(best)