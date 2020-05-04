# I use gcd of gmpy2 because it is extremely faster than my own implementation
from gmpy2 import gcd
e = 65537 # Most used exponent

# Return the file as a string of 0's and 1's
def read_string_of_bits(path):
  file = open(path,"rb")
  content_in_bytes = file.read()
  content_as_integer = int.from_bytes(content_in_bytes, byteorder='big')
  s = "{0:b}".format(content_as_integer)
  file.close()
  return s

text_1 = read_string_of_bits("12-testdata/plaintexts/test1.txt")
text_2 = read_string_of_bits("12-testdata/plaintexts/test2.txt")
ciphered_1 = read_string_of_bits("12-testdata/ciphered/test1.txt")
ciphered_2 = read_string_of_bits("12-testdata/ciphered/test2.txt")

a = (int(text_1, 2)**e) - int(ciphered_1, 2)
b = (int(text_2, 2)**e) - int(ciphered_2, 2)
result = gcd(a,b)
print(result)
