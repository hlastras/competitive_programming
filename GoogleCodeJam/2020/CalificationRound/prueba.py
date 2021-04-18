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

def determine_alternative(array):
  a1 = "".join(array)
  a2 = "".join(negate(array))
  array.reverse()
  a3 = "".join(array)
  a4 = "".join(negate(a3))

  alternatives = list(set([a1,a2,a3,a4]))

  print(a1,a2,a3,a4)
  print(alternatives)


a = ["0", "1", "1", "0", "0", "X", "X", "1", "1", "0", "1", "1"]
determine_alternative(a)
