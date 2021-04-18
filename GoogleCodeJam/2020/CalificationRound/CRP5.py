from itertools import permutations 

totals = set()

def can_add(l, used):
  for i, val in enumerate(l):
    for us in used:
      if us[i] == val:
        return False
  return True

def ite(used, lista, max):
  global totals
  if len(used) == max:
    total = 0
    for i, p in enumerate(used):
      # print(p)
      total += p[i]
    # print("Total: %d\n" % total)
    len_before = len(totals)
    totals.add(total)
    len_after = len(totals)
    if len_after > len_before:
      print(sorted(list(totals)))
    return

  for l in lista:
    if can_add(l, used):
      used.append(l)
      ite(used, lista, max)
      used.pop()
  
perms = list(permutations(list(range(1, 7))))

ite([], perms, 6)
print(sorted(list(set(totals))))

# 2  [2, 4]
# 3  [3, 5, 6, 7, 9]
# 11 [4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]
# 19 [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25]
# 29 [6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36]