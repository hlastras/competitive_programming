init = 172930
end = 683082

def adyacent(x):
  line = str(x)
  before = 'a'
  count=0
  for c in line:
    if c != before:
      if count == 2:
        return True
      else:
        count = 0
        before = c
    count+=1
  return count == 2

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