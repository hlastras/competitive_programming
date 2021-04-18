def print_layer(im):
  for line in im:
    nl = []
    for c in line:
      if c == "0":
        nl.append(" ")
      elif c=="1":
        nl.append("▓")
      else:
        nl.append(" ")
    print("".join(nl))
  
  print("\n")

def print_layer2(im):
  count = 0
  for _ in range(6):
    line = []
    for _ in range(25):
      line.append(im[count])
      count += 1
    print("".join(line))
  
  print("\n")


image = input()

# for x in range(11, len(image), 25*6):
#   print(image[x])
# exit(0)

layer_number = 0
init_layer = 0
all_layer = {}
for end_layer in range(25*6, len(image)+1, 25*6):
  layer = image[init_layer:end_layer]
  matrix_layer = []
  count = 0
  for x in range(6):
    line = []
    for y in range(25):
      line.append(layer[count])
      count += 1
    matrix_layer.append(line)

  all_layer[layer_number] = matrix_layer
  layer_number += 1
  init_layer = end_layer





image = all_layer[0]
print_layer(image)

for layer in range(0, len(all_layer)):
  image_layer = all_layer[layer]

  for x in range(6):
    for y in range(25):
      if(image[x][y] == "2"):
        image[x][y] = image_layer[x][y]

print_layer(image)

