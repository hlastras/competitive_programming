image = input()

layer_number = 0
init_layer = 0
all_layer = {}
for end_layer in range(25*6, len(image), 25*6):
  layer = image[init_layer:end_layer]
  info_layer = {}
  for pixel in layer:
    if pixel not in info_layer:
      info_layer[pixel] = 0
    info_layer[pixel] += 1

  all_layer[layer_number] = info_layer

  init_layer = end_layer
  layer_number += 1

min = len(image)+1
min_key = -1
for key in all_layer.keys():
  image_info = all_layer[key]
  if "0" in image_info and image_info["0"] < min:
    min =  image_info["0"]
    min_key = key

print(all_layer[min_key]["1"]*all_layer[min_key]["2"])