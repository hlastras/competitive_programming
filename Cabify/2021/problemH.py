c = int(input())
plates = []
for _ in range(c):
  plates.append(int(input()))

results = set()
while True:
  found = False
  for value in range(2, max(plates)):
    all_eq = True
    target = plates[0]%value
    for plate in plates:
      if plate%value != target:
        all_eq = False
        break
    
    if all_eq:
      found = True

      for v in results.copy():
        results.add(v*value)
      results.add(value)

      plates = list(map(lambda x: int(x/value), plates))

      break

  if not found:
    break

print(" ".join([str(x) for x in results]))