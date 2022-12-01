# open the input file and read the lines into a list
with open('input.txt') as f:
  lines = f.readlines()

# remove whitespace characters like `\n` at the end of each line
lines = [line.strip() for line in lines]

# initialize the dictionary that will hold the food counts for each Elf
elves = {}

# initialize the current Elf to None (we haven't seen any Elves yet)
current_elf = None

# iterate over the lines in the input
for line in lines:
  # if the line is empty, that means we have reached the end of an Elf's inventory
  # and we need to move on to the next Elf
  if line == '':
    current_elf = None
    continue
  
  # if the current Elf is None, that means we have reached the beginning of a new Elf's inventory
  # so we need to create a new entry in the dictionary for that Elf
  if current_elf is None:
    current_elf = len(elves)
    elves[current_elf] = 0
  
  # add the number of Calories in the current food item to the current Elf's inventory
  elves[current_elf] += int(line)

# sort the Elves by the number of Calories in their inventory
elves = sorted(elves.items(), key=lambda x: x[1], reverse=True)

# calculate the total Calories carried by the top three Elves
total_calories = sum([x[1] for x in elves[:3]])

# print the result
print(f"The top three Elves are carrying a total of {total_calories} Calories.")