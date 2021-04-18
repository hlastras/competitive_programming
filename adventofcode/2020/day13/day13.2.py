# Solved using the Chinese remainder theorem algorithm copied from here: https://github.com/stevenhalim/cpbook-code/blob/master/ch9/heliocentric.py

input()
buses = input().split(",")

def extEuclid(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(b, m):
    d, x, y = extEuclid(b,m)
    if d != 1:
        raise ValueError
    return x % m

def crt(r, m):
    n = len(m)
    mt = 1
    for i in range(n):
        mt *= m[i]
    sm = 0
    for i in range(n):
        p = mt//m[i]
        sm += r[i] * modinv(p, m[i]) * p
    return sm % mt

a = []
b = []
for i, value in enumerate(buses):
  if value != "x":
    value = int(value)
    a.append(value-i)
    b.append(value)
print(crt(a, b))