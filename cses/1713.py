import random
import time
from fractions import gcd

n = int(raw_input())

def is_probable_prime(n, k = 1):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True   
def pollard(N):
    if N % 2 == 0:
        return 2
    y, c, m = random.randint(1, N - 1), random.randint(1, N - 1), random.randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r *= 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break

    return g

def pollard_rho(n, seed=2, f=lambda x: x**2 + 1):
   x, y, d = seed, seed, 1
   while d == 1:
     x = f(x) % n
     y = f(f(y)) % n
     d = gcd((x - y) % n, n)
   return None if d == n else d

def f(n, list):
    if n == 1:
        return
    if is_probable_prime(n):
        list.append(n)
        return

    factor = pollard(n)
    f(factor, list)
    f(n/factor, list)


for _ in range(n):
    v = int(raw_input())
    if v==1:
        print 1
    else:
        factors = []
        f(v, factors)
        factors.sort()

        result = 1
        pas = factors[0]
        count = 0
        for x in factors:
            if x == pas:
                count += 1
            else:
                result *= (count + 1)
                pas = x
                count = 1

        result *= (count + 1)

        print result

