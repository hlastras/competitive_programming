init = 172930
end = 683082

def adyacent(x):
  line = str(x)
  count = 0
  for pos in range(5):
    if line[pos] == line[pos+1]:
      count += 1

  return count>0

def never_decrease(x):
  line = str(x)
  for pos in range(5):
    if line[pos] > line[pos+1]:
      return False
  return True

passwords = set()
for x in range(init, end):
  if adyacent(x):
    if never_decrease(x):
      passwords.add(x)

print(len(passwords))