# gf2_matrix_square() gf2_matrix_times() and crc32_combine() are implementations
# in python of crc32_combine() from zlib not aviable in python zlib 
# I copied the code from there:
# https://github.com/toomuchio/pycrc32combine/blob/master/crc32_combine.py
#
# Another assumption of the problem is that all files given only have 0x00 as content
# So for calculate crc32 hashes we don need read the file, we only need the size (in bytes)
# And with this we can calculate file hash in O(nlog n)
# If this assumption is not true, we need change calculate_hash() by calculate_hash_reading_file()

import tarfile
import zlib
from sys import stdin

mem = {}

def main():
  tar = tarfile.open("15-animals.tar.gz", "r:gz")
  lines = stdin.read().split("\n")[:-1]
  lines.reverse()

  while len(lines) > 0:
    path, n = lines.pop().split()
    n = int(n)
    fileSize = tar.getmember("animals/./"+path).size

    cuts = []
    aditions = []
    for _ in range(n):
      index, value = [int(x) for x in lines.pop().split()]
      cuts.append(index-len(list(filter(lambda x: x < index, cuts))))
      aditions.append((index, value))
    cuts = sorted(set(cuts))
    
    hashes = []
    actualIndex = 0
    for cutIndex in cuts:
      if cutIndex > actualIndex:
        hash, lengthRead = calculate_hash(cutIndex-actualIndex)
        if lengthRead > 0:
          hashes.append([hash, lengthRead])
      actualIndex = cutIndex
    hash, lengthRead = calculate_hash(fileSize-actualIndex)
    if lengthRead > 0:
      hashes.append([hash, lengthRead])

    # Print CRC32 of the original file without any addition
    result = 0x00000000
    for hash, length in hashes:
      result = crc32_combine(result, hash, length)
    print("%s %d: %08x" % (path, 0, result))
    
    count = 1
    for index, value in aditions:
      # Insert addition in the hashes in the correct position
      newHashes = []
      pos = 0
      for hash, length in hashes:
        if pos == index:
          byteHash = calculate_byte_hash(value)
          newHashes.append([byteHash, 1])
        newHashes.append([hash, length])
        pos += length
      if pos == index:
          byteHash = calculate_byte_hash(value)
          newHashes.append([byteHash, 1])
      hashes = newHashes

      # Calculate entire file hash
      result = 0x00000000
      for hash, length in hashes:
        result = crc32_combine(result, hash, length)
      print("%s %d: %08x" % (path, count, result))

      count += 1

def gf2_matrix_square(square, mat):
  for n in range(0, 32):
    if (len(square) < (n + 1)):
      square.append(gf2_matrix_times(mat, mat[n]))
    else:
      square[n] = gf2_matrix_times(mat, mat[n])
  return square

def gf2_matrix_times(mat, vec):
  sum = 0
  i = 0
  while vec:
    if (vec & 1):
      sum = sum ^ mat[i]
    vec = (vec >> 1) & 0x7FFFFFFF
    i = i + 1
  return sum

def crc32_combine(crc1, crc2, len2):
  even = []
  odd = []
  if (len2 == 0):
    return crc1

  odd.append(0xEDB88320)
  row = 1

  for n in range(1, 32):
    odd.append(row)
    row = row << 1

  even = gf2_matrix_square(even, odd)
  odd = gf2_matrix_square(odd, even)

  while (len2 != 0):
    even = gf2_matrix_square(even, odd)
    if (len2 & 1):
      crc1 = gf2_matrix_times(even, crc1)
    len2 = len2 >> 1
  
    if (len2 == 0):
      break
  
    odd = gf2_matrix_square(odd, even)
    if (len2 & 1):
      crc1 = gf2_matrix_times(odd, crc1)
    len2 = len2 >> 1
  
  crc1 = crc1 ^ crc2
  return crc1

def calculate_byte_hash(byte):
  return zlib.crc32(bytes([byte]), 0) & 0xFFFFFFFF

def calculate_hash(length):
  if length <= 0:
    return 0, 0

  global mem
  hash = 0x00000000
  l = 0
  while l < length:
    maximum = length - l
    for v in reversed(list(mem.keys())):
      if v < maximum:
        maximum = v
        break
    hash = crc32_combine(hash, mem[maximum], maximum)
    l += maximum
    mem[l] = hash
  return mem[length], length


if __name__ == '__main__':
  hash = calculate_byte_hash(0x00)
  mem[1] = hash
  main()

# def calculate_hash_reading_file(file, length):
#   read = 0
#   hash = 0
#   while read < length or length < 0:
#       chunk = 0
#       if read + 1024 <= length:
#         chunk = 1024
#       elif length > 0:
#         chunk = length-read
#       else:
#         chunk = 1024
#       s = file.read(chunk)
#       read += len(s)
#       if not s:
#           break
#       hash = zlib.crc32(s, hash)
#   return hash & 0xFFFFFFFF, read