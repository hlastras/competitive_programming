T = int(input())

for case in range(1, T+1):
  N = int(input())
  patterns = []
  for _ in range(N):
    patterns.append(input().split("*"))

  result = "*"
  can_match = True

  prefixes = []
  sufixes = []
  infixes = []
  for pattern in patterns:
    if pattern[0] != '':
      prefixes.append(pattern[0])
    if pattern[-1] != '':
      sufixes.append(pattern[-1])
    for infix in pattern[1:-1]:
      if infix != "":
        infixes.append(infix)

  prefixes.sort(key=len, reverse=True)
  prefix = "" if len(prefixes) == 0 else prefixes[0]
  if len(prefixes) > 1:
    for x in prefixes[1:]:
      if not prefix.startswith(x):
        can_match = False
        break

  sufixes.sort(key=len, reverse=True)
  sufix = "" if len(sufixes) == 0 else sufixes[0]
  if len(sufixes) > 1:
    for x in sufixes[1:]:
      if not sufix.endswith(x):
        can_match = False
        break

  if can_match:
    result = prefix + "".join(infixes) + sufix

  print("Case #%d: %s" % (case, result))