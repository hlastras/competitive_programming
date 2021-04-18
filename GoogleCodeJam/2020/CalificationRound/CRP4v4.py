
def my_input():
  r = input()
  if r == "N":
    exit(1)
  return r
def my_print(output):
  print(output)

def next_point(array):
  for i in range(len(array)):
    if array[i] == "X":
      return i
    elif array[len(array)-1-i] == "X":
      return len(array)-1-i
  return -1

def negate(array):
  new_array = []
  for x in array:
    if x == "0":
      new_array.append("1")
    elif x == "1":
      new_array.append("0")
    else:
      new_array.append(x)
  return new_array

def some_diff(i, alternatives):
  r = set()
  for alt in alternatives:
    r.add(alt[i])
  return len(r)>1

def determine_alternative(array):
  a1 = "".join(array)
  a2 = "".join(negate(array))
  array.reverse()
  a3 = "".join(array)
  a4 = "".join(negate(a3))

  alternatives = list(set([a1,a2,a3,a4]))
  lastpos = -1
  while len(alternatives) > 1:
    pos = -1
    for i in range(lastpos+1, len(alternatives[0])):
      if some_diff(i, alternatives):
        pos = i
        break

    if pos >= 0:
      global request
      request += 1
      my_print(pos+1)
      value = my_input()
      lastpos = pos
      alternatives = list(filter(lambda x: (x[pos] == value or x[pos] == "X"), alternatives))
    else:
      break

  return list(alternatives[0])



T, N = [int(x) for x in my_input().split()]

for _ in range(T):
  my_print(1)
  my_input()
  request = 1

  array = ["X"] * N
  left = 0
  right = N - 1

  while request < 150:

    point = next_point(array)
    my_print(point+1)
    array[point] = my_input()
    request += 1

    if 'X' not in set(array):
      break
    

    if (request) % 10 == 0:
      array = determine_alternative(array)


  if (request-1) % 10 == 0:
    array = determine_alternative(array)
  
  my_print("".join(array))
  my_input()
