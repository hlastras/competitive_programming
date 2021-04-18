f = open("out.txt", "w")

def my_input():
  r = input()
  global f
  f.write("< ")
  f.write(r)
  f.write("\n")
  if r == "N":
    exit(1)
  return r
def my_print(output):
  global f
  print(output)
  f.write(">>> ")
  f.write(str(output))
  f.write("\n")

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
  global f
  f.write("||| ")
  f.write(str(array))
  f.write("\n")
  a1 = "".join(array)
  a2 = "".join(negate(array))
  array.reverse()
  a3 = "".join(array)
  a4 = "".join(negate(a3))
  f.write("111||| ")
  f.write(str([a1,a2,a3,a4]))
  f.write("\n")

  alternatives = list(set([a1,a2,a3,a4]))
  while len(alternatives) > 1:
    pos = -1
    for i in range(len(alternatives[0])):
      if some_diff(i, alternatives):
        pos = i
        break

    if pos >= 0:
      global request
      request += 1
      my_print(pos+1)
      value = my_input()
      alternatives = list(filter(lambda x: (x[pos] == value), alternatives))
      f.write("222||| ")
      f.write(str(alternatives))
      f.write("\n")
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
    # if request-1 % 10 == 0:
    #   array = determine_alternative(array)
    # else:
    # if request % 2 == 0:
    #   my_print(left+1)
    #   array[left] = my_input()
    #   left += 1
    # else:
    #   my_print(right+1)
    #   array[right] = my_input()
    #   right -= 1

    point = next_point(array)
    my_print(point+1)
    array[point] = my_input()
    request += 1

    f.write("**** ")
    f.write(str('X' not in set(array)))
    f.write("\n")
    if 'X' not in set(array):
      break
    

    if (request) % 10 == 0:
      array = determine_alternative(array)


  f.write("********* ")
  f.write(str(request))
  f.write("\n")
  f.write("".join(array))
  f.write("\n")
  if (request-1) % 10 == 0:
    array = determine_alternative(array)
  # array.reverse
  my_print("".join(array))
  my_input()
  f.write("********* ")
  f.write(str(request))
  f.write("\n")

f.close()