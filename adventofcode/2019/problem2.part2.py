ns = [int(x) for x in input().split(',')]

result_x = -1
result_y = -1

for x in range(100):
  for y in range(100):
    numbers = ns.copy()
    print(numbers)

    numbers[1] = x
    numbers[2] = y

    reader_pos = 0
    while True:
      if numbers[reader_pos] == 99:
        break
      a = numbers[reader_pos+1]
      b = numbers[reader_pos+2]
      c = numbers[reader_pos+3]

      if numbers[reader_pos] == 1:
        numbers[c] = numbers[a] + numbers[b]
      else:
        numbers[c] = numbers[a] * numbers[b]

      reader_pos +=4

    if numbers[0] == 19690720:
      if result_x == -1:
        result_x = x
        result_y = y
      else:
        print("MAS")

print(100*result_x+result_y)