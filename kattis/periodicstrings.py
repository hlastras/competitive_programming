def rotate(s):
  return s[-1] + s[:-1]

s = input()
solved = False
for i in range(1, len(s)):
  p = 0
  well = True
  while p < len(s)-i:
    if rotate(s[p:p+i]) != s[p+i:p+i+i]:
      well = False
      break
    p += i

  if well:
    solved = True
    print(str(i))
    break

if not solved:
  print(len(s))