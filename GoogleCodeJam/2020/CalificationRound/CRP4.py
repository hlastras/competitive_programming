def mi_input(f):
  r = input()
  f.write("< ")
  f.write(r)
  f.write("\n")
  return r
def mi_print(f, algo):
  print(algo)
  f.write(">>> ")
  f.write(str(algo))
  f.write("\n")

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

def rearange(array, a1, a2, b1, b2, flag_a, flag_b):
  oa1 = array[int(flag_a)-1]
  oa2 = array[-int(flag_a)-1]
  ob1 = array[int(flag_b)-1]
  ob2 = array[-int(flag_b)-1]

  if oa1 == a1 and oa2 == a2 and ob1 == b1 and ob2 == b2:
    # do nothing
    return array
  elif oa1 != a1 and oa2 != a2 and ob1 != b1 and ob2 != b2:
    # negate
    return negate(array)
  elif oa1 != a1 and oa2 != a2 and ob1 == b1 and ob2 == b2:
    # reverse
    array.reverse()
    return array
  else:
    # reverse and inverse
    n_array = negate(array)
    n_array.reverse
    return n_array

f = open("demofile2.txt", "w")

T, N = [int(x) for x in mi_input(f).split()]

mi_print(f, 1)
mi_input(f)

flag_a = -1
flag_b = -1
#Find flag
left = 1
rigth = N
request = 0

while (flag_a == -1 or flag_b == -1) and request < 150:
  mi_print(f, left)
  a = mi_input(f)
  mi_print(f, rigth)
  b = mi_input(f)
  
  if flag_a == -1:
    if a != b:
      flag_a = left
  else:
    if a == b:
      flag_b = left
  left += 1
  rigth -= 1
  request += 1
  if request % 10 == 0:
    mi_print(f, 1)
    mi_input(f)
    request += 1







f.write(str(flag_a))
f.write("\n")
f.write(str(flag_b))
f.write("\n")

array = ["E"] * N

left = 1
rigth = N

determine = False
while left < rigth:
  f.write("Requ")
  f.write(str(request))
  f.write("\n")
  if not determine:
    position = -1
    if request%2 == 0:
      position = left
      left += 1
    else:
      position = rigth
      rigth -= 1

    mi_print(f, position)
    array[position-1] = mi_input(f)
    request += 1
    
    if request%10 == 0:
      determine = True
  else:
    mi_print(f, int(flag_a))
    a1 = mi_input(f)
    mi_print(f, N - int(flag_a) + 1)
    a2 = mi_input(f)
    mi_print(f, int(flag_a))
    b1 = mi_input(f)
    mi_print(f, N - int(flag_b) + 1)
    b2 = mi_input(f)

    array = rearange(array, a1, a2, b1, b2, flag_a, flag_b)
    determine = False
    request += 4
    
result = "".join(array)

# mi_print(f, "10110100101")
f.write(result)
# f.write("\n")
f.close()