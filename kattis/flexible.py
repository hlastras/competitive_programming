w, p = [int(x) for x in input().split(" ")]
number_list = [int(x) for x in input().split()]
number_list.insert(0, 0)
number_list.append(w)


result = set()

for i in range(1, p+2):
  for j in range(0, len(number_list)-i):
    result.add(number_list[j+i] - number_list[j])

r = list(result)
r.sort()
r = [str(x) for x in r]
print(" ".join(r))
