from sys import stdin, stdout 

n, p = map(int, stdin.readline().split())
students = list(map(lambda x: x-p, map(int, stdin.readline().split())))

sum = 0
ans = 0
for n in students:
  sum += n
  ans = max(ans, sum)
  if sum < 0:
    sum = 0
stdout.write("%d\n" % ans)
