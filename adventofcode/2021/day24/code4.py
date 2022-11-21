
optype =  [ 1,  1,  1, 26,  1, 26, 26,  1,  26,  1,  1, 26, 26, 26]
correction =  [11, 11, 15,-14, 10,  0, -6, 13,  -3, 13, 15, -2, -9, -2]
offset = [ 6, 14, 13,  1,  6, 13,  6,  3,   8, 14,  4,  7, 15,  1]

inp = [5,1,9,8,3,9,9,9,9,4,7,9,9,9]

x = 0
y = 0
z = 0
for i, w in enumerate(inp):
    x = (z % 26) + correction[i]
    z = z // optype[i]

    if x != w:
        z = (z * 26) + w + offset[i]

print(z)
