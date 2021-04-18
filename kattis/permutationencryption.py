result = []
line = input()
while line != '0':
  permutations = [int(x) for x in line.split(" ")][1:]
  message = input()

  phrase = ["'"]
  l = len(permutations)
  extra_spaces = (l - (len(message) % l)) % l
  message += (" " * extra_spaces)

  offset = 0
  for _ in range(len(message)//l):
    for j in permutations:
      phrase.append(message[offset+j-1])
    offset += l
  phrase.append("'")
  result.append("".join(phrase))

  line = input()

print("\n".join(result))