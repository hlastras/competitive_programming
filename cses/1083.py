n = int(input())
see = [False]*n
numbers = [int(x) for x in input().split()]
for v in numbers:
  see[v-1] = True
print(see.index(False)+1)