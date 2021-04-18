numbers = [int(x) for x in input().split(',')]
numbers[1] = 12
numbers[2] = 2

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


print(numbers[0])