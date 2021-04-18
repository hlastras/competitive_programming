import sys
lines = sys.stdin.read().split("\n")
lines.reverse()

result = []

def hash_file(file):
  file_bites = bytes(file, encoding='utf8')
  hash = file_bites[0]
  for c in file_bites[1:]:
    hash ^=  c
  return hash

number_files = int(lines.pop())
while number_files > 0:

  hashes = {}
  unique_files = 0
  hash_collisions = 0

  for _ in range(number_files):
    file = lines.pop()
    
    hash = hash_file(file)

    if hash not in hashes:
      hashes[hash] = [{}, 0]

    registry = hashes[hash]
    if file not in registry[0]:
      registry[0][file] = 0
      unique_files += 1
    
    hash_collisions += registry[1] - registry[0][file]
    registry[0][file] += 1
    registry[1] += 1


  result.append("%d %d\n" %  (unique_files, hash_collisions) )

  number_files = int(lines.pop())

print("".join(result))