import bisect
n = int(input())
A = [int(x) for x in input().split()]
L = []
for i in range(len(A)):
  pos = bisect.bisect_left(L, A[i])
  if pos >= len(L):
    L.append(A[i])
  else:
    L[pos] = A[i]
print(len(L))