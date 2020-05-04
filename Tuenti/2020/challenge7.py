querty = "`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
dvorak = "`1234567890[]',.pyfgcrl/=\aoeuidhtns-;qjkxbmwvz~!@#$%^&*(){}\"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ "

dvorak_to_querty = {}
for d, q in zip(dvorak, querty):
  if d != q:
    dvorak_to_querty[d] = q

n = int(input())
for case in range(1, n+1):
  line = input()
  new_line = ""
  for c in line:
    if c in dvorak_to_querty:
      new_line += dvorak_to_querty[c]
    else:
      new_line += c

  print("Case #%d: %s" % (case, new_line))