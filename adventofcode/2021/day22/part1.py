import sys
lines = sys.stdin.read().split("\n")[:-1]

def parse(line):
   action, coord_raw =  line.split()
   coord_x_raw, coord_y_raw, coord_z_raw = coord_raw.split(",")
   x_from, x_to = coord_x_raw[2:].split("..")
   y_from, y_to = coord_y_raw[2:].split("..")
   z_from, z_to = coord_z_raw[2:].split("..")

   return action, [int(x_from), int(x_to)], [int(y_from), int(y_to)], [int(z_from), int(z_to)]


turned_on = set()

for line in lines:
    action, x_range, y_range, z_range = parse(line)

    if max(x_range) > 50 or min(x_range) < -50 or max(y_range) > 50 or min(y_range) < -50 or max(z_range) > 50 or min(z_range) < -50:
        print(x_range, y_range, z_range)
        continue

    for x in range(x_range[0]+50, x_range[1]+51):
        for y in range(y_range[0]+50, y_range[1]+51):
            for z in range(z_range[0]+50, z_range[1]+51):
                cube_idx =  x*(101**2) + y*101 + z
                if action == 'on':
                    turned_on.add(cube_idx)
                else:
                    turned_on.discard(cube_idx)

print(len(turned_on))