from functools import cmp_to_key

def roman_to_int(roman):
  values = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
  total = 0
  for i in range(len(roman)):
    if i > 0 and values[roman[i]] > values[roman[i - 1]]:
      total += values[roman[i]] - 2 * values[roman[i - 1]]
    else:
      total += values[roman[i]]
  return total

def sortFunc(a, b):
  a = a.split()
  b = b.split()
  if a[0] < b[0]:
    return -1
  elif a[0] > b[0]:
    return 1
  else:
    # compare numbers
    return roman_to_int(a[1]) - roman_to_int(b[1])

def sortRoman(names):
    return sorted(names, key=cmp_to_key(sortFunc))

if __name__ == '__main__':
    names_count = int(input().strip())

    names = []

    for _ in range(names_count):
        names_item = input()
        names.append(names_item)

    print(sortRoman(names))

