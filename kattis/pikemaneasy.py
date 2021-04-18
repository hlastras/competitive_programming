n, t = [int(x) for x in input().split()]
a, b, c, t0 = [int(x) for x in input().split()]

arr = [t0] * n
for i in range(n-1):
  arr[i+1]=(((a*arr[i] + b) % c) + 1)

arr.sort()

penalty = 0
solved = 0
time_elapsed = 0
while solved < n and time_elapsed + arr[solved] < t:
  time_elapsed += arr[solved]
  solved += 1
  penalty += time_elapsed


print(solved, penalty%1000000007)