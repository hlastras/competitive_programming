from sys import stdin, stdout   
n, q = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))

p = [0]*(n+1)
for i, v in enumerate(numbers):
  p[i+1] = p[i]+v
  
for _ in range(q):
  a, b = map(int, stdin.readline().split())
  stdout.write("%d\n" % (p[b]-p[a-1]))