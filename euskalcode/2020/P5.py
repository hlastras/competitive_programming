def num_to_coord(num):
  row = num // 3
  col = num % 3
  return row, col

def entryTime(s, keypad):
    time = 0
    current_index = keypad.index(s[0])
    current_coord = num_to_coord(current_index)
    for n in s[1:]:
      new_index = keypad.index(n)
      new_coord = num_to_coord(new_index)

      diff_x = abs(new_coord[0] - current_coord[0])
      diff_y = abs(new_coord[1] - current_coord[1])

      if diff_x == 2 or diff_y == 2:
        time +=2
      elif diff_x == 1 or diff_y == 1:
        time += 1
      
      current_index = new_index
      current_coord = new_coord
    return time

if __name__ == '__main__':
    s = input()

    keypad = input()

    print(entryTime(s, keypad))