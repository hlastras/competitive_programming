import sys

def binary_search(values, up, down, first_mid):
  for c in values:
    k = int((up + down) / 2)
    if c == first_mid:
      down = k
    else:
      up = k + 1

  return up

lines = sys.stdin.read().strip().split("\n")

seats = []
for line in lines:
  row = binary_search(line[:7], 0, 127, "F")
  col = binary_search(line[7:], 0, 7, "L")
  seat_id = row * 8 + col
  seats.append(seat_id)


seats.sort()
for i in range (1, 960):
  if(seats[i]-seats[i-1] != 1):
    print(seats[i]-1)
    break