# From plain text and encripted text we can obtain the key

# plain = "514;248;980;347;145;332"
# encripted = "3633363A33353B393038383C363236333635313A353336"
# key = ""
# for i, p in enumerate(plain):
#   e = encripted[(i*2):(i*2)+2]
#   key += str(ord(p) ^ int(e, 16))
# print(key)

# This key in the original algoritm is in reverse order



# ENCRYPT ALGORITHM
# plain = "514;248;980;347;145;332"
# key = "32211132908756187141604"
# encripted = ""
# for i, p in enumerate(plain):
#   k = int(key[i])
#   encripted += '%02X' % (ord(p) ^ k)
# print(encripted)



# DECRYPT ALGORITHM
encripted = "3A3A333A333137393D39313C3C3634333431353A37363D"
key = "32211132908756187141604"
plain = ""
for i, k in enumerate(key):
  e = encripted[(i*2):(i*2)+2]
  plain += chr(int(e, 16) ^ int(k))
print(plain)